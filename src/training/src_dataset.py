
from src.configs import (
        PROTECTED_ATTRIBUTES,
        TARGET,
        FAVORABLE_OUTCOME,
        SplitDataset
        )

from aif360.datasets import BinaryLabelDataset
from pandas import DataFrame
from sklearn.model_selection import train_test_split


def src_dataset(df : DataFrame) -> SplitDataset:

    df = df.dropna()
    df_train, df_test = train_test_split(df, test_size=0.4, random_state=42)
    df_valid, df_test = train_test_split(df_test, test_size=0.5, random_state=42)

    return SplitDataset(
            BinaryLabelDataset(
                df=df_train,
                label_names=[TARGET],
                favorable_label=FAVORABLE_OUTCOME,
                protected_attribute_names=PROTECTED_ATTRIBUTES
                ),
            BinaryLabelDataset(
                df=df_test,
                label_names=[TARGET],
                favorable_label=FAVORABLE_OUTCOME,
                protected_attribute_names=PROTECTED_ATTRIBUTES
                ),
            BinaryLabelDataset(
                df=df_valid,
                label_names=[TARGET],
                favorable_label=FAVORABLE_OUTCOME,
                protected_attribute_names=PROTECTED_ATTRIBUTES
                ),
            )
