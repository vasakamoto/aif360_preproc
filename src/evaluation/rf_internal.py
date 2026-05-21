
from dataclasses import fields
from aif360.datasets import BinaryLabelDataset
import numpy as np
from pandas import DataFrame, Series
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
        accuracy_score,
        roc_auc_score
        )
from sklearn.preprocessing import StandardScaler

from src.configs import (
        SplitDataset,
        TrainedModels,
        GroupedProcessedDatasets,
        PATH_ROOT
        )

# [ ] RANDOM FOREST INTERNAL & ADVANCED ROBUSTNESS
#     [ ] FEATURE IMPORTANCE SHIFT (Permutation Importance stability)
#     [ ] ADVERSARIAL ACCURACY (Can a shadow model predict 'A' from 'Y_hat'?)
#     [ ] DELTA AUC (Threshold-invariant performance gap)


def _feature_importance_(models : TrainedModels, split_ds : SplitDataset) -> DataFrame:

    d = {"features" : split_ds.train.feature_names}

    for model in fields(models):
        d.update({model.name : getattr(models, model.name).feature_importances_})
    
    d = DataFrame(d)
    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"rf_metrics", "w") as file:
        file.write("FEATURE IMPORTANCES\n\n")
        d.to_markdown(file)

    return d


def _delta_auc_metrics(trained_models: TrainedModels,
                       raw_dataset: SplitDataset,
                       grouped_ds: GroupedProcessedDatasets) -> DataFrame:

    df_meta = DataFrame(raw_dataset.test.features, columns=raw_dataset.test.feature_names)
    subgroups = df_meta["race"].astype(int).astype(str) + "_" + df_meta["fam_inc"].astype(int).astype(str)
    unique_subgroups = subgroups.unique()
    
    # Mapeamento estruturado cruzando (Cenário, Modelo, Dataset de Teste Específico)
    execution_matrix = {
        "Baseline": (trained_models.raw, raw_dataset.test),
        "Reweighing": (trained_models.reweighing, raw_dataset.test),
        "DIR": (trained_models.disparate_impact_remover, grouped_ds.disparate_impact_remover.transformed_test)
    }
        
    auc_summary = {}
    
    for scenario, (model, bld_test) in execution_matrix.items():
        if model is None or bld_test is None:
            continue
            
        X_test, y_test, _ = _unwrap_bld(bld_test)
        preds = model.predict_proba(X_test)[:, 1]
        
        # 1. AUC Global
        auc_global = roc_auc_score(y_test, preds)
        
        # 2. AUC Interseccional por Célula Amostral
        subgroup_aucs = []
        for g in unique_subgroups:
            mask = (subgroups == g).values
            # Filtro defensivo para desbalanceamento crítico (N > 10 e presença de ambas as classes)
            if len(np.unique(y_test[mask])) == 2 and np.sum(mask) > 10:
                subgroup_aucs.append(roc_auc_score(y_test[mask], preds[mask]))
                
        delta_auc_inter = (max(subgroup_aucs) - min(subgroup_aucs)) if subgroup_aucs else np.nan
        
        auc_summary[scenario] = {
            "AUC_Global": auc_global,
            "Delta_AUC_Interseccional": delta_auc_inter
        }
        
    df_auc = DataFrame(auc_summary).T
    # Diferença de performance em relação ao baseline de utilidade
    df_auc["Delta_AUC_Global_Loss"] = df_auc["AUC_Global"].loc["Baseline"] - df_auc["AUC_Global"]
    
    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"rf_metrics", "a") as file:
        file.write("\n\n")
        file.write("_"*100)
        file.write("\n\nDelta_AUC_Global_Loss\n\n")
        df_auc.to_markdown(file)
    return df_auc


#def evaluate_adversarial_accuracy(X_train_base, X_test_base, X_train_dir, X_test_dir, race_train, race_test):
#    """
#    Avalia a capacidade de um classificador adversário reconstruir a variável de raça.
#    """
#    # Proporção do grupo majoritário no teste (Zero-Rule Classifier baseline)
#    majority_baseline = race_test.value_counts(normalize=True).max()
#    print(f"Frequência Base do Grupo Majoritário (Acurácia Dummy): {majority_baseline:.4f}\n")
#    
#    adv_results = {}
#    
#    scenarios = {
#        'Baseline Space': (X_train_base, X_test_base),
#        'DIR Transformed Space': (X_train_dir, X_test_dir)
#    }
#    
#    for name, (X_tr, X_te) in scenarios.items():
#        # Normalização rigorosa para convergência do modelo adversário linear
#        scaler = StandardScaler()
#        X_tr_scaled = scaler.fit_transform(X_tr)
#        X_te_scaled = scaler.transform(X_te)
#        
#        # Modelo adversário focado em decodificar a informação protegida
#        adversary = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs', random_state=42)
#        adversary.fit(X_tr_scaled, race_train)
#        
#        adv_preds = adversary.predict(X_te_scaled)
#        acc = accuracy_score(race_test, adv_preds)
#        
#        adv_results[name] = {
#            'Adversarial_Accuracy': acc,
#            'Information_Leakage_Above_Baseline': acc - majority_baseline
#        }
#        
#    return DataFrame(adv_results).T

# Nota: O cenário 'Reweighing' compartilha do mesmo espaço físico de características do Baseline, 
# contudo o seu teste adversário direto exige um classificador treinado com os pesos inversos 
# sobre as variáveis preditivas para verificar se a distribuição de pesos confunde a separabilidade linear.
def _unwrap_bld(dataset: BinaryLabelDataset) -> tuple[DataFrame, np.ndarray, np.ndarray]:
    """Extrai (X_dataframe, y_array, weights_array) de um BinaryLabelDataset."""
    X_df = DataFrame(dataset.features, columns=dataset.feature_names)
    y_arr = dataset.labels.ravel()
    w_arr = dataset.instance_weights.ravel()
    return X_df, y_arr, w_arr
def evaluate_spaces_adversarial_accuracy(
    raw_dataset: SplitDataset,
    processed_groups: GroupedProcessedDatasets
) -> DataFrame: """Mapeia o vazamento de informação sensível (race) nos diferentes espaços gerados."""
    
    # Extração dos targets adversários (variável sensível race)
    X_train_raw, _, _ = _unwrap_bld(raw_dataset.train)
    X_test_raw, _, _ = _unwrap_bld(raw_dataset.test)
    
    race_train = X_train_raw["race"].astype(int).values
    race_test = X_test_raw["race"].astype(int).values
    
    majority_baseline = Series(race_test).value_counts(normalize=True).max()
    print(f"Frequência Base do Grupo Majoritário (Dummy Threshold): {majority_baseline:.4f}\n")
    
    # Dicionário de espaços vetoriais a auditar
    spaces_to_audit = {
        "Baseline Space": (raw_dataset.train, raw_dataset.test),
        "DIR Space": (processed_groups.disparate_impact_remover.transformed_train, 
                      processed_groups.disparate_impact_remover.transformed_test)
    }
    
    # Inclui LFR se o objeto interno não contiver falhas numéricas
    if processed_groups.learning_fair_representations:
        spaces_to_audit["LFR Space"] = (processed_groups.learning_fair_representations.transformed_train,
                                        processed_groups.learning_fair_representations.transformed_test)
        
    adv_results = {}
    
    for space_name, (bld_train, bld_test) in spaces_to_audit.items():
        if bld_train is None or bld_test is None:
            continue
            
        X_tr, _, _ = _unwrap_bld(bld_train)
        X_te, _, _ = _unwrap_bld(bld_test)
        
        # Padronização para convergência estável do solucionador do classificador adversário
        scaler = StandardScaler()
        X_tr_scaled = scaler.fit_transform(X_tr)
        X_te_scaled = scaler.transform(X_te)
        
        adversary = LogisticRegression(max_iter=1000, solver="lbfgs", random_state=42)
        adversary.fit(X_tr_scaled, race_train)
        
        acc = accuracy_score(race_test, adversary.predict(X_te_scaled))
        
        adv_results[space_name] = {
            "Adversarial_Accuracy": acc,
            "Information_Leakage_Above_Baseline": acc - majority_baseline
        }
        
    d = DataFrame(adv_results).T
    with open(PATH_ROOT/"results"/"tables"/"evaluation"/"rf_metrics", "a") as file:
        file.write("\n\n")
        file.write("_"*100)
        file.write("\n\nAdversarial_Accuracy\n\n")
        d.to_markdown(file)
    return d

def rf_metrics(t : TrainedModels, g : GroupedProcessedDatasets, s : SplitDataset):
    #_feature_importance_(t, s)
    _delta_auc_metrics(t, g, s)
    #evaluate_spaces_adversarial_accuracy(s, g)
