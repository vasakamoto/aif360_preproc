

from pandas import DataFrame, Series

# TYPES
# CATEGORIZATION (NOMINAL, ORDINAL, DISCRETE, CONTINUOUS)
# NULL


def inspection_analysis(df : DataFrame) -> None:
    for c in df.columns.sort_values():
        print(f"COLUMN : {c}")
        print(f"TYPE : {df[c].dtype}")
        print(f"NULL PERCENTAGE : {round(df[c].isna().sum() / df[c].shape[0], 4)*100}")
        print(df[c].value_counts())
        print("_"*40)
