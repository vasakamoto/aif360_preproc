

from dataclasses import fields

from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier

from src.configs import (
        PATH_ROOT,
        SplitDataset,
        TrainedModels,
        PRIVILEGED_GROUP,
        UNPRIVILEGED_GROUP
        )


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
            "statistical_parity_difference": round(cm.statistical_parity_difference(), 3),
            "disparate_impact": round(cm.disparate_impact(), 3),
            "equal_opportunity_difference": round(cm.equal_opportunity_difference(), 3),
            "average_odds_difference": round(cm.average_odds_difference(), 3),
            "false_positive_rate_diff": round(cm.false_positive_rate_difference(), 3),
            "false_discovery_rate_diff": round(cm.false_discovery_rate_difference(), 3),
            }


def fair_metrics(models : TrainedModels, split_ds : SplitDataset) -> DataFrame:

    d = {
            "dataset" : [],
            "statistical_parity_difference": [],
            "disparate_impact": [],
            "equal_opportunity_difference": [],
            "average_odds_difference": [],
            "false_positive_rate_diff": [],
            "false_discovery_rate_diff": [],
            }

    for model in fields(models):
        ds_test = split_ds.test
        ds_validation = split_ds.validation

        res_test = _fairness_metrics(getattr(models, model.name), ds_test)
        res_test.update({"dataset" : f"{model.name}_test"})
        res_validation = _fairness_metrics(getattr(models, model.name), ds_validation)
        res_validation.update({"dataset" : f"{model.name}_validation"})

        [d[c].append(res_test[c]) for c in res_test.keys()]
        [d[c].append(res_validation[c]) for c in res_validation.keys()]

    d = DataFrame(d)

    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"fairness_metrics", "w") as file:
        file.write("FAIRNESS METRICS\n\n")
        d.to_markdown(file)

    return d
