
from src.configs import (
        PRIVILEGED_GROUP,
        UNPRIVILEGED_GROUP,
        PROTECTED_ATTRIBUTES,
        TARGET,
        FAVORABLE_OUTCOME,
        GroupedProcessedDatasets,
        ProcessedDataset,
        SplitDataset
        )

from aif360.datasets import BinaryLabelDataset
from aif360.algorithms.preprocessing.optim_preproc_helpers.opt_tools import OptTools
from aif360.algorithms.preprocessing import (
    DisparateImpactRemover,
    LFR,
    OptimPreproc,
    Reweighing,
)
from pandas import cut


def _reweighing(ds : SplitDataset) -> ProcessedDataset:

    ds_copy_train = ds.train.copy(deepcopy=True)
    ds_copy_test = ds.test.copy(deepcopy=True)
    ds_copy_validation = ds.validation.copy(deepcopy=True)

    preprocess = Reweighing(
            privileged_groups=PRIVILEGED_GROUP,
            unprivileged_groups=UNPRIVILEGED_GROUP
            )
    preprocess.fit(ds_copy_train)
    transformed_train = preprocess.transform(ds_copy_train)
    transformed_test = preprocess.transform(ds_copy_test)
    transformed_validation = preprocess.transform(ds_copy_validation)

    return ProcessedDataset(
            preprocess,
            transformed_train,
            transformed_test,
            transformed_validation
            )


def _disparate_impact_remover(ds : SplitDataset, **kwargs) -> ProcessedDataset:

    ds_copy_train = ds.train.copy(deepcopy=True)
    ds_copy_test = ds.test.copy(deepcopy=True)
    ds_copy_validation = ds.validation.copy(deepcopy=True)

    preprocess = DisparateImpactRemover(
        repair_level=kwargs.get("repair_level", 1.0),
        sensitive_attribute=PROTECTED_ATTRIBUTES[0],
    )
    preprocess.fit(ds_copy_train)
    transformed_train = preprocess.fit_transform(ds_copy_train)
    transformed_test = preprocess.fit_transform(ds_copy_test)
    transformed_validation = preprocess.fit_transform(ds_copy_validation)

    return ProcessedDataset(
            preprocess,
            transformed_train,
            transformed_test,
            transformed_validation
            )


def _learning_fair_representations(ds : SplitDataset, **kwargs) -> ProcessedDataset:

    ds_copy_train = ds.train.copy(deepcopy=True)
    ds_copy_test = ds.test.copy(deepcopy=True)
    ds_copy_validation = ds.validation.copy(deepcopy=True)
    preprocess = LFR(
            unprivileged_groups=[{"race" : list([g["race"] for g in UNPRIVILEGED_GROUP])}],
        privileged_groups=[{"race" : list([g["race"] for g in PRIVILEGED_GROUP])}],
        k=kwargs.get("k", 15),
        Ax=kwargs.get("Ax", 0.5),
        Ay=kwargs.get("Ay", 10.0),
        Az=kwargs.get("Az", 0.01),
        verbose=kwargs.get("verbose", False),
        seed=kwargs.get("seed", 4),
    )
    preprocess.fit(ds_copy_train)
    transformed_train = preprocess.transform(ds_copy_train)
    transformed_test = preprocess.transform(ds_copy_test)
    transformed_validation = preprocess.transform(ds_copy_validation)

    return ProcessedDataset(
            preprocess,
            transformed_train,
            transformed_test,
            transformed_validation
            )


# def _optimized_preprocessing(ds : BinaryLabelDataset, training : bool,
#                              continuous : list[str], **kwargs) -> ProcessedDataset:
# 
#     def distortion(vold, vnew):
#         # HAMMING DISTANCE
#         return sum(1.0 for key in vold if vold[key] != vnew[key])
# 
#         # WEIGHTED DISTANCE
#         # # 1. Defina quais colunas NUNCA podem ser alteradas pelo otimizador
#         # # Alterar essas colunas quebraria a lógica do negócio ou geraria dados impossíveis
#         # colunas_imutaveis = ['race', 'sex', 'age_cat'] 
#         # 
#         # for col in colunas_imutaveis:
#         #     if col in vold and vold[col] != vnew[col]:
#         #         return 10000.0  # Custo proibitivo (bloqueia a transformação)
# 
#         # # 2. Defina pesos de importância para as colunas que PODEM ser alteradas
#         # # Valores maiores significam que você quer proteger mais aquela coluna contra mudanças
#         # pesos_atributos = {
#         #     'credit_history': 3.0,  # Mudar o histórico de crédito é muito severo
#         #     'employment_stat': 2.0, # Mudar o status de emprego é moderado
#         #     'housing': 1.0,         # Mudar o tipo de moradia tem menor impacto
#         # }
#         # 
#         # custo_total = 0.0
#         # 
#         # # 3. Calcula o custo ponderado das mudanças
#         # for key in vold:
#         #     if vold[key] != vnew[key]:
#         #         # Se a coluna tiver um peso definido, usa ele; se não, usa o padrão 1.0
#         #         peso = pesos_atributos.get(key, 1.0)
#         #         custo_total += peso
#         #         
#         # return custo_totald[key] != vnew[key])
# 
#     ds_copy = ds.copy(deepcopy=True)
#     df, _ = ds_copy.convert_to_dataframe()
#     for c in continuous:
#         df[c] = cut(df[c], bins=kwargs.get("bins", 5), labels=False)
#     ds_copy = BinaryLabelDataset(
#         df=df,
#         label_names=[TARGET],
#         favorable_label=FAVORABLE_OUTCOME,
#         protected_attribute_names=PROTECTED_ATTRIBUTES
#         )
# 
#     preprocess = OptimPreproc(
#             optimizer=OptTools,
#             optim_options={
#                 "distortion_fun": distortion,
#                 "epsilon" : kwargs.get("epsilon", 0.05),
#                 "clist" : kwargs.get("clist", [0.99, 1.99, 2.99]),
#                 "dlist" : kwargs.get("dlist", [0.1, 0.05, 0.0]),
#                 },
#             unprivileged_groups=UNPRIVILEGED_GROUP,
#             privileged_groups=PRIVILEGED_GROUP,
#             verbose=kwargs.get("verbose", False),
#             seed=kwargs.get("seed", 4),
#             )
#     preprocess.fit(ds_copy)
#     transformed = preprocess.transform(ds_copy) if training else None
# 
#     return ProcessedDataset(
#             preprocess,
#             transformed
#             )


def process(ds : SplitDataset, continuous : list[str], **kwargs) -> GroupedProcessedDatasets:

    return GroupedProcessedDatasets(
            reweighing=_reweighing(ds),
            disparate_impact_remover=_disparate_impact_remover(ds, **kwargs),
            learning_fair_representations=_learning_fair_representations(ds, **kwargs),
            optimized_preprocessing=None#_optimized_preprocessing(ds, training, continuous, **kwargs),
            )

