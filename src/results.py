
from aif360.datasets import StandardDataset, BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from pandas import DataFrame, Series
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
    roc_auc_score,
    confusion_matrix
)

from .configs import (
    TARGET,
    FAVORABLE_OUTCOME,
    PROTECTED_ATTRIBUTES,
    PRIVILEGED_GROUP,
    UNPRIVILEGED_GROUP
)


def _rf_metrics(**kwargs) -> dict:
    model = kwargs["model"]
    samples = kwargs["samples"][kwargs["sample"]]

    X_TR, y_tr = [0, 0]
    X_T, y_t = [0, 0]
    X_V, y_v = [0, 0]

    if kwargs["sample"] == "reweighted_samples":
        X_TR, y_tr, w_tr = samples["train"]
        X_T, y_t, w_t = samples["test"]
        X_V, y_v, w_v = samples["validation"]

    else:
        X_TR, y_tr = samples["train"]
        X_T, y_t = samples["test"]
        X_V, y_v = samples["validation"]

    y_prediction = model.predict(X_T)
    y_vprediction = model.predict(X_V)

    y_prediction_p = model.predict_proba(X_T)[:, 1]
    y_vprediction_p = model.predict_proba(X_V)[:, 1]

    # test
    acc_t = accuracy_score(y_t, y_prediction)
    prec_t = precision_score(y_t, y_prediction, pos_label=1)
    recall_t = recall_score(y_t, y_prediction, pos_label=1)
    f1_t = f1_score(y_t, y_prediction, pos_label=1)
    roc_auc_t = roc_auc_score(y_t, y_prediction_p)
    cm_t = confusion_matrix(y_t, y_prediction)

    # validation
    acc_v = accuracy_score(y_v, y_vprediction)
    prec_v = precision_score(y_v, y_vprediction, pos_label=1)
    recall_v = recall_score(y_v, y_vprediction, pos_label=1)
    f1_v = f1_score(y_v, y_vprediction, pos_label=1)
    roc_auc_v = roc_auc_score(y_v, y_vprediction_p)
    cm_v = confusion_matrix(y_v, y_vprediction)

    return {
        "train" : {
            "baseline_accuracy" : round(model.score(X_TR, y_tr), 3),
        },
        "test" : {
            "baseline_accuracy" : round(model.score(X_T, y_t), 3),
            "accuracy" : round(acc_t, 3),
            "precision" : round(prec_t, 3),
            "recall" : round(recall_t, 3),
            "f1" : round(f1_t, 3),
            "roc_auc_t" : round(roc_auc_t, 3),
            "confunsion_matrix" : cm_t,
        },
        "validation" : {
            "baseline_accuracy" : round(model.score(X_V, y_v), 3),
            "accuracy" : round(acc_v, 3),
            "precision" : round(prec_v, 3),
            "recall" : round(recall_v, 3),
            "f1" : round(f1_v, 3),
            "roc_auc_t" : round(roc_auc_v, 3),
            "confunsion_matrix" : cm_v,
        },
    }


def _rf_f_metrics(**kwargs) -> dict:
    model = kwargs["model"]
    odf = kwargs["odf"]

    if isinstance(odf, BinaryLabelDataset):
        
        y_biased = model.predict(odf.features)

        bdf = odf.copy(deepcopy=True)
        bdf.labels = y_biased

        fair_metrics = ClassificationMetric(
            odf,
            bdf,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
        )

        return {
            "Mean Difference" : round(fair_metrics.mean_difference(), 3),
            "Statistical Parity Difference" : round(fair_metrics.statistical_parity_difference(), 3),
            "Disparate Impact" : round(fair_metrics.disparate_impact(), 3),
            "Equal Opportunity Difference" : round(fair_metrics.equal_opportunity_difference(), 3),
            "Average Odds Difference" : round(fair_metrics.average_odds_difference(), 3),
            "True Positive Rate" : round(fair_metrics.difference(fair_metrics.true_positive_rate), 3),
            "False Positive Rate" : round(fair_metrics.difference(fair_metrics.false_positive_rate), 3),
        }
        

    ds = StandardDataset(
        odf,
        label_name=TARGET,
        favorable_classes=FAVORABLE_OUTCOME,
        protected_attribute_names=PROTECTED_ATTRIBUTES,
        privileged_classes=[[p["race"] for p in PRIVILEGED_GROUP]],
    )

    c = odf.columns.tolist() 
    c.remove(TARGET)
    X = odf[c]

    y_biased = model.predict(X)

    bdf = ds.copy(deepcopy=True)
    bdf.labels = y_biased

    fair_metrics = ClassificationMetric(
        ds,
        bdf,
        unprivileged_groups=UNPRIVILEGED_GROUP,
        privileged_groups=PRIVILEGED_GROUP
    )

    return {
        "Mean Difference" : round(fair_metrics.mean_difference(), 3),
        "Statistical Parity Difference" : round(fair_metrics.statistical_parity_difference(), 3),
        "Disparate Impact" : round(fair_metrics.disparate_impact(), 3),
        "Equal Opportunity Difference" : round(fair_metrics.equal_opportunity_difference(), 3),
        "Average Odds Difference" : round(fair_metrics.average_odds_difference(), 3),
        "True Positive Rate" : round(fair_metrics.difference(fair_metrics.true_positive_rate), 3),
        "False Positive Rate" : round(fair_metrics.difference(fair_metrics.false_positive_rate), 3),
    }


def all_metrics(model : RandomForestClassifier, odf : DataFrame, samples : dict, sample : str) -> dict:
    return {
        "standard_metrics" : _rf_metrics(model=model, samples=samples, sample=sample),
        "fairness_metrics" : _rf_f_metrics(model=model, odf=odf),
    }


def print_metrics(d : dict) -> None:
    for k, _ in d.items():
        print("-"*50)
        print(k)
        if k =="standard_metrics":
            for k, _ in _.items():
                print("-"*30)
                print(k)
                for k, v in _.items():
                    print(f"{k}: {v}")
        else:
            for k, v in _.items():
                print(f"{k}: {v}")
