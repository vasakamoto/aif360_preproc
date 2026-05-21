
from src.configs import (
        PROTECTED_ATTRIBUTES,
        TARGET,
        FAVORABLE_OUTCOME,
        SplitDataset
        )

from aif360.datasets import BinaryLabelDataset
from pandas import (
        DataFrame,
        concat
        )
from sklearn.model_selection import train_test_split
from sklearn.utils import resample


def src_dataset(df : DataFrame) -> SplitDataset:

    df = df.dropna()
    df_major = df[df[TARGET] == FAVORABLE_OUTCOME]
    df_minor = df[df[TARGET] == 0]
    df_major_downsampled = resample(
        df_major, 
        replace=False, 
        n_samples=len(df_minor) * 2,  # Mantém uma proporção saudável de 2 positivos para 1 negativo
        random_state=42
    )
    df = concat([df_major_downsampled, df_minor])
    df_train, df_test = train_test_split(df, test_size=0.4, random_state=42)
    df_valid, df_test = train_test_split(df_test, test_size=0.5, random_state=42)

    return SplitDataset(
            train=BinaryLabelDataset(
                df=df_train,
                label_names=[TARGET],
                favorable_label=FAVORABLE_OUTCOME,
                protected_attribute_names=PROTECTED_ATTRIBUTES
                ),
            test=BinaryLabelDataset(
                df=df_test,
                label_names=[TARGET],
                favorable_label=FAVORABLE_OUTCOME,
                protected_attribute_names=PROTECTED_ATTRIBUTES
                ),
            validation=BinaryLabelDataset(
                df=df_valid,
                label_names=[TARGET],
                favorable_label=FAVORABLE_OUTCOME,
                protected_attribute_names=PROTECTED_ATTRIBUTES
                ),
            )
