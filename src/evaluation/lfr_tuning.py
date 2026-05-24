
from itertools import product

from aif360.algorithms.preprocessing import LFR
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
        roc_auc_score,
        accuracy_score
        )
from numpy import (
        isnan,
        nan
        )
from pandas import DataFrame

from src.configs import (
        PRIVILEGED_GROUP,
        UNPRIVILEGED_GROUP,
        SplitDataset,
        PATH_ROOT
        )


def lfr_exploration(split_ds : SplitDataset) -> DataFrame:

    train_ds = split_ds.train.copy(deepcopy=True)
    test_ds = split_ds.test.copy(deepcopy=True)

    k_options = [5, 7, 10, 12, 15, 17, 20, 22, 25]
    ax_options = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    az_options = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    ay_options = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    
    records = []
    
    for k, ax, az, ay in product(k_options, ax_options, az_options, ay_options):
        
        lfr = LFR(
            unprivileged_groups=[{"race" : list([g["race"] for g in UNPRIVILEGED_GROUP])}],
            privileged_groups=[{"race" : list([g["race"] for g in PRIVILEGED_GROUP])}],
            k=k, Ax=ax, Az=az, Ay=ay,
            verbose=0
        )
        
        try:
            lfr_model = lfr.fit(train_ds)
            trans_train = lfr_model.transform(train_ds)
            trans_test = lfr_model.transform(test_ds)
            
            if isnan(trans_train.features).any():
                records.append({"k": k, "Ax": ax, "Az": az, "Ay": ay, "Status": "NaN_Propagation", "Test_AUC": nan})
                continue
                
            rf = RandomForestClassifier(random_state=42)
            rf.fit(trans_train.features, train_ds.labels.ravel())
            
            preds = rf.predict_proba(trans_test.features)[:, 1]
            auc = roc_auc_score(test_ds.labels.ravel(), preds)
            acc = accuracy_score(test_ds.labels.ravel(), rf.predict(trans_test.features))
            
            records.append({
                "k": k, "Ax": ax, "Az": az, "Ay": ay, 
                "Status": "Success", "Test_Accuracy": acc, "Test_AUC": auc
            })
            
        except Exception as e:
            records.append({"k": k, "Ax": ax, "Az": az, "Ay": ay, "Status": f"Solver_Error: {type(e).__name__}", "Test_AUC": nan})
            
    d = DataFrame(records)
    with open(PATH_ROOT/"results"/"tables"/"evaluation.md", "a") as file:
        file.write("\n\nLFR hyperparameter exploration\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

    return d
