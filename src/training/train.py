

from src.configs import GroupedProcessedDatasets, SplitDataset, TrainedModels

from aif360.datasets import BinaryLabelDataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV


def _rf(ds: BinaryLabelDataset, use_weights: bool=True) -> RandomForestClassifier:
    X = ds.features
    y = ds.labels.ravel()
    model = RandomForestClassifier(
            n_estimators=100,
            min_samples_split=2,
            min_samples_leaf=2,
            max_features="sqrt",
            max_depth=5,
            random_state=42,
            )

    if use_weights:
        w = ds.instance_weights
        model.fit(X, y, sample_weight=w)
    else:
        model.fit(X, y)
        # param_dist = {
        #     'n_estimators': [100, 200, 500],
        #     'max_depth': [5, 10, 20, None],
        #     'min_samples_split': [2, 5, 10],
        #     'min_samples_leaf': [1, 2, 4],
        #     'max_features': ['sqrt', 'log2', 0.5]
        # }

        # random_search = RandomizedSearchCV(
        #     estimator=model, 
        #     param_distributions=param_dist, 
        #     n_iter=20,          # Testa 20 combinações aleatórias
        #     cv=5,               # Estratégia K-Fold
        #     scoring='accuracy', # Métrica de otimização
        #     random_state=42,
        #     n_jobs=-1
        # )
        # random_search.fit(X, y)
        # print("Melhores parâmetros encontrados:", random_search.best_params_)

    return model


def train(raw : SplitDataset, grouped_ds : GroupedProcessedDatasets) -> TrainedModels:

    return TrainedModels(
            raw=_rf(raw.train, False),
            reweighing=_rf(grouped_ds.reweighing.transformed_train),
            disparate_impact_remover=_rf(grouped_ds.disparate_impact_remover.transformed_train),
            learning_fair_representations=_rf(grouped_ds.learning_fair_representations.transformed_train),
            )
