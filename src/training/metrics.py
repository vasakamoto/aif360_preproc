
from src.configs import (
        UNPRIVILEGED_GROUP,
        PRIVILEGED_GROUP,
        SplitDataset
        )

from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric


def _preprocess_metrics(split_ds : SplitDataset) -> None:
# [ ] STATISTICAL PARITY DIFFERENCE (BEFORE VS. AFTER)
# [ ] DISPARATE IMPACT (BEFORE VS. AFTER)
# [ ] INTERSECTIONAL SUBGROUP SP/DI (To detect compounded bias)
# [ ] DISTORTION MEASURES (Wasserstein Distance / L2 Norm)
# [ ] ATTRIBUTE-TARGET MUTUAL INFORMATION (Retention of predictive signal)

    raw_metrics = BinaryLabelDatasetMetric(
            split_ds.train,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )
    rwg_metrics = BinaryLabelDatasetMetric(
            split_ds.processed_train.reweighing.transformed,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )
    dir_metrics = BinaryLabelDatasetMetric(
            split_ds.processed_train.disparate_impact_remover.transformed,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )
    lfr_metrics = BinaryLabelDatasetMetric(
            split_ds.processed_train.learning_fair_representations.transformed,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )


    return
















def _standard_metrics(ds : BinaryLabelDataset) -> dict[str, float]:

    metrics = BinaryLabelDatasetMetric(
            ds,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )

    return {
            "disparate_impact" : round(metrics.disparate_impact(), 3),
            "statistical_parity_difference" : round(metrics.statistical_parity_difference(), 3),
            }









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
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, precision_recall_curve, auc

OUTPUT_DIR = Path("charts")

_METRIC_LABELS = {
    "accuracy": "Acurácia",
    "precision": "Precisão",
    "recall": "Sensibilidade",
    "f1": "F1-Score",
    "roc_auc": "ROC-AUC",
}

_SPLIT_LABELS = {
    "test": "Teste",
    "validation": "Validação",
}


def _setup():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.size": 10,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
    })


def _save(fig, name: str):
    OUTPUT_DIR.mkdir(exist_ok=True)
    fig.savefig(OUTPUT_DIR / f"{name}.png", bbox_inches="tight")
    plt.close(fig)


def _method_colors(methods: list) -> dict:
    colors = plt.cm.tab10.colors
    return {m: colors[i % len(colors)] for i, m in enumerate(methods)}


# ---------------------------------------------------------------------------
#  Public API
# ---------------------------------------------------------------------------

def standard_metrics(all_results: dict, split: str = "test") -> None:
    _setup()
    methods = list(all_results.keys())
    colors = _method_colors(methods)
    metric_keys = list(_METRIC_LABELS.keys())
    labels = [_METRIC_LABELS[m] for m in metric_keys]

    x = np.arange(len(metric_keys))
    width = 0.8 / len(methods)

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, method in enumerate(methods):
        vals = [all_results[method]["standard_metrics"][split].get(m, 0) for m in metric_keys]
        offset = (i - len(methods) / 2 + 0.5) * width
        bars = ax.bar(x + offset, vals, width, label=method, color=colors[method])
        ax.bar_label(bars, fmt="%.3f", fontsize=7, rotation=90, padding=3)

    ax.set_ylabel("Valor")
    ax.set_title(f"Métricas de Classificação — {_SPLIT_LABELS.get(split, split)}")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.18)
    ax.legend(loc="lower right", fontsize=8)

    _save(fig, f"standard_metrics_{split}")


def fairness_metrics(all_results: dict) -> None:
    _setup()
    methods = list(all_results.keys())
    colors = _method_colors(methods)

    diff_keys = [
        "Mean Difference",
        "Statistical Parity Difference",
        "Equal Opportunity Difference",
        "Average Odds Difference",
        "True Positive Rate Diff",
        "False Positive Rate Diff",
    ]

    x = np.arange(len(diff_keys))
    width = 0.8 / len(methods)

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(18, 7), gridspec_kw={"width_ratios": [3, 1]},
    )

    for i, method in enumerate(methods):
        vals = [all_results[method]["fairness_metrics"].get(m, 0) for m in diff_keys]
        offset = (i - len(methods) / 2 + 0.5) * width
        ax1.bar(x + offset, vals, width, label=method, color=colors[method])

    ax1.axhline(y=0, color="black", linestyle="--", linewidth=0.8, alpha=0.5)
    ax1.set_ylabel("Diferença")
    ax1.set_title("Métricas de Equidade — Diferenças (ideal = 0)")
    ax1.set_xticks(x)
    ax1.set_xticklabels([k.replace(" ", "\n") for k in diff_keys], fontsize=8)
    ax1.legend(fontsize=8)

    di_vals = [all_results[m]["fairness_metrics"]["Disparate Impact"] for m in methods]
    bars = ax2.bar(methods, di_vals, color=[colors[m] for m in methods])
    ax2.bar_label(bars, fmt="%.3f", fontsize=8)
    ax2.axhline(y=1, color="black", linestyle="--", linewidth=0.8, alpha=0.5)
    ax2.set_ylabel("Razão")
    ax2.set_title("Disparate Impact (ideal = 1)")
    ax2.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    _save(fig, "fairness_metrics")


def confusion_matrices(all_results: dict, split: str = "test") -> None:
    _setup()
    methods = list(all_results.keys())
    n = len(methods)
    cols = min(n, 3)
    rows = (n + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4.5 * rows))
    axes = np.array(axes).flatten()

    cell_labels = [["TN", "FP"], ["FN", "TP"]]

    for i, method in enumerate(methods):
        cm = all_results[method]["standard_metrics"][split]["confusion_matrix"]
        ax = axes[i]
        im = ax.imshow(cm, cmap="Blues", interpolation="nearest")

        thresh = cm.max() / 2
        for r in range(cm.shape[0]):
            for c in range(cm.shape[1]):
                ax.text(
                    c, r, f"{cell_labels[r][c]}\n{cm[r, c]}",
                    ha="center", va="center",
                    color="white" if cm[r, c] > thresh else "black",
                    fontsize=11, fontweight="bold",
                )

        ax.set_xlabel("Predito")
        ax.set_ylabel("Real")
        ax.set_title(method)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xticklabels(["Negativo", "Positivo"])
        ax.set_yticklabels(["Negativo", "Positivo"])
        fig.colorbar(im, ax=ax, fraction=0.046)

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle(
        f"Matrizes de Confusão — {_SPLIT_LABELS.get(split, split)}", fontsize=14,
    )
    fig.tight_layout()
    _save(fig, f"confusion_matrices_{split}")


def roc_curves(models_data: dict, split: str = "test") -> None:
    _setup()
    methods = list(models_data.keys())
    colors = _method_colors(methods)

    fig, ax = plt.subplots(figsize=(8, 7))

    for name, md in models_data.items():
        model, ds = md["model"], md["data"][split]
        y_true = ds.labels.ravel()
        y_prob = model.predict_proba(ds.features)[:, 1]
        fpr, tpr, _ = roc_curve(y_true, y_prob)
        roc_auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.3f})", color=colors[name])

    ax.plot([0, 1], [0, 1], "k--", alpha=0.4, label="Aleatório (AUC = 0.500)")
    ax.set_xlabel("Taxa de Falsos Positivos (FPR)")
    ax.set_ylabel("Taxa de Verdadeiros Positivos (TPR)")
    ax.set_title(f"Curvas ROC — {_SPLIT_LABELS.get(split, split)}")
    ax.legend(loc="lower right", fontsize=9)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1.05])

    _save(fig, f"roc_curves_{split}")


def pr_curves(models_data: dict, split: str = "test") -> None:
    _setup()
    methods = list(models_data.keys())
    colors = _method_colors(methods)

    fig, ax = plt.subplots(figsize=(8, 7))

    for name, md in models_data.items():
        model, ds = md["model"], md["data"][split]
        y_true = ds.labels.ravel()
        y_prob = model.predict_proba(ds.features)[:, 1]
        prec, rec, _ = precision_recall_curve(y_true, y_prob)
        ap = auc(rec, prec)
        ax.plot(rec, prec, label=f"{name} (AP = {ap:.3f})", color=colors[name])

    ax.set_xlabel("Recall (Sensibilidade)")
    ax.set_ylabel("Precisão")
    ax.set_title(f"Curvas Precisão–Recall — {_SPLIT_LABELS.get(split, split)}")
    ax.legend(loc="lower left", fontsize=9)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1.05])

    _save(fig, f"pr_curves_{split}")


def tradeoff(all_results: dict, split: str = "test") -> None:
    _setup()
    methods = list(all_results.keys())
    colors = _method_colors(methods)

    fig, ax = plt.subplots(figsize=(9, 7))

    for name in methods:
        r = all_results[name]
        f1 = r["standard_metrics"][split]["f1"]
        spd = abs(r["fairness_metrics"]["Statistical Parity Difference"])
        ax.scatter(spd, f1, s=140, color=colors[name], zorder=5, edgecolors="black")
        ax.annotate(
            name, (spd, f1),
            textcoords="offset points", xytext=(10, 8), fontsize=9,
        )

    ax.set_xlabel("|Statistical Parity Difference|  (menor → mais justo)")
    ax.set_ylabel("F1-Score  (maior → melhor)")
    ax.set_title(f"Trade-off: Desempenho vs Equidade — {_SPLIT_LABELS.get(split, split)}")
    ax.axvline(x=0, color="green", linestyle="--", alpha=0.3)

    _save(fig, f"tradeoff_{split}")


def generate_all(all_results: dict, models_data: dict) -> None:
    for split in ("test", "validation"):
        standard_metrics(all_results, split)
        confusion_matrices(all_results, split)
        roc_curves(models_data, split)
        pr_curves(models_data, split)
        tradeoff(all_results, split)
    fairness_metrics(all_results)
    print(f"Gráficos salvos em: {OUTPUT_DIR.resolve()}")
