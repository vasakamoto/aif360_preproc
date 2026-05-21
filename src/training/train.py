
from aif360.datasets import BinaryLabelDataset
from numpy import False_
from sklearn.ensemble import RandomForestClassifier

from src.configs import GroupedProcessedDatasets, SplitDataset, TrainedModels


def _rf(ds: BinaryLabelDataset, use_weights: bool) -> RandomForestClassifier:
    X = ds.features
    y = ds.labels.ravel()

    if use_weights:
        w = ds.instance_weights
        model = RandomForestClassifier(
                min_samples_leaf=5,
                n_estimators=200,
                random_state=42,
                )
        model.fit(X, y, sample_weight=w)
    else:
        model = RandomForestClassifier(
                min_samples_leaf=5,
                n_estimators=200,
                random_state=42,
                )
        model.fit(X, y)

    return model


def train(raw : SplitDataset, grouped_ds : GroupedProcessedDatasets) -> TrainedModels:

    return TrainedModels(
            raw=_rf(raw.train, False),
            reweighing=_rf(grouped_ds.reweighing.transformed_train, True),
            disparate_impact_remover=_rf(grouped_ds.disparate_impact_remover.transformed_train, True),
            learning_fair_representations=_rf(grouped_ds.learning_fair_representations.transformed_train, True),
            )
