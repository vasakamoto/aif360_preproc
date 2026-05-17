
from src.configs import (
        UNPRIVILEGED_GROUP,
        PRIVILEGED_GROUP
        )

from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric


def _spddi(ds : BinaryLabelDataset) -> dict[str, float]:

    metrics = BinaryLabelDatasetMetric(
            ds,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )

    return {
            "disparate_impact" : round(metrics.disparate_impact(), 3),
            "statistical_parity_difference" : round(metrics.statistical_parity_difference(), 3),
            }
