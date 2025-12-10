
from os import system
from pathlib import Path

from aif360.metrics import ClassificationMetric, BinaryLabelDatasetMetric
from aif360.datasets import StandardDataset
from aif360.algorithms.preprocessing import Reweighing
from matplotlib import pyplot
from pandas import (
    DataFrame,
    read_csv,
    concat,
    Series
)
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
    roc_auc_score,
    confusion_matrix
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder


def model():
    # ingest dataset
    path_csv = Path().cwd() / "tcc/bar_pass_prediction/bar_pass_prediction.csv"
    df = read_csv(
        path_csv,
        index_col="ID",
        encoding="utf-8",
    ).dropna() # There is enough data to exclude instances with null values


    # preprocess dataset
    # dropping redundant attributes
    dcolumns = [
        "decile1b",
        "decile3",
        "decile1",
        #"sex",
        #"race",
        "cluster",
        #"lsat",
        "ugpa",
        "zfygpa",
        #"DOB_yr",
        "grad",
        "zgpa",
        "bar1",
        "bar1_yr",
        "bar2",
        "bar2_yr",
        #"fulltime",
        #"fam_inc",
        "age",
        "gender",
        "parttime",
        "male",
        "race1",
        "race2",
        "Dropout",
        "other",
        "asian",
        "black",
        "hisp",
        #"pass_bar",
        "bar",
        "bar_passed",
        "tier",
        #"index6040",
        "indxgrp",
        "indxgrp2",
        "dnn_bar_pass_prediction",
        #"gpa",
    ]
    df.drop(columns=dcolumns, inplace=True)

    # typing attributes
    types = {
        #"decile1b"                  :   "int8",
        #"decile3"                   :   "int8",
        #"decile1"                   :   "int8",
        "sex"                       :   "int8",
        "race"                      :   "int8",
        #"cluster"                   :   "int8",
        "lsat"                      :   "float32",
        #"ugpa"                      :   "float32",
        "zfygpa"                    :   "float32",
        #"DOB_yr"                    :   "int8",
        #"grad"                      :   "category",
        #"zgpa"                      :   "float32",
        #"bar1"                      :   "category",
        #"bar1_yr"                   :   "int8",
        #"bar2"                      :   "category",
        #"bar2_yr"                   :   "int8",
        "fulltime"                  :   "category",
        "fam_inc"                   :   "category",
        #"age"                       :   "int8",
        #"gender"                    :   "category",
        #"parttime"                  :   "category",
        #"male"                      :   "category",
        #"race1"                     :   "category",
        #"race2"                     :   "category",
        #"Dropout"                   :   "category",
        #"other"                     :   "category",
        #"asian"                     :   "category",
        #"black"                     :   "category",
        #"hisp"                      :   "category",
        "pass_bar"                  :   "category",
        #"bar"                       :   "category",
        #"bar_passed"                :   "category",
        #"tier"                      :   "category",
        #"index6040"                 :   "float32",
        #"indxgrp"                   :   "category",
        #"indxgrp2"                  :   "category",
        #"dnn_bar_pass_prediction"   :   "float32",
        "gpa"                       :   "float32",
    }
    df = df.astype(types)

    # balancing dataset
    #repro = df.loc[df['pass_bar'] == 0]
    #aprov = df.loc[df['pass_bar'] == 1].sample(1040)
    #df = concat([repro, aprov])

    # categorizing attributes
    cat_columns = df.select_dtypes(include="category").columns.tolist()
    cat_encoder = OrdinalEncoder()

    # process dataset
    target = "pass_bar"
    columns = [
        c for c in df.columns.tolist() if c not in (
            target, "bar", "bar1", "bar2", "bar_passed", "dnn_bar_pass_prediction"
        )
    ] 
    x = df[columns]
    y = df[target]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.4, train_size=0.6, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    system("cls")
    print(f"Baseline accuracy on train data: {model.score(x_train, y_train)}")
    print(f"Baseline accuracy on test data: {model.score(x_test, y_test)}")

    y_pred = model.predict(x_test)
    y_pred_prob = model.predict_proba(x_test)[:, 1]
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, pos_label=1)
    recall = recall_score(y_test, y_pred, pos_label=1)
    f1 = f1_score(y_test, y_pred, pos_label=1)
    roc_auc = roc_auc_score(y_test, y_pred_prob)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Acurácia: {acc:.4f}")
    print(f"Precision (Classe Positiva): {prec:.4f}")
    print(f"Recall (Classe Positiva): {recall:.4f}")
    print(f"F1-Score (Classe Positiva): {f1:.4f}")
    print(f"ROC AUC Score: {roc_auc:.4f}")
    print("\nMatriz de Confusão:")
    print(cm)


    df_bias = StandardDataset(
        df,
        label_name="pass_bar",
        favorable_classes=[1],
        protected_attribute_names=["race"],
        privileged_classes=[[7]],
    )

    y_bias = model.predict(x)

    df_pred_bias = df_bias.copy()
    df_pred_bias.labels = y_bias

    #metric_orig_train = BinaryLabelDatasetMetric(
    #    df_bias, 
    #    unprivileged_groups=[{"race" : 3}],
    #    privileged_groups=[{"race" : 7}]
    #)

    #print("Mean Difference = %f" % metric_orig_train.mean_difference())
    #print("Statistical Parity Difference = %f" % metric_orig_train.statistical_parity_difference())
    #print("Disparate Impact = %f" % metric_orig_train.disparate_impact())

    fair_metrics = ClassificationMetric (
        df_bias,
        df_pred_bias,
        unprivileged_groups=[{"race" : 3}],
        privileged_groups=[{"race" : 7}]
    )



    print("Mean Difference = %f" % fair_metrics.mean_difference())
    print("Statistical Parity Difference = %f" % fair_metrics.statistical_parity_difference())
    print("Disparate Impact = %f" % fair_metrics.disparate_impact())

    # Diferença de Igualdade de Oportunidade (Equal Opportunity Difference)
    print(f"Equal Opportunity Difference: {fair_metrics.equal_opportunity_difference():.4f}")

    # Diferença de Odds Médias (Average Odds Difference)
    # Representa a média da diferença de TPR e FPR entre os grupos.
    print(f"Average Odds Difference (AOD): {fair_metrics.average_odds_difference():.4f}")

    # Métricas individuais para contextualização
    tpr_diff = fair_metrics.difference(fair_metrics.true_positive_rate)
    fpr_diff = fair_metrics.difference(fair_metrics.false_positive_rate)
    print(f"   -> Diferença de TPR (Recall): {tpr_diff:.4f}")
    print(f"   -> Diferença de FPR: {fpr_diff:.4f}")
