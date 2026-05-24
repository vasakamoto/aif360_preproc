

from dataclasses import fields

from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier

from src.configs import (
        PATH_ROOT,
        SplitDataset,
        TrainedModels,
        PRIVILEGED_GROUP,
        UNPRIVILEGED_GROUP
        )


def _fairness_metrics(model : RandomForestClassifier, ds_validation : BinaryLabelDataset,
         ds_test : BinaryLabelDataset) -> dict:

    y_pred_test = model.predict(ds_test.features)
    pred_ds_test = ds_test.copy(deepcopy=True)
    pred_ds_test.labels = y_pred_test.reshape(-1, 1)

    y_pred_validation = model.predict(ds_validation.features)
    pred_ds_validation = ds_validation.copy(deepcopy=True)
    pred_ds_validation.labels = y_pred_validation.reshape(-1, 1)

    cm_test = ClassificationMetric(
            ds_test,
            pred_ds_test,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP,
            )

    cm_validation = ClassificationMetric(
            ds_validation,
            pred_ds_validation,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP,
            )

    return {
            "test_statistical_parity_difference": round(cm_test.statistical_parity_difference(), 3),
            "test_disparate_impact": round(cm_test.disparate_impact(), 3),
            "test_equal_opportunity_difference": round(cm_test.equal_opportunity_difference(), 3),
            "test_average_odds_difference": round(cm_test.average_odds_difference(), 3),
            "test_false_positive_rate_diff": round(cm_test.false_positive_rate_difference(), 3),
            "test_false_discovery_rate_diff": round(cm_test.false_discovery_rate_difference(), 3),
            "validation_statistical_parity_difference": round(cm_validation.statistical_parity_difference(), 3),
            "validation_disparate_impact": round(cm_validation.disparate_impact(), 3),
            "validation_equal_opportunity_difference": round(cm_validation.equal_opportunity_difference(), 3),
            "validation_average_odds_difference": round(cm_validation.average_odds_difference(), 3),
            "validation_false_positive_rate_diff": round(cm_validation.false_positive_rate_difference(), 3),
            "validation_false_discovery_rate_diff": round(cm_validation.false_discovery_rate_difference(), 3),
            }


def _prediction_frequency(model : RandomForestClassifier, split_ds : SplitDataset, nm : str="") -> dict:

    df_test = DataFrame(split_ds.test.features, columns=split_ds.test.feature_names)
    df_test["target_real"] = split_ds.test.labels.ravel()
    df_test["target_predicted"] = model.predict(split_ds.test.features)

    df_validation = DataFrame(split_ds.validation.features, columns=split_ds.validation.feature_names)
    df_validation["target_real"] = split_ds.validation.labels.ravel()
    df_validation["target_predicted"] = model.predict(split_ds.validation.features)

    df_confused_test = DataFrame(index=df_test["race"].value_counts().index)
    test_real_negative = df_test[df_test["target_real"] == 0]["race"].value_counts()
    test_real_positive = df_test[df_test["target_real"] == 1]["race"].value_counts()
    test_true_negative = df_test[(df_test["target_real"] == 0) & (df_test["target_predicted"] == 0)]["race"].value_counts()
    test_true_positive = df_test[(df_test["target_real"] == 1) & (df_test["target_predicted"] == 1)]["race"].value_counts()
    test_false_negative = df_test[(df_test["target_real"] == 1) & (df_test["target_predicted"] == 0)]["race"].value_counts()
    test_false_positive = df_test[(df_test["target_real"] == 0) & (df_test["target_predicted"] == 1)]["race"].value_counts()

    df_confused_test["abs_true_negative"]  = test_true_negative
    df_confused_test["abs_true_positive"]  = test_true_positive
    df_confused_test["abs_false_negative"] = test_false_negative
    df_confused_test["abs_false_positive"] = test_false_positive
    df_confused_test["rel_true_negative"]  = test_true_negative / test_real_negative
    df_confused_test["rel_true_positive"]  = test_true_positive / test_real_positive
    df_confused_test["rel_false_negative"] = test_false_negative / test_real_positive
    df_confused_test["rel_false_positive"] = test_false_positive / test_real_negative

    df_confused_validation = DataFrame(index=df_validation["race"].value_counts().index)
    validation_real_negative = df_validation[df_validation["target_real"] == 0]["race"].value_counts()
    validation_real_positive = df_validation[df_validation["target_real"] == 1]["race"].value_counts()
    validation_true_negative = df_validation[(df_validation["target_real"] == 0) & (df_validation["target_predicted"] == 0)]["race"].value_counts()
    validation_true_positive = df_validation[(df_validation["target_real"] == 1) & (df_validation["target_predicted"] == 1)]["race"].value_counts()
    validation_false_negative = df_validation[(df_validation["target_real"] == 1) & (df_validation["target_predicted"] == 0)]["race"].value_counts()
    validation_false_positive = df_validation[(df_validation["target_real"] == 0) & (df_validation["target_predicted"] == 1)]["race"].value_counts()

    df_confused_validation["abs_true_negative"]  = validation_true_negative
    df_confused_validation["abs_true_positive"]  = validation_true_positive
    df_confused_validation["abs_false_negative"] = validation_false_negative
    df_confused_validation["abs_false_positive"] = validation_false_positive
    df_confused_validation["rel_true_negative"]  = validation_true_negative / validation_real_negative
    df_confused_validation["rel_true_positive"]  = validation_true_positive / validation_real_positive
    df_confused_validation["rel_false_negative"] = validation_false_negative / validation_real_positive
    df_confused_validation["rel_false_positive"] = validation_false_positive / validation_real_negative

    if nm:
# 1. Separar os dados em dois DataFrames estruturados por classe real
        df_real_neg = df_confused_test[['rel_true_negative', 'rel_false_positive']].copy()
        df_real_neg.columns = ['Verdadeiro Negativo (TN)', 'Falso Positivo (FP)']

        df_real_pos = df_confused_test[['rel_true_positive', 'rel_false_negative']].copy()
        df_real_pos.columns = ['Verdadeiro Positivo (TP)', 'Falso Negativo (FN)']

# 2. Plotar os gráficos lado a lado para comparação entre as raças
        fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

        df_real_neg.plot(kind='bar', stacked=True, ax=axes[0], colormap='coolwarm')
        axes[0].set_title('Distribuição dos Casos Reais Negativos')
        axes[0].set_ylabel('Proporção')

        df_real_pos.plot(kind='bar', stacked=True, ax=axes[1], colormap='viridis')
        axes[1].set_title('Distribuição dos Casos Reais Positivos')

        plt.savefig(PATH_ROOT/"results"/"charts"/"evaluation"/f"stacked_{nm}")

    abs_values = ["abs_true_negative", "abs_true_positive", "abs_false_negative", "abs_false_positive"]

    return {
            "test" : df_confused_test[abs_values],
            "validation" : df_confused_validation[abs_values]
            }


def fair_metrics(models : TrainedModels, split_ds : SplitDataset) -> DataFrame:

    d = {
            "metrics" : [],
            "raw" : [],
            "reweighing" : [],
            "disparate_impact_remover" : [],
            "learning_fair_representations" : [],
            }

    d["metrics"].extend([k for k in _fairness_metrics(models.raw, split_ds.validation, split_ds.test).keys()])

    c = {}

    for model in fields(models):

        if model.name not in d.keys(): continue

        res = _fairness_metrics(getattr(models, model.name), split_ds.validation, split_ds.test)
        d[model.name].extend([res[k] for k in res.keys()])
        c.update({model.name : _prediction_frequency(getattr(models, model.name), split_ds, model.name)})

    d = DataFrame(d)

    with open(PATH_ROOT/"results"/"tables"/"evaluation.md", "a") as file:
        file.write("\n\nFAIRNESS METRICS\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        for k in c.keys():
            file.write(f"\n\nCONSUFION MATRIX - {k.upper()}\n\n")
            c[k]["test"].to_markdown(file)
            file.write("\n\n")
            c[k]["validation"].to_markdown(file)
            file.write("\n\n\n")
            file.write("_"*100)

    return d
