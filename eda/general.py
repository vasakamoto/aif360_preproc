
from src.configs import PATH_ROOT

import seaborn as sns
import numpy as np
from pandas import DataFrame
from matplotlib import pyplot as plt


##  ~~IDENTIFY IDS (distinct(n) = len) AND CONSTANTS (distinct(n) = 1)~~
##  **PROOF**
##
##  ~~CLASSIFY VARIABLES~~
##      ~~CATEGORIES~~
##          ~~NOMINAL: OBJECT OR BOOL~~
##          ~~ORDINAL: NUMERIC LOW CARDINALITY~~
##      ~~continuous~~
##  **PROOF**
##
##  ~~GENERAL BEHAVIOR~~
##      ~~CATEGORIES~~
##          ~~FREQUENCY: HISTOGRAM (check general distribution)~~
##      ~~CONTINUOUS~~
##          ~~FREQUENCY: FUNCTION DISTRIBUTION (check general distribution)~~
##  **FORMAT**
##      ALIGN LABELS (x axis is vertically aligned)
##      FORMAT LABELS (float to integer in some cases)
##      SCALE (facilitates visualization of rare categories)
##  **VISUALIZE PASSED AND REPROVED ("legends")**
        

def _unique_constant(df : DataFrame) -> dict[str, list]:
     """Check for categorical variables with cardinality = size(df) and cardinality = 1"""
 
     unique = []
     constant = []
 
     for label, data in df.items():
         if data.count() == data.nunique():
             unique.append(label)
         if data.count() == 1:
             constant.append(label)
 
     return {
             "unique" : unique,
             "constant" : constant
             }


def _null_features(df : DataFrame) -> None:
    "Check for significance of null values of features"

    white = df.loc[df["race1"] == "white"].dropna().count()
    color = df.loc[df["race1"] != "white"].dropna().count()
    na_white = df.loc[df["race1"] == "white"].isna().sum()
    na_color = df.loc[df["race1"] != "white"].isna().sum()
    print(f"SIGNIFICATIVE NULL VALUES\nrelative frequency of:\n{'columns'.ljust(10)} |{'no_na':>10} |{'na':>10} |{'na/no_na':>10}| color", end="\n\n")
    for i, v in white.items():
        if round(na_white[i] / white[i] * 100, 2) > 1:
            print(f"{i.ljust(10)} |{round(white[i] / df.shape[0] * 100, 2):>10} |{round(na_white[i] / df.shape[0] * 100, 2):>10} |{round(na_white[i] / white[i] * 100, 2):>10}| white")
            print(f"{i.ljust(10)} |{round(color[i] / df.shape[0] * 100, 2):>10} |{round(na_color[i] / df.shape[0] * 100, 2):>10} |{round(na_color[i] / color[i] * 100, 2):>10}| color")
    print("--------------------------------")
    
    # is not possible to simple drop null values from DataFrame because there are 
    # features that have a significative proportion of null / non null values which
    # could be a new source of bias
    # use MICE (multivariate imputation by chained equations) or group-wise imputation 
    # when training model to treat null values


def _classify_variables(df : DataFrame) -> dict[str, list]:
    """Classify variables into categorical (ordinal and nominal) and continuous"""

    ordinal = []
    nominal = []
    binary = []
    continuous = []
    others = []

    for label, data in df.items():
        non_null = data.dropna()
        if non_null.dtype in ["str", "object"]:
            nominal.append(label)
        elif non_null.value_counts().size == 2:
            binary.append(label)
        elif (non_null == non_null.astype(int)).all():
            ordinal.append(label)
        elif ((data - data.round().abs()) < 0).any():
            continuous.append(label)
        else:
            others.append(label)


    return {
            "ordinal" : ordinal,
            "binary" : binary,
            "nominal" : nominal,
            "continuous" : continuous,
            "others" : others
            }
 

def _abs_distribution(df : DataFrame, classified : dict[str, list],
                                    target : str) -> None:
    """Check for absolute distribution of variables by target variable"""

    for k, v in classified.items():
        if k in ["ordinal", "binary", "nominal"]:
            for c in v:
                if c == target: continue
                sns.histplot(
                        data=df[[c, target]],
                        x=c,
                        stat="density",
                        hue=target,
                        element="step",
                        palette="viridis",
                        )
                plt.xlabel(c)
                plt.ylabel("Frequency")
                plt.savefig(PATH_ROOT/"img"/f"hist_{c}")
                plt.close()
        elif k == "continuous":
            for c in v:
                sns.kdeplot(
                        data=df[[c, target]],
                        x=c,
                        hue=target,
                        fill=True,
                        common_norm=False,
                        palette='crest',
                        alpha=0.5
                        )
                plt.xlabel(c)
                plt.ylabel(target)
                plt.savefig(PATH_ROOT/"img"/f"f_freq_{c}")
                plt.close()
        else:
            continue

    return


def _rel_distribution(df : DataFrame, classified : dict[str, list],
                                    target : str) -> None:
    """Check for relative distribution of variables by target variable"""

    for k, v in classified.items():
        if k in ["ordinal", "binary", "nominal"]:
            for c in v:
                if c == target: continue
                s = df[[c, target]].value_counts()
                sns.histplot(
                        data=df[[c, target]],
                        x=c,
                        hue=target,
                        element="step",
                        stat="percent",
                        palette="viridis",
                        )
                #acc = {}
                #for i, v in s.items():
                #    acc[str(i[0])] = acc.get(str(i[0]), 0) + v
                #s = s.astype("float64")
                #for i, v in s.items():
                #    s[i] = round(v / acc[str(i[0])], 2)
                #s = s.reset_index(name="relative_frequency")
                #sns.barplot(
                #        data=s,
                #        x=c,
                #        y="relative_frequency",
                #        hue=target,
                #        stacked=True,
                #        palette="viridis",
                #        )
                plt.xlabel(c)
                plt.ylabel("Frequency")
                plt.savefig(PATH_ROOT/"img"/f"rel_hist_{c}")
                plt.close()
                return
        elif k == "continuous": continue


def _plot_clustered_stacked(dfall, labels=None, title="multiple stacked bar plot",  H="/", **kwargs):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""
    n_df = len(dfall)
    n_col = len(dfall[0].columns) 
    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)
    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=0,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      **kwargs)  # make bar plots
    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                rect.set_hatch(H * int(i / n_col)) #edited part     
                rect.set_width(1 / float(n_df + 1))
    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(df.index, rotation = 0)
    axe.set_title(title)
    # Add invisible data to add another legend
    n=[]        
    for i in range(n_df):
        n.append(axe.bar(0, 0, color="gray", hatch=H * i))
    l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
    if labels is not None:
        l2 = plt.legend(n, labels, loc=[1.01, 0.1]) 
    axe.add_artist(l1)
    return axe


def analysis_general(df : DataFrame) -> None:

    #_null_features(df)
    #_corr_features(df)

    data = df.drop(columns=[
        "decile1",                  # deciles from zfygpa
        "decile1b",                 # deciles from zfygpa
        "decile3",                  # deciles from gpa
        "ID",                       # unique identifier for instances
        "Dropout",                  # ???
        "grad",                     # ???
        "cluster",                  # reordered tier
        "parttime",                 # fulltime inverted
        "sex",                      # label encoding from gender
        "gender",                   # nominal for male 
        "race1",                    # nominal for race
        "race2",                    # grouped hisp, asian and other into other
        "asian",                    # hot encoded from race1
        "black",                    # hot encoded from race1
        "hisp",                     # hot encoded from race1
        "other",                    # hot encoded from race1
        "bar_passed",               # boolean for pass_bar
        "bar",                      # nominal for approvation by attempt
        "bar1",                     # nominal for pass_bar
        "bar2",                     # nominal for pass_bar
        "index6040",                # derived from lsat
        "indxgrp",                  # grouped index6040
        "indxgrp2",                 # grouped index6040
        "gpa",                      # same as ugpa
        "dnn_bar_pass_prediction",  # prediction for deep neural networks
        "DOB_yr",                   # birth year
        "bar2_yr",                  # year of approvation
        "age",                      # ??? but derived from 
        "bar1_yr",                  # difference between age and DOB_yr
        ])

    # transform bar2_yr and DOB_yr into age of approvation
    data["age"] = df["bar2_yr"] - df["DOB_yr"]

    print(f"\nCOLUMNS BEFORE {df.shape[1]}\nCOLUMNS AFTER {data.shape[1]}")
    print(f"\nDATASET DIMENSIONS: f{data.shape}")

    buffer = _unique_constant(data)

    print("VARIABLES CLASSIFICATION")
    print(f"\tUNIQUE: {buffer['unique']}")
    print(f"\tCONSTANTS: {buffer['constant']}") 

    buffer = _classify_variables(data)

    print(f"\tBINARY: {buffer['binary']}")
    print(f"\tORDINAL: {buffer['ordinal']}")
    print(f"\tNOMINAL: {buffer['nominal']}") 
    print(f"\tCONTINUOUS: {buffer['continuous']}") 
    print(f"\tOTHERS: {buffer['others']}") 

    #_abs_distribution(data, buffer, "pass_bar")
    #_rel_distribution(data, buffer, "pass_bar")
    #_abs_distribution_by_protected(data, buffer, "pass_bar", "male")

    # testing grouped stacked columns
    #df1 = DataFrame(np.random.rand(4, 5),
    #                   index=["A", "B", "C", "D"],
    #                   columns=["I", "J", "K", "L", "M"])
    #df2 = DataFrame(np.random.rand(4, 5),
    #                   index=["A", "B", "C", "D"],
    #                   columns=["I", "J", "K", "L", "M"])
    #df3 = DataFrame(np.random.rand(4, 5),
    #                   index=["A", "B", "C", "D"], 
    #                   columns=["I", "J", "K", "L", "M"])

    #_plot_clustered_stacked([df1, df2, df3],["df1", "df2", "df3"])
