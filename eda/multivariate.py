
from math import factorial

from src.configs import PATH_ROOT

from matplotlib import pyplot as plt
from numpy import (
        sqrt,
        average,
        nan,
        number,
        cumsum
        )
from pandas import (
        DataFrame,
        Series,
        crosstab,
        qcut
        )
from scipy.stats import (
        alpha,
        chi2_contingency,
        ttest_ind,
        mannwhitneyu,
        kruskal,
        pointbiserialr
        )
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

## MULTIVARIATE ANALYSIS
# [x] conditional statistical parity
# [x] VIF (VARIANCE INFLATION FACTOR)
# [x] bivariate charts with hue (pass_bar)
# [x] PCA
# [x] spearman matrix

def _spddicsp(df: DataFrame, quali: list[str], quanti: list[str], target: str) -> DataFrame:
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
    with open(PATH_ROOT/"tables"/f"multi_tests_spddicsp", "w") as file:
        file.write("SPD, DI AND CONDITIONAL STATISTICAL PARITY\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")

    return d


def _vif(df : DataFrame, target_feat : str) -> Series:

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

    with open(PATH_ROOT/"tables"/f"multi_tests_vif", "w") as file:
        file.write("VARIANCE INFLATION FACTOR\n\n")
        vif_series.to_markdown(file)
        file.write("\n\n\n")

    return vif_series


def _spearman_matrix(df : DataFrame) -> DataFrame:

    corr = df.corr(method="spearman")

    sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt='.2f')
    plt.title(f"Pearson Matrix")
    plt.savefig(PATH_ROOT/"img"/"multi_corr_matrix")
    plt.close()

    with open(PATH_ROOT/"tables"/f"multi_tests_spearman_corr_matrix", "w") as file:
        file.write("SPEARMAN MATRIX\n\n")
        corr.to_markdown(file)
        file.write("\n\n\n")

    return corr 


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

            plt.savefig(PATH_ROOT/"img"/f"multi_scatter_{a[0]}_{a[1]}")
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
            plt.savefig(PATH_ROOT/"img"/f"multi_violin_{ql}_{qt}")
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
            plt.savefig(PATH_ROOT/"img"/f"multi_stacked_{idx}_{var}")
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
    plt.savefig(PATH_ROOT/"img"/f"multi_pca")
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
    plt.savefig(PATH_ROOT/"img"/f"multi_pca_scatter")
    plt.close()



    return pca, exp_var_cum


def multivariate_analysis(df : DataFrame) -> None:

    quali = ["race", "fulltime", "fam_inc", "male", "tier"]
    quant = ["lsat", "ugpa", "zfygpa", "zgpa"]#, "age"]
    target = "pass_bar"

    #_spddicsp(df, quali, quant, target)
    #_vif(df, target)
    #_spearman_matrix(df)

    #_scatter_plot(df, quant, "pass_bar")
    #_violin_plot(df, quant, quali, "pass_bar")
    #_stacked_bar(df, quali, "pass_bar")
    _pca(df, target)
