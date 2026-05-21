
from dataclasses import fields

from src.configs import (
        PATH_ROOT,
        TARGET,
        PROTECTED_ATTRIBUTES,
        PRIVILEGED_GROUP,
        UNPRIVILEGED_GROUP,
        GroupedProcessedDatasets,
        SplitDataset
        )

from aif360.metrics import BinaryLabelDatasetMetric
from pandas import (
        DataFrame,
        merge
        )
from scipy.stats import wasserstein_distance
from sklearn.feature_selection import mutual_info_classif


def _spddi(grouped_ds : GroupedProcessedDatasets, split_ds : SplitDataset) -> DataFrame:

    d = {
            "method" : [],
            "before_spd" : [],
            "before_di" : [],
            "after_spd" : [],
            "after_di" : [],
            }

    metrics_before = BinaryLabelDatasetMetric(
            split_ds.train,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP
            )

    for att in fields(grouped_ds):

        if att.name == "optimized_preprocessing": continue

        metrics_after = BinaryLabelDatasetMetric(
                getattr(grouped_ds, att.name).transformed_train,
                unprivileged_groups=UNPRIVILEGED_GROUP,
                privileged_groups=PRIVILEGED_GROUP
                )
        d["method"].append(att.name)
        d["before_di"].append(round(metrics_before.disparate_impact(), 3))
        d["before_spd"].append(round(metrics_before.statistical_parity_difference(), 3))
        d["after_di"].append(round(metrics_after.disparate_impact(), 3))
        d["after_spd"].append(round(metrics_after.statistical_parity_difference(), 3))

    d = DataFrame(d)
    d["delta_di"] = d["after_di"] - d["before_di"]
    d["delta_spd"] = d["after_spd"] - d["before_spd"]

    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"processing_metrics", "w") as file:
        file.write("STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT\n\n")
        d.to_markdown(file)

    return d


def _w_distance(grouped_ds : GroupedProcessedDatasets, split_ds : SplitDataset) -> DataFrame:

    d = {
            "method" : [],
            "var" : [],
            "wasserstein_distance_before" : [], 
            "wasserstein_distance_after" : [], 
            "wasserstein_distance_delta" : [], 
            }
    quant = ["lsat", "ugpa", "zfygpa", "zgpa", "age"]
    df_before = split_ds.train.convert_to_dataframe()[0]

    for var in quant:
        priv_before = df_before[
                (df_before[PROTECTED_ATTRIBUTES[0]] == 2.0) |
                (df_before[PROTECTED_ATTRIBUTES[0]] == 7.0) 
                ][var]
        unpriv_before = df_before[
                (df_before[PROTECTED_ATTRIBUTES[0]] != 2.0) & 
                (df_before[PROTECTED_ATTRIBUTES[0]] != 7.0) 
                ][var]
        w_distance_before = wasserstein_distance(priv_before, unpriv_before)
        for att in fields(grouped_ds):

            if att.name == "optimized_preprocessing": continue

            df_after = getattr(grouped_ds, att.name).transformed_train.convert_to_dataframe()[0]
            priv_after = df_after[
                    (df_after[PROTECTED_ATTRIBUTES[0]] == 2.0) |
                    (df_after[PROTECTED_ATTRIBUTES[0]] == 7.0) 
                    ][var]                                      
            unpriv_after = df_after[                            
                                    (df_after[PROTECTED_ATTRIBUTES[0]] != 2.0) & 
                                    (df_after[PROTECTED_ATTRIBUTES[0]] != 7.0) 
                                    ][var]
            w_distance_after = wasserstein_distance(priv_after, unpriv_after)

            d["method"].append(att.name)
            d["var"].append(var)
            d["wasserstein_distance_before"].append(w_distance_before)
            d["wasserstein_distance_after"].append(w_distance_after)
            d["wasserstein_distance_delta"].append(w_distance_after - w_distance_before)

    d = DataFrame(d)
    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"processing_metrics", "a") as file:
        file.write("\n\n")
        file.write("_"*100)
        file.write("\n\nWASSERSTEIN DISTANCE\n\n")
        d.to_markdown(file)

    return d


def _mutual_information(grouped_ds : GroupedProcessedDatasets, split_ds : SplitDataset) -> DataFrame:
    """
    Calcula a Informação Mútua entre os atributos preditivos (X) e o alvo (Y)
    antes e depois de cada método de pré-processamento.
    """
    d = {
            "method": [],
            "var": [],
            "mi_before": [],
            "mi_after": [],
            "mi_delta": []
            }

    quant = ["lsat", "ugpa", "zfygpa", "zgpa", "age"]

    df_before = split_ds.train.convert_to_dataframe()[0]
    X_before = df_before[quant]
    y_before = df_before[split_ds.train.label_names[0]]

    # Informação Mútua original para cada variável
    # random_state garante a reprodutibilidade do algoritmo de vizinhos mais próximos do sklearn
    mi_before_values = mutual_info_classif(X_before, y_before, random_state=42)
    mi_before_dict = dict(zip(quant, mi_before_values))

    for att in fields(grouped_ds):
        if att.name == "optimized_preprocessing": 
            continue

        df_after = getattr(grouped_ds, att.name).transformed_train.convert_to_dataframe()[0]
        X_after = df_after[quant]
        y_after = df_after[split_ds.train.label_names[0]]

        # Informação Mútua após o pré-processamento
        mi_after_values = mutual_info_classif(X_after, y_after, random_state=42)
        mi_after_dict = dict(zip(quant, mi_after_values))

        for var in quant:
            mi_b = mi_before_dict[var]
            mi_a = mi_after_dict[var]

            d["method"].append(att.name)
            d["var"].append(var)
            d["mi_before"].append(round(mi_b, 5))
            d["mi_after"].append(round(mi_a, 5))
            d["mi_delta"].append(round(mi_a - mi_b, 5))

    df_mi = DataFrame(d)
    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"processing_metrics", "a") as file:
        file.write("\n\n")
        file.write("_"*100)
        file.write("\n\nATTRIBUTE-TARGET MUTUAL INFORMATION\n\n")
        df_mi.to_markdown(file)

    return df_mi


def _intersectional_spd(grouped_ds : GroupedProcessedDatasets, split_ds : SplitDataset) -> DataFrame:
    """
    Mapeia os subgrupos interseccionais e calcula o hiato máximo de Paridade Estatística
    (Pior cenário de SPD entre o subgrupo mais privilegiado e o menos privilegiado).
    """

    quali = ["race", "fam_inc"]
    target_col = split_ds.train.label_names[0]

    # 1. Base Original (Antes)
    df_before, _ = split_ds.train.convert_to_dataframe()
    df_res = df_before.groupby(quali).agg(
            sample_size=(target_col, 'count'),
            rate_before=(target_col, 'mean')
            ).reset_index()

    # Arredonda a taxa original
    df_res['rate_before'] = df_res['rate_before'].round(3)

    # 2. Coleta das taxas modificadas (Depois) para cada método
    for att in fields(grouped_ds):
        if att.name == "optimized_preprocessing": 
            continue

        dataset_target = getattr(grouped_ds, att.name).transformed_train
        df_after, _ = dataset_target.convert_to_dataframe()

        col_name = f"rate_after_{att.name}"

        # Considera os pesos para o cálculo ponderado do Reweighing
        if hasattr(dataset_target, 'instance_weights') and att.name == "reweighing":
            df_after['__weights'] = dataset_target.instance_weights
            def weighted_mean(group):
                return (group[target_col] * group['__weights']).sum() / group['__weights'].sum()

            rates_after = df_after.groupby(quali).apply(weighted_mean).reset_index()
            rates_after.columns = quali + [col_name]
        else:
            rates_after = df_after.groupby(quali)[target_col].mean().reset_index()
            rates_after.columns = quali + [col_name]

        # Insere a nova coluna no DataFrame consolidado via merge
        df_res = merge(df_res, rates_after, on=quali, how='left')
        df_res[col_name] = df_res[col_name].round(3)

    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"processing_metrics", "a") as file:
        file.write("\n\n")
        file.write("_"*100)
        file.write("\n\nINTERSECTIONAL SUBGROUPS DETAILED RATES\n\n")
        df_res.to_markdown(file)

    return df_res


def process_metrics(grouped_ds : GroupedProcessedDatasets, split_ds : SplitDataset) -> None:
    # sanity test to check if preprocessing methods worked in some way.
    # does not work with disparate impact remover because this method does not alter
    # Y.
    _spddi(grouped_ds, split_ds)
    _w_distance(grouped_ds, split_ds)
    _mutual_information(grouped_ds, split_ds)
    #_intersectional_spd(grouped_ds, split_ds)


