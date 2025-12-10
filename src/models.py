

from sklearn.ensemble import RandomForestClassifier


def rf(samples : dict, sample : str) -> RandomForestClassifier:

    if sample == "original_samples":
        model = RandomForestClassifier(
            class_weight="balanced", min_samples_leaf=5, n_estimators=200, random_state=42
        )

        X, y = samples[sample]["train"]

        model.fit(X, y)
        return model

    X, y, w = samples[sample]["train"]

    model = RandomForestClassifier(
        min_samples_leaf=5, n_estimators=200, random_state=42
    )


    model.fit(X, y, sample_weight=w)
    return model
