
from numpy import (
        sqrt,
        var
        )
from pandas import (
        DataFrame,
        Series,
        crosstab
        )
from scipy.stats import (
        chi2_contingency,
        kruskal
        )
from statsmodels.stats.outliers_influence import variance_inflation_factor


def _corr_features(df : DataFrame, features : list[str]) -> DataFrame:
    """
    Check for strongly correlated features

    !!!!!!!ONLY APPLYED FOR ORDINAL AND NUMERICAL VARIABLES!!!!!!!!

    """

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

    return df[features].corr(method="spearman", numeric_only=True)


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

    # it needs a constant
    X['intercept'] = 1

    vif_series = Series(
        [variance_inflation_factor(X.values, i) for i in range(X.shape[1])], 
        index=X.columns
    )
    vif_series.drop('intercept', inplace=True)

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

    return vif_series


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

    return DataFrame(d, index=d["label"]).drop(columns=["label"])


def kruskal_wallis(df : DataFrame, protected_feat : list[str], predict_feat : list[str]) -> None:
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

    dprob = { x : [] for x in predict_feat }
    dprob.update({"group" : []})
    dstat = { x : [] for x in predict_feat }
    dstat.update({"group" : []})

    for protfeat in protected_feat:
        dprob["group"].append(protfeat)
        dstat["group"].append(protfeat)
        for predfeat in predict_feat:
            groups = [df[df[protfeat] == g][predfeat] for g in df[protfeat].dropna().unique()]
            [s.dropna(inplace=True) for s in groups]
            stat, p = kruskal(*groups, nan_policy="raise")
            dprob[predfeat].append(p)
            dstat[predfeat].append(stat)

    print(DataFrame(dprob).set_index("group"))
    print(DataFrame(dstat).set_index("group"))
    #grupos = [df[df['race'] == g]['lsat'] for g in df['race'].unique()]
    #stat, p = kruskal(*grupos)

    #for g in df['race'].unique():
    #    print(g)
    #print(f'Estatística: {stat:.4f}, p-valor: {p:.4e}')
    return


def analysis_correlation(df : DataFrame) -> None:

    categorical_feats = ["fam_inc", "tier"]
    continuous_feats = ["lsat", "zfygpa", "zgpa", "ugpa"]
    binary_feats = ["race", "fulltime", "male"] 
    target_feat = ["pass_bar"]

    #_corr_features(df, continuous_feats + binary_feats + target_feat)
    #_vif(df, "pass_bar"))
    #_coefficient_v(df, categorical_feats + binary_feats + target_feat)
    kruskal_wallis(df, categorical_feats + binary_feats, continuous_feats + target_feat)
    return
