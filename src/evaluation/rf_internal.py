
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


def _feature_importance_(models : TrainedModels, split_ds : SplitDataset) -> DataFrame:

    d = {"features" : split_ds.train.feature_names}

    for model in fields(models):
        d.update({model.name : getattr(models, model.name).feature_importances_})
    
    d = DataFrame(d)
    with open(PATH_ROOT/"results"/"tables"/"evaluation.md", "a") as file:
        file.write("\n\nFEATURE IMPORTANCES\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return d


def _unwrap_bld(dataset: BinaryLabelDataset) -> tuple[DataFrame, np.ndarray, np.ndarray]:

    X_df = DataFrame(dataset.features, columns=dataset.feature_names)
    y_arr = dataset.labels.ravel()
    w_arr = dataset.instance_weights.ravel()
    return X_df, y_arr, w_arr


def _delta_auc_metrics(trained_models: TrainedModels, processed_groups: GroupedProcessedDatasets,
                       raw_dataset: SplitDataset) -> DataFrame:
    
    df_meta = DataFrame(raw_dataset.test.features, columns=raw_dataset.test.feature_names)
    subgroups = df_meta["race"].astype(int).astype(str) + "_" + df_meta["fam_inc"].astype(int).astype(str)
    unique_subgroups = subgroups.unique()
    
    execution_matrix = {
        "Baseline": (trained_models.raw, raw_dataset.test),
        "Reweighing": (trained_models.reweighing, raw_dataset.test),
        "DIR": (trained_models.disparate_impact_remover, processed_groups.disparate_impact_remover.transformed_test)
    }
    
    if trained_models.learning_fair_representations and processed_groups.learning_fair_representations:
        execution_matrix["LFR"] = (trained_models.learning_fair_representations, processed_groups.learning_fair_representations.transformed_test)
        
    auc_summary = {}
    
    for scenario, (model, bld_test) in execution_matrix.items():
        if model is None or bld_test is None:
            continue
            
        X_test, y_test, _ = _unwrap_bld(bld_test)
        preds = model.predict_proba(X_test)[:, 1]
        
        auc_global = roc_auc_score(y_test, preds)
        
        subgroup_aucs = []
        for g in unique_subgroups:
            mask = (subgroups == g).values
            if len(np.unique(y_test[mask])) == 2 and np.sum(mask) > 10:
                subgroup_aucs.append(roc_auc_score(y_test[mask], preds[mask]))
                
        delta_auc_inter = (max(subgroup_aucs) - min(subgroup_aucs)) if subgroup_aucs else np.nan
        
        auc_summary[scenario] = {
            "AUC_Global": auc_global,
            "Delta_AUC_Interseccional": delta_auc_inter
        }
        
    df_auc = DataFrame(auc_summary).T
    df_auc["Delta_AUC_Global_Loss"] = df_auc["AUC_Global"].loc["Baseline"] - df_auc["AUC_Global"]
    
    with open(PATH_ROOT/"results"/"tables"/"evaluation.md", "a") as file:
        file.write("\n\nDelta_AUC_Global_Loss\n\n")
        df_auc.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)
    return df_auc


def _spaces_adversarial_accuracy(raw_dataset: SplitDataset,
                                 processed_groups: GroupedProcessedDatasets) -> DataFrame:
    
    X_train_raw, _, _ = _unwrap_bld(raw_dataset.train)
    X_test_raw, _, _ = _unwrap_bld(raw_dataset.test)
    
    race_train = X_train_raw["race"].astype(int).values
    race_test = X_test_raw["race"].astype(int).values
    
    majority_baseline = Series(race_test).value_counts(normalize=True).max()
    
    spaces_to_audit = {
        "Baseline Space": (raw_dataset.train, raw_dataset.test),
        "DIR Space": (processed_groups.disparate_impact_remover.transformed_train, 
                      processed_groups.disparate_impact_remover.transformed_test)
    }
    
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
    with open(PATH_ROOT/"results"/"tables"/"evaluation.md", "a") as file:
        file.write("\n\nAdversarial_Accuracy\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)
    return d


def rf_metrics(t : TrainedModels, g : GroupedProcessedDatasets, s : SplitDataset):
    _feature_importance_(t, s)
    _delta_auc_metrics(t, g, s)
    _spaces_adversarial_accuracy(s, g)
