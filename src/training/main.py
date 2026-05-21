

from pandas import DataFrame

from src.training import (
        src_dataset,
        preprocess,
        train
        )

def execute(df : DataFrame) -> dict:

    split_ds = src_dataset.src_dataset(df)
    grouped_ds = preprocess.process(split_ds, [])
    models = train.train(split_ds, grouped_ds)

    return {
            "split_ds" : split_ds,
            "grouped_ds" : grouped_ds,
            "models" : models
            }

