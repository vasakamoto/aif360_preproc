
from itertools import cycle
from math import factorial

from src.configs import (
        PATH_ROOT,
        TRANSLATIONS,
        HACHING_PATTERNS,
        TRUNCATED_GREY
        )

from matplotlib import pyplot as plt
from numpy import (
        sqrt,
        )
from pandas import (
        DataFrame,
        crosstab,
        )
from scipy.stats import (
        chi2_contingency,
        ttest_ind,
        mannwhitneyu,
        kruskal,
        pointbiserialr
        )
import seaborn as sns


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
    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write(f"\n\nCONTINGENCY TABLE - {" X ".join(columns)}\n\n")
        frequency.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return frequency


def _stacked_bar(df : DataFrame, index : str, variable : str) -> None:

    plot = df[f"rel_f_{index}_by_{variable}"].unstack(level=variable)
    ax = plot.plot(kind="bar", stacked=True, width=0.85, edgecolor="black", cmap=TRUNCATED_GREY)

    for container, hatch_pattern in zip(ax.containers, cycle(HACHING_PATTERNS)):
        for patch in container.patches:
            patch.set_hatch(hatch_pattern)

    ax.set_title(f"Distribuição de {TRANSLATIONS.get(f'{index}', index)} por {TRANSLATIONS.get(f'{variable}', variable)}")
    ax.set_xlabel(f"{TRANSLATIONS.get(f'{index}', index)}")
    ax.set_ylabel("Frequência Relativa")

    ax.legend(title=TRANSLATIONS.get(f"{variable}", variable))

    ax.grid(axis='y', linestyle=':', alpha=0.6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(PATH_ROOT/"results"/"charts"/"bivariate"/f"stacked_{index}_{variable}")
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

    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write(f"\n\nCHI SQUARED TEST - {var1} X {var2}\n\n")
        matrix.to_markdown(file)
        file.write("\n\n\n")
        file.write(f"\nChi squared: {chit[0]:.4f}\n")
        file.write(f"\nP-value: {chit[1]:.4f}\n")
        file.write(f"\nDegrees of Freedom: {chit[2]}\n")
        file.write("\n\n\n")
        file.write("_"*100)

    return {
            "matrix" : matrix,
            "chi2" : chit[0],
            "p_value" : chit[1],
            "degree_freedon" : chit[2],
            }


def _coefficient_v(df : DataFrame, categ_feats : list) -> DataFrame:
    """
    The Cramér coefficient, or V  of Cramér, measures how much two nominal variables
    are dependent of each other
                    V = sqrt( (Qui^2 / n) / min(k-1, r-1) )
    Qui^2: independent Pearson test
    n: quantity of samples
    k: quantity of columns
    r: quantity of rows
    """

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
    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write("\n\nCRAMER TEST - COEFFICIENT V\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return d
#               race  fulltime   fam_inc      male      tier  pass_bar
# race      0.999838  0.018133  0.216824  0.073293  0.202271  0.187597
# fulltime  0.018133  0.999685  0.076914  0.000000  0.109763  0.066158
# fam_inc   0.216824  0.076914  1.000000  0.048234  0.065707  0.086778
# male      0.073293  0.000000  0.048234  0.999909  0.046955  0.021115
# tier      0.202271  0.109763  0.065707  0.046955  1.000000  0.141560
# pass_bar  0.187597  0.066158  0.086778  0.021115  0.141560  0.999549

# There is no strong correlation for family income and pass bar, which indicates
# that probably there is no **direct** bias towards this feature. The same occurs
# with tier. But both of these features are somewhat related to race, which might
# indicate a proxy between these features.
# Full time and male do not have a significant coefficient v with pass bar, which
# indicates that both might be a weak predictor. At least in these simple bivariate 
# analysis.
# Confirm with some training.
# Race have a significant value, it might have some bias in there. But, also, is
# associated with race, which might propagate some bias.
# This bias might show with people of color being in the least privileged tiers.


# QUANTI X QUALI
def _violin_plot(df : DataFrame, quanti : str, quali : str) -> None:

    ax = sns.violinplot(
        data=df[[quanti, quali]], 
        x=quali,
        y=quanti,
        inner='quartile',
        palette='gray',
        cut=0
    )

    for collection, hatch_pattern in zip(ax.collections, cycle(HACHING_PATTERNS)):
        collection.set_hatch(hatch_pattern)
        collection.set_edgecolor('black')  # Ensures structural boundaries remain visible
        collection.set_linewidth(1.5)

    plt.title(f"{TRANSLATIONS.get(f"{quali}", quali)} X {TRANSLATIONS.get(f"{quanti}", quanti)}", fontsize=12, fontweight='bold', pad=12)
    plt.xlabel(f"{TRANSLATIONS.get(f"{quali}", quali)}", fontsize=10)
    plt.ylabel(f"{TRANSLATIONS.get(f"{quanti}", quanti)}", fontsize=10)
    plt.grid(axis='y', alpha=0.3, linestyle=':')
    
    sns.despine()

    plt.tight_layout()
    plt.savefig(PATH_ROOT/"results"/"charts"/"bivariate"/f"violin_{quali}_{quanti}")
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

    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write(f"\n\nSTUDENT'S T AND MANN-WHITNEY U TEST - {quant} X {quali}\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return d.loc[(d["t_test_p_value"] < 0.05) & (d["mann_whitney_p_value"] < 0.05)].sort_values("group_a")


def _kruskal_wallis(df : DataFrame, quali : list[str], quanti : list[str]) -> DataFrame:
    """A non-parametric test (does not assume any specific distribution, consequently
    does not make use of averages and variance), which focus is over frequency only.
    This test hypothesis is that:
        H0 = population median are equal (both population should have the same probability)
        H1 = one population have a different median (one population have a higher probability)

                                        k
        H = ( 12 / ( N * ( N+1 ) ) ) * SUM ( ( Ri^2 / ni ) - ( 3 * ( N + 1 ) ) )
                                       i=1 
        N   = number of samples
        k   = number of groups / categories
        ni  = number of samples for a group
        Ri  = sum of ranks of category
    """

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
    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write("\n\nKRUSKAL WALLIS TEST\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return DataFrame(d)


# QUANTI X QUANTI
def _scatter_plot(df : DataFrame, var1 : str, var2 :str) -> None:

    ax = df[[var1, var2]].plot.scatter(
        x=var1,
        y=var2,
        alpha=0.2,
        color='#444444',
        edgecolors='black',
        linewidths=0.5
    )
    ax.set_title(f'Dispersão: {TRANSLATIONS.get(f"{var1}", var1)} vs {TRANSLATIONS.get(f"{var2}", var2)}', fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel(f"{TRANSLATIONS.get(f"{var1}", var1)}", fontsize=10)
    ax.set_ylabel(f"{TRANSLATIONS.get(f"{var2}", var2)}", fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(PATH_ROOT / "results" / "charts" / "bivariate" / f"scatter_{var1}_{var2}.png")
    plt.close()


def _corr_matrix_heatmap(df: DataFrame, quanti: list[str]) -> DataFrame:

    corr = df[quanti].corr(method="pearson")
    with open(PATH_ROOT / "results" / "tables" / "bivariate.md", "a") as file:
        file.write("\n\nPEARSON MATRIX\n\n")
        corr.to_markdown(file)
        file.write("\n\n\n")
        file.write("_" * 100)

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        corr, 
        annot=True, 
        cmap=TRUNCATED_GREY, 
        center=0, 
        fmt='.2f', 
        linewidths=0.5, 
        linecolor='black',
        ax=ax
    )
    ax.set_title("Matriz de Pearson", fontsize=12, fontweight='bold', pad=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(PATH_ROOT / "results" / "charts" / "bivariate" / "corr_matrix.png", dpi=300)
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
    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write("\n\nSTATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

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
    with open(PATH_ROOT/"results"/"tables"/"bivariate.md", "a") as file:
        file.write("\n\nPOINT BISERIAL TEST\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return d


def bivariate_analysis(df : DataFrame) -> None:

    quali = ["race", "fulltime", "fam_inc", "male", "pass_bar", "tier"]
    quant = ["lsat", "ugpa", "zfygpa", "zgpa", "age"]

    (PATH_ROOT/"results"/"tables"/"bivariate.md").unlink(missing_ok=True)

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


