
from aif360.datasets import BinaryLabelDataset
from numpy import False_
from sklearn.ensemble import RandomForestClassifier

from src.configs import SplitDataset, TrainedModels


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


def train(split_ds : SplitDataset) -> TrainedModels:

    return TrainedModels(
            raw=_rf(split_ds.train, False),
            reweighing=_rf(split_ds.processed_train.reweighing.transformed, True),
            disparate_impact_remover=_rf(split_ds.processed_train.disparate_impact_remover.transformed, True),
            learning_fair_representations=_rf(split_ds.processed_train.learning_fair_representations.transformed, True),
            )
