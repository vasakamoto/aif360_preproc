
from dataclasses import fields

from aif360.datasets import BinaryLabelDataset
from numpy import mean
from pandas import DataFrame
from pandas._libs.hashtable import mode
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
        accuracy_score,
        f1_score,
        recall_score,
        precision_score,
        roc_auc_score,
        confusion_matrix,
        )

from src.configs import (
        PATH_ROOT,
        GroupedProcessedDatasets,
        SplitDataset,
        TrainedModels
        )


def _std(model : RandomForestClassifier, ds_validation : BinaryLabelDataset,
         ds_test : BinaryLabelDataset) -> dict:

    def cm_to_df(cm) -> DataFrame:
        # [TN, FP]
        # [FN, TP]
        cm = {
                "/" : ["REAL NEGATIVE", "REAL POSITIVE"],
                "PREDICTED NEGATIVE" : [cm[0,0], cm[1,0]],
                "PREDICTED POSITIVE" : [cm[0,1], cm[1,1]]
                }

        return DataFrame(cm)

    X_test = ds_test.features
    X_validation = ds_validation.features

    y_test = ds_test.labels.ravel()
    y_validation = ds_validation.labels.ravel()

    y_pred_test = model.predict(X_test)
    y_pred_validation = model.predict(X_validation)

    y_prob_test = model.predict_proba(X_test)[:, 1]
    y_prob_validation = model.predict_proba(X_validation)[:, 1]

    return {
            "test_baseline_accuracy" : round(max(mean(y_test == 1), mean(y_test == 0)), 3),
            "test_accuracy" : round(accuracy_score(y_test, y_pred_test), 3),
            "test_precision" : round(precision_score(y_test, y_pred_test, pos_label=1), 3),
            "test_recall" : round(recall_score(y_test, y_pred_test, pos_label=1), 3),
            "test_f1" : round(f1_score(y_test, y_pred_test, pos_label=1), 3),
            "test_roc_auc" : round(roc_auc_score(y_test, y_prob_test), 3),
            "test_confusion_matrix" : cm_to_df(confusion_matrix(y_test, y_pred_test)),
            "validation_baseline_accuracy" : round(max(mean(y_validation == 1), mean(y_validation == 0)), 3),
            "validation_accuracy" : round(accuracy_score(y_validation, y_pred_validation), 3),
            "validation_precision" : round(precision_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_recall" : round(recall_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_f1" : round(f1_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_roc_auc" : round(roc_auc_score(y_validation, y_prob_validation), 3),
            "validation_confusion_matrix" : cm_to_df(confusion_matrix(y_validation, y_pred_validation)),
            }


def std_metrics(models : TrainedModels, grouped_ds : GroupedProcessedDatasets,
            split_ds : SplitDataset) -> DataFrame:

    d = {
            "metrics" : [],
            "raw" : [],
            "reweighing" : [],
            "disparate_impact_remover" : [],
            "learning_fair_representations" : [],
            }

    c = {
            "dataset" : [],
            "validation_confusion_matrix" : [],
            "test_confusion_matrix" : []
            }

    d["metrics"].extend([
        k for k in _std(models.raw, split_ds.test, split_ds.validation).keys()
        if k not in ["validation_confusion_matrix", "test_confusion_matrix"]
        ])

    for model in fields(models):

        if model.name not in d.keys(): continue

        ds_test = split_ds.test
        ds_validation = split_ds.validation

        res = _std(getattr(models, model.name), ds_validation, ds_test)
        
        d[model.name].extend([
            res[k] for k in res.keys() 
            if k not in ["validation_confusion_matrix", "test_confusion_matrix"]
            ])

        c["dataset"].append(model.name)
        c["validation_confusion_matrix"].append(res["validation_confusion_matrix"])
        c["test_confusion_matrix"].append(res["test_confusion_matrix"])

    d = DataFrame(d)

    with open(PATH_ROOT/"results"/"tables"/"evaluation.md", "a") as file:
        file.write("\n\nSTANDARD METRICS\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        for i in range(len(c["dataset"])):
            file.write(f"\n\nVALIDATION CONFUSION MATRIX {c["dataset"][i].upper()}\n\n")
            c["validation_confusion_matrix"][i].to_markdown(file)
            file.write("\n\n\n")
            file.write("_"*100)
            file.write(f"\n\nTEST CONFUSION MATRIX {c["dataset"][i].upper()}\n\n")
            c["test_confusion_matrix"][i].to_markdown(file)
            file.write("\n\n\n")
            file.write("_"*100)

    return d
