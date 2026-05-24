
from src.configs import PATH_ROOT

from matplotlib import pyplot as plt
from numpy import nan
from pandas import (
        DataFrame,
        Series,
        cut
        )


def _distribution(s : Series) -> DataFrame:

    frequency = DataFrame()
    nnull = s.isna().sum()
    buffer = {
            "abs_frequency" : nnull,
            "rel_frequency" : round(nnull / s.size, 4) * 100
            }

    if s.dtype == "Int64":
        frequency = DataFrame(index=s.value_counts().index)
        frequency["abs_frequency"] = s.value_counts().values
        frequency["rel_frequency"] = round(frequency["abs_frequency"] / s.size, 4) * 100

    ### CATEGORIZE CONTINOUS VARIABLES
    if s.dtype == "float64":
        ul = float(s.max());
        bl = float(s.min());
        skip = abs((ul - bl) / 8)
        bins = [round((x*skip) + bl, 2) for x in range(0, 9)]
        labels = [f"{round((x*skip) + bl, 2)} - {round(((x + 1)*skip) + bl, 2)}" for x in range(0, 8)]
        categ = cut(s, bins=bins, labels=labels)
        frequency = DataFrame(index=categ.value_counts().index)
        frequency["abs_frequency"] = categ.value_counts().values
        frequency["rel_frequency"] = round(frequency["abs_frequency"] / categ.size, 4) * 100

    frequency.loc[nan] = buffer["abs_frequency"], buffer["rel_frequency"]

    return frequency


def _histogram(s : Series) -> None:

    s.sort_index().plot(kind="bar", width=1.0, edgecolor="black")
    plt.xlabel(f"{s.index.name}")
    plt.tight_layout()
    plt.savefig(PATH_ROOT/"results"/"charts"/"univariate"/f"hist_{s.index.name}")
    plt.close()


def univariate_analysis(df : DataFrame) -> None:

    (PATH_ROOT/"results"/"tables"/"univariate.md").unlink(missing_ok=True)

    for c in df.columns:
        with open(PATH_ROOT/"results"/"tables"/"univariate.md", "a") as file:
            measures = {
            "average" : df[c].mean(),
            "median" : df[c].median(),
            "mode" : df[c].mode(),
            "variance" : df[c].var(),
            "amplitude" : df[c].max() - df[c].min()
            }
            s = _distribution(df[c]).sort_index()
            _histogram(s["abs_frequency"])
            file.write(f"\n\n{c}\n\n")
            s.to_markdown(file)
            file.write("\n")
            for k, v in measures.items():
                file.write(f"\n{k} = {v}")
            file.write("\n\n")
            file.write("_"*100)
        
    return
