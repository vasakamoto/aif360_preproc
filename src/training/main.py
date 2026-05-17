

from pandas import DataFrame

from src.training import (
        src_dataset,
        preprocess,
        metrics,
        train
        )

def execute(df : DataFrame) -> None:

    split_ds = src_dataset.src_dataset(df)
    preprocess.preprocess(split_ds)
    models = train.train(split_ds)

    print(models.raw.score(split_ds.train.features, split_ds.train.labels.ravel()))

