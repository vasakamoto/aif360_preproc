
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


def _reweighing(ds : BinaryLabelDataset, training : bool) -> ProcessedDataset:

    ds_copy = ds.copy(deepcopy=True)
    preprocess = Reweighing(
            privileged_groups=PRIVILEGED_GROUP,
            unprivileged_groups=UNPRIVILEGED_GROUP
            )
    preprocess.fit(ds_copy)
    transformed = preprocess.transform(ds_copy) if training else None

    return ProcessedDataset(
            preprocess,
            transformed
            )


def _disparate_impact_remover(ds : BinaryLabelDataset, training : bool, **kwargs) -> ProcessedDataset:

    ds_copy = ds.copy(deepcopy=True)
    preprocess = DisparateImpactRemover(
        repair_level=getattr(kwargs, "repair_level", 1.0),
        sensitive_attribute=PROTECTED_ATTRIBUTES[0],
    )
    preprocess.fit(ds_copy)
    transformed = preprocess.fit_transform(ds_copy) if training else None

    return ProcessedDataset(
            preprocess,
            transformed
            )


def _learning_fair_representations(ds : BinaryLabelDataset, training : bool, **kwargs) -> ProcessedDataset:

    ds_copy = ds.copy(deepcopy=True)
    preprocess = LFR(
            unprivileged_groups=[{"race" : list([g["race"] for g in UNPRIVILEGED_GROUP])}],
        privileged_groups=[{"race" : list([g["race"] for g in PRIVILEGED_GROUP])}],
        k=getattr(kwargs, "k", 5),
        Ax=getattr(kwargs, "Ax", 0.1),
        Ay=getattr(kwargs, "Ay", 1.0),
        Az=getattr(kwargs, "Az", 50.0),
        verbose=getattr(kwargs, "verbose", False),
        seed=getattr(kwargs, "seed", 4),
    )
    preprocess.fit(ds_copy)
    transformed = preprocess.transform(ds_copy) if training else None

    return ProcessedDataset(
            preprocess,
            transformed
            )


def _optimized_preprocessing(ds : BinaryLabelDataset, training : bool,
                             continuous : list[str], **kwargs) -> ProcessedDataset:

    def distortion(vold, vnew):
        # HAMMING DISTANCE
        return sum(1.0 for key in vold if vold[key] != vnew[key])

        # WEIGHTED DISTANCE
        # # 1. Defina quais colunas NUNCA podem ser alteradas pelo otimizador
        # # Alterar essas colunas quebraria a lógica do negócio ou geraria dados impossíveis
        # colunas_imutaveis = ['race', 'sex', 'age_cat'] 
        # 
        # for col in colunas_imutaveis:
        #     if col in vold and vold[col] != vnew[col]:
        #         return 10000.0  # Custo proibitivo (bloqueia a transformação)

        # # 2. Defina pesos de importância para as colunas que PODEM ser alteradas
        # # Valores maiores significam que você quer proteger mais aquela coluna contra mudanças
        # pesos_atributos = {
        #     'credit_history': 3.0,  # Mudar o histórico de crédito é muito severo
        #     'employment_stat': 2.0, # Mudar o status de emprego é moderado
        #     'housing': 1.0,         # Mudar o tipo de moradia tem menor impacto
        # }
        # 
        # custo_total = 0.0
        # 
        # # 3. Calcula o custo ponderado das mudanças
        # for key in vold:
        #     if vold[key] != vnew[key]:
        #         # Se a coluna tiver um peso definido, usa ele; se não, usa o padrão 1.0
        #         peso = pesos_atributos.get(key, 1.0)
        #         custo_total += peso
        #         
        # return custo_totald[key] != vnew[key])

    ds_copy = ds.copy(deepcopy=True)
    df, _ = ds_copy.convert_to_dataframe()
    for c in continuous:
        df[c] = cut(df[c], bins=getattr(kwargs, "bins", 5), labels=False)
    ds_copy = BinaryLabelDataset(
        df=df,
        label_names=[TARGET],
        favorable_label=FAVORABLE_OUTCOME,
        protected_attribute_names=PROTECTED_ATTRIBUTES
        )

    preprocess = OptimPreproc(
            optimizer=OptTools,
            optim_options={
                "distortion_fun": distortion,
                "epsilon" : getattr(kwargs, "epsilon", 0.05),
                "clist" : getattr(kwargs, "clist", [0.99, 1.99, 2.99]),
                "dlist" : getattr(kwargs, "dlist", [0.1, 0.05, 0.0]),
                },
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP,
            verbose=getattr(kwargs, "verbose", False),
            seed=getattr(kwargs, "seed", 4),
            )
    preprocess.fit(ds_copy)
    transformed = preprocess.transform(ds_copy) if training else None

    return ProcessedDataset(
            preprocess,
            transformed
            )


def _process(ds : BinaryLabelDataset, training : bool, continuous : list[str], **kwargs) -> GroupedProcessedDatasets:

    return GroupedProcessedDatasets(
            reweighing=_reweighing(ds, training),
            disparate_impact_remover=_disparate_impact_remover(ds, training, **kwargs),
            learning_fair_representations=_learning_fair_representations(ds, training, **kwargs),
            optimized_preprocessing=None#_optimized_preprocessing(ds, training, continuous, **kwargs),
            )

def preprocess(split_ds : SplitDataset) -> None:

    continuous_feat = ["lsat", "zgpa"]
    split_ds.processed_train = _process(split_ds.train, True, continuous_feat)
    split_ds.processed_test = _process(split_ds.test, False, continuous_feat)
    split_ds.processed_validation = _process(split_ds.validation, False, continuous_feat)

