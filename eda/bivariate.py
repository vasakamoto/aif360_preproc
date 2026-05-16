
from math import factorial

from src.configs import PATH_ROOT

from matplotlib import pyplot as plt
from numpy import (
        sqrt,
        average,
        nan
        )
from pandas import (
        DataFrame,
        Series,
        crosstab,
        qcut
        )
from scipy.stats import (
        chi2_contingency,
        ttest_ind,
        mannwhitneyu,
        kruskal,
        pointbiserialr
        )
import seaborn as sns


## quali x quali
# [x] contingency tables (frequencies discriminated by another category)
# [x] stacked bars 
# [x] chi-square test
# [x] coeficient v (cramér)
# 
## quanti x quali
# [x] violin plot
#   - grouped boxplots
#   - overlaid KDE or histogram
# [x] t test or mann-whitney U
# [x] kruskal-wallis
# 
## quanti x quanti
# [x] scatter plot
# [x] pearson/spearman correlation matrix
# [x] heatmaps
#
# bias metrics / target var metrics
## quali
# [x] disparate impact
# [x] statistical parity difference
## quanti
# [x] point-biserial correlation

# QUALI X QUALI
def _contingency_table(df : DataFrame) -> DataFrame:

    size = len(df)
    columns = df.columns.tolist()
    frequency = DataFrame(index=df.value_counts(dropna=False).index)
    frequency["abs_frequency"] = df.value_counts(dropna=False).values
    frequency["rel_frequency_tot"] = round(frequency["abs_frequency"] / size, 4) * 100
    frequency[f"rel_f_{columns[0]}_by_{columns[1]}"] = ( 
                                     frequency["abs_frequency"] / 
                                     frequency.groupby(level=columns[0])["abs_frequency"].transform("sum")
                                     ) * 100
    frequency[f"rel_f_{columns[1]}_by_{columns[0]}"] = ( 
                                     frequency["abs_frequency"] / 
                                     frequency.groupby(level=columns[1])["abs_frequency"].transform("sum")
                                     ) * 100

    frequency.sort_index(inplace=True)
    with open(PATH_ROOT/"tables"/f"bi_{"_".join(columns)}", "w") as file:
        frequency.to_markdown(file)
        file.write("\n\n       \n\n")

    return frequency


def _stacked_bar(df : DataFrame, index : str, variable : str) -> None:

    plot = df[f"rel_f_{index}_by_{variable}"].unstack(level=variable)
    plot.plot(kind="bar", stacked=True)
    plt.tight_layout()
    plt.savefig(PATH_ROOT/"img"/f"bi_stacked_{index}_{variable}")
    plt.close()


def _chi_square_test(df : DataFrame, var1 : str, var2 : str) -> dict:

    matrix = df[[var1, var2]].dropna().value_counts()
    matrix = matrix.unstack(fill_value=0) 

    idxs = matrix.index
    columns = matrix.columns

    chit = chi2_contingency(matrix.values)

    chit_matrix = DataFrame(
            chit[3], index=idxs, columns=[f"expected_{c}" for c in columns]
            ).astype("int64")
    matrix = matrix.join(chit_matrix)

    for c in columns:
        matrix[f"delta_{c}"] = matrix[c] - matrix[f"expected_{c}"]

    with open(PATH_ROOT/"tables"/f"bi_{var1}_{var2}", "a") as file:
        matrix.to_markdown(file)
        file.write("\n\n\n")
        file.write(f"\nChi squared: {chit[0]:.4f}\n")
        file.write(f"\nP-value: {chit[1]:.4f}\n")
        file.write(f"\nDegrees of Freedom: {chit[2]}\n")

    return {
            "matrix" : matrix,
            "chi2" : chit[0],
            "p_value" : chit[1],
            "degree_freedon" : chit[2],
            }


def _coefficient_v(df : DataFrame, categ_feats : list) -> DataFrame:

    d = { c : [] for c in categ_feats }
    d.update({"label" : []})

    for c in categ_feats:
        d["label"].append(c)
        for l in categ_feats:
            confusion_matrix = crosstab(df[c], df[l])
            chi2 = chi2_contingency(confusion_matrix)[0]
            n = confusion_matrix.sum().sum()
            phi2 = chi2 / n
            r, k = confusion_matrix.shape
            phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
            rcorr = r - ((r-1)**2)/(n-1)
            kcorr = k - ((k-1)**2)/(n-1)
            v = sqrt(phi2corr / min((kcorr-1), (rcorr-1)))
            d[l].append(v)

    d = DataFrame(d, index=d["label"]).drop(columns=["label"])
    with open(PATH_ROOT/"tables"/"bi_tests_cramer", "w") as file:
        file.write("CRAMER TEST - COEFFICIENT V\n\n")
        d.to_markdown(file)

    return d


# QUANTI X QUALI
def _violin_plot(df : DataFrame, quanti : str, quali : str) -> None:

    sns.violinplot(
        data=df[[quanti, quali]], 
        x=quali,
        y=quanti,
        inner='quartile',
        palette='muted',
        cut=0
    )

    plt.title(f'{quanti} X {quali}')
    plt.xlabel(quali)
    plt.ylabel(quanti)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(PATH_ROOT/"img"/f"bi_violin_{quali}_{quanti}")
    plt.close()


def _student_mannwhitneyu_test(df : DataFrame, quant : str, quali : str) -> DataFrame:

    d = {
            "group_a" : [],
            "group_b" : [],
            "t_test" : [],
            "t_test_p_value" : [],
            "mann_whitney" : [],
            "mann_whitney_p_value" : [],
            }
    groups = df[quali].dropna().unique().tolist()
    n = len(groups)
    combinations = factorial(n) / (factorial(n - 2) * 2)
    groups.sort()

    while len(groups) > 1:
        s1 = df[df[quali] == groups[0]][quant].dropna()
        for i in range(1, len(groups)):
            s2 = df[df[quali] == groups[i]][quant].dropna()
            t, pt = ttest_ind(s1, s2, nan_policy="omit")
            mw, pmw = mannwhitneyu(s1, s2)
            d["group_a"].append(groups[0])
            d["group_b"].append(groups[i])
            d["t_test"].append(t)
            d["t_test_p_value"].append(pt/combinations)
            d["mann_whitney"].append(mw)
            d["mann_whitney_p_value"].append(pmw)
        groups.pop(0)

    d = DataFrame(d)

    with open(PATH_ROOT/"tables"/f"bi_tests_{quant}_{quali}", "w") as file:
        file.write("STUDENT'S T AND MANN-WHITNEY U TEST\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")

    return d.loc[(d["t_test_p_value"] < 0.05) & (d["mann_whitney_p_value"] < 0.05)].sort_values("group_a")


def _kruskal_wallis(df : DataFrame, quali : list[str], quanti : list[str]) -> DataFrame:

    d = { f"p_{c}" : [] for c in quali }
    d.update({ f"s_{c}" : [] for c in quali })
    d.update({"label" : []})

    for var in quanti:
        d["label"].append(var)
        for c in quali:
            groups = [df[df[c] == g][var] for g in df[c].dropna().unique()]
            [s.dropna(inplace=True) for s in groups]
            stat, p = kruskal(*groups, nan_policy="raise")
            d[f"p_{c}"].append(p)
            d[f"s_{c}"].append(stat)

    d = DataFrame(d).set_index("label")
    with open(PATH_ROOT/"tables"/f"bi_tests_kruskal_wallis", "w") as file:
        file.write("KRUSKAL WALLIS TEST\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")

    return DataFrame(d)


# QUANTI X QUANTI
def _scatter_plot(df : DataFrame, var1 : str, var2 :str) -> None:
    
    df[[var1, var2]].plot.scatter(x=var1, y=var2, alpha=0.1, colormap="viridis")
    plt.title(f'Dispersão {var1} {var2}')
    plt.xlabel(var1)
    plt.ylabel(var2)

    plt.savefig(PATH_ROOT/"img"/f"bi_scatter_{var1}_{var2}")
    plt.close()

    return


def _corr_matrix_heatmap(df : DataFrame, quanti : list[str]) -> DataFrame:

    corr = df[quanti].corr(method="pearson")

    with open(PATH_ROOT/"tables"/f"bi_corr_matrix", "w") as file:
        file.write("PEARSON MATRIX\n\n")
        corr.to_markdown(file)

    sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt='.2f')
    plt.title(f"Pearson Matrix")
    plt.savefig(PATH_ROOT/"img"/"bi_corr_matrix")
    plt.close()

    return corr


# METRICS
def _spddi(df : DataFrame, quali : list[str], target : str) -> DataFrame:

    d = {
            "variable": [],
            "privileged_group": [],
            "priv_rate" : [],
            "unprivileged_group": [],
            "unpriv_rate" : [],
            "disparate_impact": [],
            "statistical_parity_difference": [],
            }

    for var in quali:
        if var == target:
            continue
        rates = df.groupby(var)[target].mean()
        priv_group = rates.idxmax()
        priv_rate = rates.max()

        for group, rate in rates.items():
            if group == priv_group:
                continue
            di = rate / priv_rate if priv_rate > 0 else 0
            spd = rate - priv_rate
            d["variable"].append(var)
            d["privileged_group"].append(priv_group)
            d["priv_rate"].append(priv_rate)
            d["unprivileged_group"].append(group)
            d["unpriv_rate"].append(rate)
            d["disparate_impact"].append(di)
            d["statistical_parity_difference"].append(spd)

    d = DataFrame(d)
    with open(PATH_ROOT/"tables"/f"bi_tests_spddi", "w") as file:
        file.write("STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")

    return d


def _point_biserial(df : DataFrame, quant : list[str], target : str) -> DataFrame:

    d = {
            "label" : [],
            "correlation" : [],
            "p_value" : []
            }

    for c in quant:
        df_clean = df[[target, c]].dropna()
        corr, pvalue = pointbiserialr(df_clean[target], df_clean[c])
        d["label"].append(c)
        d["p_value"].append(pvalue)
        d["correlation"].append(corr)

    d = DataFrame(d).set_index("label")
    with open(PATH_ROOT/"tables"/f"bi_tests_point_biserial", "w") as file:
        file.write("POINT BISERIAL TEST\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")

    return d


def bivariate_analysis(df : DataFrame) -> None:

    quali = ["race", "fulltime", "fam_inc", "male", "pass_bar", "tier"]
    quant = ["lsat", "ugpa", "zfygpa", "zgpa", "age"]

    _corr_matrix_heatmap(df, quant)    
    _coefficient_v(df, quali)
    _kruskal_wallis(df, quali, quant)
    _point_biserial(df, quant, "pass_bar")
    _spddi(df, quali, "pass_bar")

    for ql in quali:
        for qt in quant:
            _violin_plot(df, qt, ql)
            _student_mannwhitneyu_test(df, qt, ql)

    while len(quant) > 1:
        for i in range(1, len(quant)):
            _scatter_plot(df, quant[0], quant[i])
        quant.pop(0)

    while len(quali) > 1:
        for i in range(1, len(quali)):
            ct = _contingency_table(df[[quali[0], quali[i]]])
            _stacked_bar(ct, quali[0], quali[i])
            _stacked_bar(ct, quali[i], quali[0])
            _chi_square_test(df, quali[0], quali[i])
        quali.pop(0)


