

from pandas import DataFrame

from src.training import (
        src_dataset,
        preprocess,
        metrics
        )

def execute(df : DataFrame) -> None:

    split_ds = src_dataset.src_dataset(df)
    preprocess.preprocess(split_ds)

    print(split_ds.test.reweighing)
