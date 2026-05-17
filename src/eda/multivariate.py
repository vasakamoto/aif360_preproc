
from src.configs import PATH_ROOT

from matplotlib import pyplot as plt
from numpy import (
        average,
        nan,
        number,
        cumsum
        )
from pandas import (
        DataFrame,
        Series,
        qcut
        )
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor


def _spddicsp(df: DataFrame, quali: list[str], quanti: list[str], target: str) -> DataFrame:
    """
    STATISTICAL PARITY DIFFERENCE
       measures the gap between the probability of a positive outcome for unprivileged
       and privileged groups
       SPD = P(Ŷ = 1 | D = unprivileged) - (Ŷ = 1 | D = privileged)
       SPD is not close to 0.0 -> system has a tendency to favor one group

    DISPARATE IMPACT
       while SPD measures the difference between probabilities, disparete impact measures
       the proportion between probabilities
       more sensible in some cases where the difference is small but the proportion
       is significative
       DI is not close to 1.0 or not bigger than 0.8 -> system has a tendency to favor 
       one group
           SPD = -0.09 <- 0.01 - 0.10
           DI = 0.1 <- 0.01 / 0.10

    CONDITIONAL STATISTICAL PARITY
       check if there is a "justification" for the statistical disparaty
       use control variables (legitimate factors) to check direct or indirect bias
           direct bias -> present in dataset
           indirect bias -> present in data collection
    """

    d = {
        "variable": [],
        "privileged_group": [],
        "priv_rate": [],
        "unprivileged_group": [],
        "unpriv_rate": [],
        "control_variable": [], # Nova coluna
        "disparate_impact": [],
        "statistical_parity_difference": [],
        "conditional_statistical_parity": [], # Nova coluna
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
            
            for c_var in quanti:
                temp_df = df[[var, c_var, target]].copy()
                temp_df['decile'] = qcut(temp_df[c_var].rank(method='first'), q=10, labels=False)
                
                strata_diffs = []
                weights = []
                
                for i in range(10):
                    subset = temp_df[temp_df['decile'] == i]
                    
                    p_data = subset[subset[var] == priv_group][target]
                    u_data = subset[subset[var] == group][target]
                    
                    if not p_data.empty and not u_data.empty:
                        strata_diffs.append(u_data.mean() - p_data.mean())
                        weights.append(len(subset))
                
                csp = average(strata_diffs, weights=weights) if strata_diffs else nan
                
                di = rate / priv_rate if priv_rate > 0 else 0
                spd = rate - priv_rate
                
                d["variable"].append(var)
                d["privileged_group"].append(priv_group)
                d["priv_rate"].append(priv_rate)
                d["unprivileged_group"].append(group)
                d["unpriv_rate"].append(rate)
                d["control_variable"].append(c_var)
                d["disparate_impact"].append(di)
                d["statistical_parity_difference"].append(spd)
                d["conditional_statistical_parity"].append(csp)

    d = DataFrame(d)
    with open(PATH_ROOT/"results"/"tables"/"multivariate"/f"tests_spddicsp", "w") as file:
        file.write("SPD, DI AND CONDITIONAL STATISTICAL PARITY\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")

    return d
    # the results indicate that the "mistakes" of the non-white group are punished 
    # more heavily, there is a difference of reprovation of 12% in the lower deciles,
    # that means, there is some kind of direct bias in the dataset by race
    # for sex there is a huge gap with cdi for the lower decile, but the cspd is not 
    # significative
    # I don't think there will be a significative age bias in the dataset, but is good
    # to check for it


def _vif(df : DataFrame, target_feat : str) -> Series:
    """
    VIF measures the intensity of the deviation, treating the variable under analysis
    as a function of other variables:

                            VIF = 1 / (1 - R²)

    So, big values for VIF indicates a strong overposition of variables, because
    a bigger R² (coefficient of determination, which indicates the variance of a
    dependent variable has from the independent variable in a regression model) 
    indicates that there is no variance, which means that those variables are strongly
    binded.
    """

    X = df.copy()
    X.drop(columns=[target_feat], inplace=True)
    X.dropna(inplace=True)

    X['intercept'] = 1
    X = X.astype(float)
    
    vif_series = Series(
        [variance_inflation_factor(X.values, i) for i in range(X.shape[1])], 
        index=X.columns
    )
    vif_series.drop('intercept', inplace=True)

    with open(PATH_ROOT/"results"/"tables"/"multivariate"/f"tests_vif", "w") as file:
        file.write("VARIANCE INFLATION FACTOR\n\n")
        vif_series.to_markdown(file)
        file.write("\n\n\n")

    return vif_series
    # race        1.276508
    # lsat        1.566030
    # ugpa        1.288537
    # zfygpa      4.237095
    # zgpa        4.391734
    # fulltime    1.116033
    # fam_inc     1.118013
    # male        1.044756
    # tier        1.433240
    # age         1.194559

    # Generally there is no significant value for VIF, which indicates a strong 
    # independency between variables. The only variable which that looks like there is 
    # some dependency is zgpa and zfygpa, which makes sense, because the gpa for the 
    # first year is used to calculate gpa
    # Also, values of 1.28 for race indicates that there is no strong dependency between
    # race and other socioeconomic variables (not a proxy)


def _spearman_matrix(df : DataFrame) -> DataFrame:

    corr = df.corr(method="spearman")

    sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt='.2f')
    plt.title(f"Pearson Matrix")
    plt.savefig(PATH_ROOT/"results"/"charts"/"multivariate"/"corr_matrix")
    plt.close()

    with open(PATH_ROOT/"results"/"tables"/"multivariate"/f"tests_spearman_corr_matrix", "w") as file:
        file.write("SPEARMAN MATRIX\n\n")
        corr.to_markdown(file)
        file.write("\n\n\n")

    return corr 
#               lsat    zfygpa      zgpa      ugpa      race  fulltime      male  pass_bar
# lsat      1.000000  0.258509  0.278077  0.235693  0.271702 -0.104909  0.073731  0.199797
# zfygpa    0.258509  1.000000  0.872999  0.173721  0.272615  0.017944  0.047042  0.234583
# zgpa      0.278077  0.872999  1.000000  0.225357  0.290348  0.011017  0.006361  0.265207
# ugpa      0.235693  0.173721  0.225357  1.000000  0.168878 -0.108277 -0.131960  0.132451
# race      0.271702  0.272615  0.290348  0.168878  1.000000  0.019552  0.073717  0.187982
# fulltime -0.104909  0.017944  0.011017 -0.108277  0.019552  1.000000 -0.006282 -0.066872
# male      0.073731  0.047042  0.006361 -0.131960  0.073717 -0.006282  1.000000  0.022349
# pass_bar  0.199797  0.234583  0.265207  0.132451  0.187982 -0.066872  0.022349  1.000000

# Race have almost the correlation with pass bar as lsat, zfygpa, zgpa and ugpa 
# which is a strong indicator that race has a strong bias. Model might use it as
# a predictor.
# As expected, grading features have correlation with target feature.
# Zgpa and zfygpa are strongly correlated, it may be redundant have both. 
# Fulltime and male have no significant correlation with pass bar.


def _scatter_plot(df : DataFrame, quanti : list[str], target : str) -> None:

    a = quanti.copy()

    while len(a) > 1:
        for i in range(1, len(a)):
            sns.scatterplot(
                    data = df[[a[0], a[i], target]],
                    x=a[0],
                    y=a[i],
                    hue=target,
                    alpha=0.1,
                    palette="viridis"
                    )
            plt.title(f'Dispersão {a[0]} {a[1]}')
            plt.xlabel(a[0])
            plt.ylabel(a[1])

            plt.savefig(PATH_ROOT/"results"/"charts"/"multivariate"/f"scatter_{a[0]}_{a[1]}")
            plt.close()
        a.pop(0)


def _violin_plot(df : DataFrame, quanti : list[str], quali : list[str], target : str) -> None:

    for qt in quanti:
        for ql in quali:
            sns.violinplot(
                data=df[[qt, ql, target]], 
                x=ql,
                y=qt,
                hue=target,
                inner='quartile',
                palette='muted',
                cut=0
            )

            plt.title(f'{qt} X {ql}')
            plt.xlabel(ql)
            plt.ylabel(qt)
            plt.grid(axis='y', alpha=0.3)

            plt.tight_layout()
            plt.savefig(PATH_ROOT/"results"/"charts"/"multivariate"/f"violin_{ql}_{qt}")
            plt.close()


def _stacked_bar(df : DataFrame, quali : list[str], target : str) -> None:

    for idx in quali:
        for var in quali:
            if idx == var: continue
            df_clean = df.dropna(subset=[idx, var, target]).copy()
            df_counts = df_clean.groupby([idx, var, target]).size().unstack(fill_value=0)
            index = sorted(df_clean[idx].unique())
            _, axes = plt.subplots(1, len(index), figsize=(15, 6), sharey=True)
            if len(index) == 1:
                axes = [axes]

            for i, ft in enumerate(index):
                data_subset = df_counts.xs(ft, level=idx)
                data_relative = data_subset.div(data_subset.sum(axis=1), axis=0)
                data_relative.plot(
                    kind='bar', 
                    stacked=True, 
                    ax=axes[i], 
                    color=['#5b84c1', '#d99066'], 
                    edgecolor='black'
                )
                axes[i].set_title(f"{idx} = {ft} (Relative)")
                axes[i].set_xlabel(var)
                axes[i].set_ylabel("Proportion")
                axes[i].set_ylim(0, 1)
            plt.tight_layout()
            plt.savefig(PATH_ROOT/"results"/"charts"/"multivariate"/f"stacked_{idx}_{var}")
            plt.close()


def _pca(df : DataFrame, target_feat : str) -> tuple:
    X = df.select_dtypes(include=[number]).dropna().copy()
    X.drop(columns=[target_feat], inplace=True)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA()
    pca_data = pca.fit_transform(X_scaled)
    exp_var_cum = cumsum(pca.explained_variance_ratio_)

    plt.figure(figsize=(10, 5))
    plt.step(range(1, len(exp_var_cum) + 1), exp_var_cum, where='mid', label='Variância Acumulada')
    plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.5, label='Variância Individual')
    
    plt.ylabel('Razão de Variância Explicada')
    plt.xlabel('Componentes Principais')
    plt.title('Análise de Variância do PCA')
    plt.legend(loc='best')
    plt.grid(alpha=0.3)
    plt.savefig(PATH_ROOT/"results"/"charts"/"multivariate"/"pca")
    plt.close()





    loadings = DataFrame(
            pca.components_[0], 
            index=X.columns, 
            columns=['PC1_Weight']
            ).sort_values(by='PC1_Weight', ascending=False)

    print(loadings) 
    pca_results = pca.transform(X_scaled)

    df_pca_plot = DataFrame(
            data = pca_results[:, :2], 
            columns = ['PC1', 'PC2']
            )
    df_pca_plot['pass_bar'] = df.dropna(subset=X.columns.tolist())['pass_bar'].values

    plt.figure(figsize=(10, 7))
    sns.scatterplot(
            x='PC1', y='PC2', 
            hue='pass_bar', 
            data=df_pca_plot, 
            palette={0: '#5b84c1', 1: '#d99066'}, 
            alpha=0.4,
            edgecolor=None
            )

    plt.title('Projeção do Dataset no Espaço PCA (PC1 vs PC2)')
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% da variância)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% da variância)')
    plt.grid(alpha=0.2)
    plt.savefig(PATH_ROOT/"results"/"charts"/"multivariate"/"pca_scatter")
    plt.close()



    return pca, exp_var_cum


def multivariate_analysis(df : DataFrame) -> None:

    quali = ["race", "fulltime", "fam_inc", "male", "tier"]
    quant = ["lsat", "ugpa", "zfygpa", "zgpa"]#, "age"]
    target = "pass_bar"

    _spddicsp(df, quali, quant, target)
    _vif(df, target)
    _spearman_matrix(df)

    _scatter_plot(df, quant, "pass_bar")
    _violin_plot(df, quant, quali, "pass_bar")
    _stacked_bar(df, quali, "pass_bar")
    _pca(df, target)
