
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
    roc_auc_score,
    confusion_matrix,
)

from .configs import (
    PRIVILEGED_GROUP,
    UNPRIVILEGED_GROUP,
)


def _standard_metrics(model: RandomForestClassifier, data: dict) -> dict:
    X_TR = data["train"].features
    y_tr = data["train"].labels.ravel()
    X_T = data["test"].features
    y_t = data["test"].labels.ravel()
    X_V = data["validation"].features
    y_v = data["validation"].labels.ravel()

    y_pred_t = model.predict(X_T)
    y_pred_v = model.predict(X_V)
    y_prob_t = model.predict_proba(X_T)[:, 1]
    y_prob_v = model.predict_proba(X_V)[:, 1]

    return {
        "train": {
            "baseline_accuracy": round(model.score(X_TR, y_tr), 3),
        },
        "test": {
            "baseline_accuracy": round(model.score(X_T, y_t), 3),
            "accuracy": round(accuracy_score(y_t, y_pred_t), 3),
            "precision": round(precision_score(y_t, y_pred_t, pos_label=1), 3),
            "recall": round(recall_score(y_t, y_pred_t, pos_label=1), 3),
            "f1": round(f1_score(y_t, y_pred_t, pos_label=1), 3),
            "roc_auc": round(roc_auc_score(y_t, y_prob_t), 3),
            "confusion_matrix": confusion_matrix(y_t, y_pred_t),
        },
        "validation": {
            "baseline_accuracy": round(model.score(X_V, y_v), 3),
            "accuracy": round(accuracy_score(y_v, y_pred_v), 3),
            "precision": round(precision_score(y_v, y_pred_v, pos_label=1), 3),
            "recall": round(recall_score(y_v, y_pred_v, pos_label=1), 3),
            "f1": round(f1_score(y_v, y_pred_v, pos_label=1), 3),
            "roc_auc": round(roc_auc_score(y_v, y_prob_v), 3),
            "confusion_matrix": confusion_matrix(y_v, y_pred_v),
        },
    }


def _fairness_metrics(model: RandomForestClassifier, dataset: BinaryLabelDataset) -> dict:
    y_pred = model.predict(dataset.features)

    pred_ds = dataset.copy(deepcopy=True)
    pred_ds.labels = y_pred.reshape(-1, 1)

    cm = ClassificationMetric(
        dataset,
        pred_ds,
        unprivileged_groups=UNPRIVILEGED_GROUP,
        privileged_groups=PRIVILEGED_GROUP,
    )

    return {
        "Mean Difference": round(cm.mean_difference(), 3),
        "Statistical Parity Difference": round(cm.statistical_parity_difference(), 3),
        "Disparate Impact": round(cm.disparate_impact(), 3),
        "Equal Opportunity Difference": round(cm.equal_opportunity_difference(), 3),
        "Average Odds Difference": round(cm.average_odds_difference(), 3),
        "True Positive Rate Diff": round(cm.difference(cm.true_positive_rate), 3),
        "False Positive Rate Diff": round(cm.difference(cm.false_positive_rate), 3),
    }


def all_metrics(model: RandomForestClassifier, data: dict) -> dict:
    return {
        "standard_metrics": _standard_metrics(model, data),
        "fairness_metrics": _fairness_metrics(model, data["test"]),
    }


def print_metrics(d: dict) -> None:
    for section, content in d.items():
        print("-" * 50)
        print(section)
        if section == "standard_metrics":
            for split, metrics in content.items():
                print("-" * 30)
                print(split)
                for name, val in metrics.items():
                    print(f"  {name}: {val}")
        else:
            for name, val in content.items():
                print(f"  {name}: {val}")
