
from src.configs import PATH_ROOT

from pandas import DataFrame, Series

# TYPES
# CATEGORIZATION (NOMINAL, ORDINAL, DISCRETE, CONTINUOUS)
# NULL


def inspection_analysis(df : DataFrame) -> None:
    with open(PATH_ROOT/"results"/"tables"/"inspection.md", "w") as file:
        for c in df.columns.sort_values():
            file.write(f"\n\nCOLUMN : {c}")
            file.write(f"\n\nTYPE : {df[c].dtype}")
            file.write(f"\n\nNULL PERCENTAGE : {round(df[c].isna().sum() / df[c].shape[0], 4)*100}")
            file.write("\n\n")
            df[c].value_counts().to_markdown(file, mode="a")
            file.write("\n\n")
            file.write("_"*40)
