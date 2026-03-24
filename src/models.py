
from aif360.datasets import BinaryLabelDataset
from sklearn.ensemble import RandomForestClassifier


def rf(train_ds: BinaryLabelDataset, use_weights: bool = False) -> RandomForestClassifier:
    X = train_ds.features
    y = train_ds.labels.ravel()

    params = {
        "min_samples_leaf": 5,
        "n_estimators": 200,
        "random_state": 42,
    }

    if use_weights:
        model = RandomForestClassifier(**params)
        model.fit(X, y, sample_weight=train_ds.instance_weights.ravel())
    else:
        model = RandomForestClassifier(class_weight="balanced", **params)
        model.fit(X, y)

    return model
