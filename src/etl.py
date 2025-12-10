

from pathlib import Path

import numpy as np
from aif360.datasets import StandardDataset, BinaryLabelDataset
from aif360.algorithms.preprocessing.reweighing import Reweighing
from pandas import (
    DataFrame,
    read_csv,
    merge
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

from .configs import (
    PRIVILEGED_GROUP,
    UNPRIVILEGED_GROUP,
    TARGET,
    FAVORABLE_OUTCOME,
    PROTECTED_ATTRIBUTES
)

def _ingest() -> DataFrame:
    path_csv = Path().cwd() / "tcc/bar_pass_prediction/bar_pass_prediction.csv"
    return read_csv(
        path_csv,
        index_col="ID",
        encoding="utf-8",
    )


def _process(df : DataFrame) -> DataFrame:

    df.dropna(inplace=True)
    
    # drop redundant and colinear attributes
    dcolumns = [
        # redundant
        "asian",                            # hot encoded race
        "bar",                              # categorization of passage by tries
        "bar1",                             # the model evaluates bar passage, not if passed on first try
        "bar2",                             # idem
        "bar_passed",                       # boolean for pass_bar
        "black",                            # hot encoded race
        "cluster",                          # reordering of tier
        "decile1b",                         # not the same as decile1, but there is almost no variance
        "Dropout",                          # inverse of grad
        "gender",                           # categorization of sex with string
        "hisp",                             # hot encoded race
        "indxgrp",                          # categorization of index6040
        "indxgrp2",                         # subcategorization of index6040
        "male",                             # hot encoded sex
        "other",                            # hot encoded race
        "parttime",                         # inverse of fulltime
        "race1",                            # categorization of race with string
        "race2",                            # subcategorization of race with string 
        "ugpa",                             # same as gpa

        # colinear
        "decile1",                          # zfygpa
        "decile3",                          # zgpa

        # useless
        "dnn_bar_pass_prediction",          # prediction with dnn
        "grad",                             # all values are true

        # not sure what is exactly
        "age",                              # have no clue
        "bar1_yr",                          # DOB_yr - age, but what does it means...
        #"index6040",                       # how this was calculated??
        #"zfygpa",                          # how this was calculated??
        #"zgpa",                            # how this was calculated?? 

        # not sure if is useful
        "bar2_yr",                         # year of aprovation
        "DOB_yr",                          # birth year

        # selected features
        #"fam_inc",                         # ordered categorization of family income
        #"fulltime",                        # if is fulltime student
        #"gpa",                             # grade point average
        #"lsat",                            # score at law school admission test
        #"pass_bar",                        # target
        #"race",                            # non binary category
        #"sex",                             # binary category
        #"tier",                            # ordered categorization of institution grouped by averages in lsat and gpa
    ]
    df.drop(columns=dcolumns, inplace=True)

    # type columns
    types = {
        # redundant
        #"asian"                     :   "category",
        #"bar"                       :   "category",
        #"bar1"                      :   "category",
        #"bar2"                      :   "category",
        #"bar_passed"                :   "category",
        #"black"                     :   "category",
        #"cluster"                   :   "int8",
        #"decile1b"                  :   "int8",
        #"Dropout"                   :   "category",
        #"gender"                    :   "category",
        #"hisp"                      :   "category",
        #"indxgrp"                   :   "category",
        #"indxgrp2"                  :   "category",
        #"male"                      :   "category",
        #"other"                     :   "category",
        #"parttime"                  :   "category",
        #"race1"                     :   "category",
        #"race2"                     :   "category",
        #"ugpa"                      :   "float32",

        # colinear
        #"decile1"                   :   "int8",
        #"decile3"                   :   "int8",

        # useless
        #"grad"                      :   "category",
        #"dnn_bar_pass_prediction"   :   "float32",

        # not sure what is exactly
        #"age"                       :   "int8",
        #"bar1_yr"                   :   "int8",
        "index6040"                 :   "float32",
        "zfygpa"                    :   "float32",
        "zgpa"                      :   "float32",

        # not sure if is useful
        #"bar2_yr"                   :   "int8",
        #"DOB_yr"                    :   "int8",

        # selected features
        "fam_inc"                   :   "category",
        "fulltime"                  :   "category",
        "gpa"                       :   "float32",
        "lsat"                      :   "float32",
        "pass_bar"                  :   "category",
        "race"                      :   "int8",
        "sex"                       :   "int8",
        "tier"                      :   "category",
    }
    df = df.astype(types)

    # encode categoric columns
    cat_columns = df.select_dtypes(include="category").columns.tolist()
    cat_encoder = OrdinalEncoder()
    df[cat_columns] = cat_encoder.fit_transform(df[cat_columns])

    # transform race into binary category (white, non-white)
    df['race'] = df['race'].apply(lambda x : 0 if x != 7 else 1)

    return df


def _samples(df : DataFrame | BinaryLabelDataset) -> dict:

    if isinstance(df, BinaryLabelDataset):
        XY, XYTV = df.split([0.5], shuffle=True, seed=42)
        XYT, XYV = XYTV.split([0.5], shuffle=True, seed=42)
        return {
            "train" : [XY.features, XY.labels.astype(int).ravel(), XY.instance_weights.flatten()],
            "test" : [XYT.features, XYT.labels.ravel(), XYT.instance_weights.ravel().flatten()],
            "validation" : [XYV.features, XYV.labels.ravel(), XYV.instance_weights.ravel().flatten()],
        }

    c = df.columns.tolist()
    c.remove(TARGET)
    X = df[c]
    y = df[TARGET]
    X_TR, X_VT, y_tr, y_vt = train_test_split(X, y, train_size=0.5, stratify=y, random_state=0)
    X_V, X_T, y_v, y_t = train_test_split(X_VT, y_vt, train_size=0.5, stratify=y_vt, random_state=0)

    return {
        "train" : [X_TR, y_tr],
        "test" : [X_T, y_t],
        "validation" : [X_V, y_v]
    }


def _reweight(samples : dict) -> StandardDataset:
    odf = merge(samples["train"][0], samples["train"][1], right_index=True, left_index=True) 
    sds = StandardDataset(
        odf,
        label_name=TARGET,
        favorable_classes=FAVORABLE_OUTCOME,
        protected_attribute_names=PROTECTED_ATTRIBUTES,
        privileged_classes=[[p["race"] for p in PRIVILEGED_GROUP]],
    )
    rw = Reweighing(
        privileged_groups=PRIVILEGED_GROUP,
        unprivileged_groups=UNPRIVILEGED_GROUP,
    )
    rw.fit(sds)
    rw_ds = rw.transform(sds) 
    return rw_ds

def load() -> dict[str,dict[str,DataFrame] | DataFrame | StandardDataset]:
    df = _ingest()
    df = _process(df)
    samples = _samples(df)
    rw_df = _reweight(samples)
    debiased_samples = _samples(rw_df)

    return {
        "original_dataframe" : df,
        "reweighted_dataframe" : rw_df,
        "original_samples" : samples,
        "reweighted_samples" : debiased_samples
    }

