
from dataclasses import fields

from aif360.datasets import BinaryLabelDataset
from numpy import mean
from pandas import DataFrame
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


def _std(model : RandomForestClassifier, ds_training : BinaryLabelDataset,
         ds_validation : BinaryLabelDataset, ds_test : BinaryLabelDataset) -> dict:

    X_training = ds_training.features
    X_test = ds_test.features
    X_validation = ds_validation.features

    y_training = ds_training.labels.ravel()
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
            "test_confusion_matrix" : confusion_matrix(y_test, y_pred_test),
            "validation_baseline_accuracy" : round(max(mean(y_validation == 1), mean(y_validation == 0)), 3),
            "validation_accuracy" : round(accuracy_score(y_validation, y_pred_validation), 3),
            "validation_precision" : round(precision_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_recall" : round(recall_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_f1" : round(f1_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_roc_auc" : round(roc_auc_score(y_validation, y_prob_validation), 3),
            "validation_confusion_matrix" : confusion_matrix(y_validation, y_pred_validation),
            }


def std_metrics(models : TrainedModels, grouped_ds : GroupedProcessedDatasets,
            split_ds : SplitDataset) -> DataFrame:

    d = {
            "dataset" : [],
            "test_baseline_accuracy" : [],
            "test_accuracy" : [],
            "test_precision" : [],
            "test_recall" : [],
            "test_f1" : [],
            "test_roc_auc" : [],
            #"test_confusion_matrix" : [],
            "validation_baseline_accuracy" : [],
            "validation_accuracy" : [],
            "validation_precision" : [],
            "validation_recall" : [],
            "validation_f1" : [],
            "validation_roc_auc" : [],
            #"validation_confusion_matrix" : [],
            }

    for model in fields(models):
        d["dataset"].append(model.name)
        ds_test = split_ds.test
        ds_validation = split_ds.validation

        if model.name == "raw":
            ds_training = split_ds.train
        elif model.name == "disparate_impact_remover" or model.name == "learning_fair_representations":
            ds_training = getattr(grouped_ds, model.name).transformed_train 
        elif model.name == "reweighing": 
            ds_training = grouped_ds.reweighing.transformed_train
        else:
            raise Exception("UNEXPECTED MODEL")

        res = _std(getattr(models, model.name), ds_training, ds_validation, ds_test)

        d["test_baseline_accuracy"].append(res["test_baseline_accuracy"])
        d["test_accuracy"].append(res["test_accuracy"])
        d["test_precision"].append(res["test_precision"])
        d["test_recall"].append(res["test_recall"])
        d["test_f1"].append(res["test_f1"])
        d["test_roc_auc"].append(res["test_roc_auc"])
        #d["test_confusion_matrix"].append(res["test_confusion_matrix"])
        d["validation_baseline_accuracy"].append(res["validation_baseline_accuracy"])
        d["validation_accuracy"].append(res["validation_accuracy"])
        d["validation_precision"].append(res["validation_precision"])
        d["validation_recall"].append(res["validation_recall"])
        d["validation_f1"].append(res["validation_f1"])
        d["validation_roc_auc"].append(res["validation_roc_auc"])
        #d["validation_confusion_matrix"].append(res["validation_confusion_matrix"])

    d = DataFrame(d)

    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"standard_metrics", "w") as file:
        file.write("STANDARD METRICS\n\n")
        d.to_markdown(file)

    return d
