
from aif360.datasets import StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric

from pandas import (
        DataFrame,
        Series,
        qcut
        )

#   STATISTICAL PARITY DIFFERENCE
#       measures the gap between the probability of a positive outcome for unprivileged
#       and privileged groups
#       SPD = P(Ŷ = 1 | D = unprivileged) - (Ŷ = 1 | D = privileged)
#       SPD is not close to 0.0 -> system has a tendency to favor one group

#   DISPARATE IMPACT
#       while SPD measures the difference between probabilities, disparete impact measures
#       the proportion between probabilities
#       more sensible in some cases where the difference is small but the proportion
#       is significative
#       DI is not close to 1.0 or not bigger than 0.8 -> system has a tendency to favor 
#       one group
#           SPD = -0.09 <- 0.01 - 0.10
#           DI = 0.1 <- 0.01 / 0.10

#   CONDITIONAL STATISTICAL PARITY
#       check if there is a "justification" for the statistical disparaty
#       use control variables (legitimate factors) to check direct or indirect bias
#           direct bias -> present in dataset
#           indirect bias -> present in data collection

#   VARIANCE
#       a bigger variance indicates a feature that is more unpredictible 

# categorize age
# that is because when the population is very small the variance can be huge, and
# is the case here, with population older then 50 have 184 individuals with a huge
# variance, from 12% of reprovation to 100%

# "A variável 'Idade' foi discretizada em intervalos quinquenais e decenais para mitigar
# a variância observada na cauda da distribuição. Esta abordagem permitiu elevar o suporte
# mínimo de cada categoria para n>180, garantindo a estabilidade das taxas de reprovação 
# observadas. A análise resultante revelou um incremento progressivo na taxa de reprovação,
# que se estabiliza entre os 35 e 45 anos (≈8.5%) antes de apresentar um salto significativo
# para 19.02% na faixa dos 50 anos, evidenciando comportamentos distintos de performance 
# acadêmica que justificam o tratamento categórico da feature."


def _spddi(df : DataFrame) -> None:

    ds = StandardDataset(
            df=df,
            label_name="pass_bar",
            favorable_classes=[1],
            protected_attribute_names=["race"],
            privileged_classes=[[7]]
            )

    metrics = BinaryLabelDatasetMetric(
            ds,
            unprivileged_groups=[
                {"race" : 1.0},
                {"race" : 2.0},
                {"race" : 3.0},
                {"race" : 4.0},
                {"race" : 5.0},
                {"race" : 6.0},
                {"race" : 8.0},
                ],
            privileged_groups=[{"race" : 7.0}],
            )

    print(f"STATISTICAL PARITY DIFFERENCE: {round(metrics.statistical_parity_difference(), 4)}")    # -0.1127
    print(f"DISPARATE IMPACT: {round(metrics.disparate_impact(), 4)}")                              # 0.8835

    # disparate impact indicates that there is no significant difference between groups
    # DI > 80
    # but SPD <> 0.00, 11.3% of difference between groups, which might configure in a
    # moderate bias towards race


    def _group_race(r : float) -> int:
        b = 0
        try:
            b = 1 if int(r) == 7 else 0
        except ValueError:
            pass
        finally:
            return b


    print("\nGROUPING RACES\n")

    df["race"] = df["race"].apply(_group_race)

    ds = StandardDataset(
            df=df,
            label_name="pass_bar",
            favorable_classes=[1],
            protected_attribute_names=["race"],
            privileged_classes=[[1]]
            )

    metrics = BinaryLabelDatasetMetric(
            ds,
            unprivileged_groups=[
                {"race" : 0},
                ],
            privileged_groups=[{"race" : 1}],
            )

    print(f"STATISTICAL PARITY DIFFERENCE: {round(metrics.statistical_parity_difference(), 4)}")    # -0.113
    print(f"DISPARATE IMPACT: {round(metrics.disparate_impact(), 4)}")                              # 0.8832

    # there is no significant difference between grouping races into a binary variable
    # difference of 0.0003



def _conditional_parity(df : DataFrame, protected_feat : str, conditional_feat : str,
                        target_feat : str) -> Series:
    """ Checks if there is a direct bias in the dataset, meaning that the `conditional_feat`
    is not being used to select truly the target_feat.
    """

    df_csp = df[[conditional_feat, protected_feat, target_feat]]
    df_csp["decile"] = qcut(df_csp[conditional_feat], 10, range(1,11))
    df_csp = df_csp.groupby(["decile", protected_feat])
    s_csp = df_csp[["decile", protected_feat, target_feat]].value_counts(normalize=True) 
    s_csp = s_csp.loc[(slice(None), slice(None), 0)]
    s_csp = s_csp.unstack(level=protected_feat)
    s_csp["conditional_spd"] = s_csp[0] - s_csp[1]
    s_csp["conditional_di"] = 1 - (s_csp[0] / s_csp[0] + s_csp[1])
    print(s_csp["conditional_spd"])
    print(s_csp["conditional_di"])

    # the results indicate that the "mistakes" of the non-white group are punished 
    # more heavily, there is a difference of reprovation of 12% in the lower deciles,
    # that means, there is some kind of direct bias in the dataset by race
    # for sex there is a huge gap with cdi for the lower decile, but the cspd is not 
    # significative
    # I don't think there will be a significative age bias in the dataset, but is good
    # to check for it

    return Series()


def _protected_distribution(df : DataFrame, protected_feats : list[str], 
                            target_feat : str) -> list[DataFrame]:
    
    f = []
    for feat in protected_feats:
        pdf = df[[feat, target_feat]].value_counts()
        pdf = pdf.unstack(level=target_feat)
        pdf[0] = pdf[0].fillna(0)
        pdf[1] = pdf[1].fillna(0)
        pdf["population"] = pdf[1] + pdf[0]
        pdf["relative_reprovation"] = round(pdf[0] / (pdf[1] + pdf[0]) * 100, 2)
        f.append(pdf[["population", "relative_reprovation"]].sort_index())

    return f


def _spddi_age(df : DataFrame) -> None:

    ds = StandardDataset(
            df=df,
            label_name="pass_bar",
            favorable_classes=[1],
            protected_attribute_names=["age"],
            privileged_classes=[[2, 3]]
            )

    metrics = BinaryLabelDatasetMetric(
            ds,
            unprivileged_groups=[
                {"age" : 1},
                {"age" : 4},
                {"age" : 5},
                {"age" : 6},
                {"age" : 7},
                {"age" : 8},
                ],
            privileged_groups=[
                {"age" : 2},
                {"age" : 3},
                ],
            )

    print(f"STATISTICAL PARITY DIFFERENCE: {round(metrics.statistical_parity_difference(), 4)}")    # -0.1127
    print(f"DISPARATE IMPACT: {round(metrics.disparate_impact(), 4)}")                              # 0.8835

    # there is no significantive SPD neither DI for age
    # SPD ≃ 0.03
    # DI > 0.96

    return


def distribution(df : DataFrame, target_feat : str) -> list[DataFrame]:

    f = []
    columns = df.columns.tolist()
    columns.remove(target_feat)
    for c in columns:
        s = df[[c, target_feat]].value_counts()
        d = s.unstack(level=target_feat)
        f.append(d)

    return f


def analysis_protect(df : DataFrame) -> None:

    protected_feats = [
            "age",
            "male",
            "race"
            ]
    target_feat = "pass_bar"

    #_conditional_parity(data, "race", "zgpa", "pass_bar")
    #_conditional_parity(data, "male", "zgpa", "pass_bar")
    #_protected_distribution(data, protected_feats, target_feat):
    #_spddi_age(data)

    for feat in protected_feats:
        d = df[[feat, target_feat]]
        d = d.groupby(feat)[target_feat].var()
        print(d)

    # Looking at variance of protected features is clear that age should not be a problem
    # there is no huge variance between groups (there is, but the group that have a huge
    # variance is a group with very few samples, for example, for people with 50+ years
    # have a population of maybe 200 individuals, in such case every sample have a bigger
    # impact over the variance.

    # Gender have a somewhat significative variance, a difference of, that means that 
    # women as a group is less homogenous than man

    # The most significative variance is race, non-white being 4x more "disperse" than
    # white, which could be a problem for Random Forests, it is much easier to predict
    # white candidate than non-white


    return
