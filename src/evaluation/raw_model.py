

from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from numpy import mean
from pandas import DataFrame, col, concat
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
        accuracy_score,
        f1_score,
        recall_score,
        precision_score,
        roc_auc_score,
        confusion_matrix,
        )
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

from src.configs import (
        SplitDataset,
        DATASET,
        TARGET,
        FAVORABLE_OUTCOME,
        PROTECTED_ATTRIBUTES,
        PRIVILEGED_GROUP,
        UNPRIVILEGED_GROUP,
        PATH_ROOT
        )


def _all_features(df : DataFrame) -> dict:

    df = df.dropna()
    df.drop(columns=[
        "bar",
        "gender",
        "grad",
        "indxgrp",
        "indxgrp2",
        "race1",
        "race2",
        "ID",
        "bar1",
        "bar2",
        "Dropout",
        "bar_passed",
        "dnn_bar_pass_prediction"
        ],
            inplace=True
            )
    df_train, df_test = train_test_split(df, test_size=0.4, random_state=42)
    df_valid, df_test = train_test_split(df_test, test_size=0.9, random_state=42)
    model = RandomForestClassifier(
            n_estimators=100,
            min_samples_split=2,
            min_samples_leaf=2,
            max_features="sqrt",
            max_depth=5,
            random_state=42,
            )

    ds_train = BinaryLabelDataset(
            df=df_train,
            label_names=[TARGET],
            favorable_label=FAVORABLE_OUTCOME,
            protected_attribute_names=PROTECTED_ATTRIBUTES
            )
    ds_test=BinaryLabelDataset(
            df=df_test,
            label_names=[TARGET],
            favorable_label=FAVORABLE_OUTCOME,
            protected_attribute_names=PROTECTED_ATTRIBUTES
            )
    ds_validation=BinaryLabelDataset(
            df=df_valid,
            label_names=[TARGET],
            favorable_label=FAVORABLE_OUTCOME,
            protected_attribute_names=PROTECTED_ATTRIBUTES
            )

    X_training = ds_train.features
    X_test = ds_test.features
    X_validation = ds_validation.features

    y_training = ds_train.labels.ravel()
    y_test = ds_test.labels.ravel()
    y_validation = ds_validation.labels.ravel()

    model.fit(X_training, y_training)

    y_pred_test = model.predict(X_test)
    y_pred_validation = model.predict(X_validation)

    y_prob_test = model.predict_proba(X_test)[:, 1]
    y_prob_validation = model.predict_proba(X_validation)[:, 1]

    metrics_std = {
            "test_baseline_accuracy" : round(max(mean(y_test == 1), mean(y_test == 0)), 3),
            "test_accuracy" : round(accuracy_score(y_test, y_pred_test), 3),
            "test_precision" : round(precision_score(y_test, y_pred_test, pos_label=1), 3),
            "test_recall" : round(recall_score(y_test, y_pred_test, pos_label=1), 3),
            "test_f1" : round(f1_score(y_test, y_pred_test, pos_label=1), 3),
            "test_roc_auc" : round(roc_auc_score(y_test, y_prob_test), 3),
            "test_confusion_matrix" : confusion_matrix(y_test, y_pred_test),
            "validation_baseline_accuracy" : round(max(mean(y_validation == 1), mean(y_validation == 0)), 3),
            "validation_accuracy" : round(accuracy_score(y_validation, y_pred_validation), 3),
            "validation_precision" : round(precision_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_recall" : round(recall_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_f1" : round(f1_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_roc_auc" : round(roc_auc_score(y_validation, y_prob_validation), 3),
            "validation_confusion_matrix" : confusion_matrix(y_validation, y_pred_validation),
            }

    pred_ds = ds_test.copy(deepcopy=True)
    pred_ds.labels = y_pred_test.reshape(-1, 1)

    cm = ClassificationMetric(
            ds_test,
            pred_ds,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP,
            )

    metrics_fair = {
            "statistical_parity_difference": round(cm.statistical_parity_difference(), 3),
            "disparate_impact": round(cm.disparate_impact(), 3),
            "equal_opportunity_difference": round(cm.equal_opportunity_difference(), 3),
            "average_odds_difference": round(cm.average_odds_difference(), 3),
            "false_positive_rate_diff": round(cm.false_positive_rate_difference(), 3),
            "false_discovery_rate_diff": round(cm.false_discovery_rate_difference(), 3),
            }

    feature_importance = DataFrame({
            "features" : ds_test.feature_names,
            "feature_importance" : model.feature_importances_
            })

    return {
            **metrics_std,
            **metrics_fair,
            "feature_importance" : feature_importance
            }


def _without_protection(split_ds : SplitDataset) -> dict:

    model = RandomForestClassifier(
            n_estimators=100,
            min_samples_split=2,
            min_samples_leaf=2,
            max_features="sqrt",
            max_depth=5,
            random_state=42,
            )
    unprotected_features = [
            i for i, name in enumerate(split_ds.train.feature_names) 
            if name not in ["male", "race", "fam_inc", "tier"]
            ]

    X_training = split_ds.train.features[:, unprotected_features]
    X_test = split_ds.test.features[:, unprotected_features]
    X_validation = split_ds.validation.features[:, unprotected_features]

    y_training = split_ds.train.labels.ravel()
    y_test = split_ds.test.labels.ravel()
    y_validation = split_ds.validation.labels.ravel()

    model.fit(X_training, y_training)

    y_pred_test = model.predict(X_test)
    y_pred_validation = model.predict(X_validation)

    y_prob_test = model.predict_proba(X_test)[:, 1]
    y_prob_validation = model.predict_proba(X_validation)[:, 1]

    metrics_std = {
            "test_baseline_accuracy" : round(max(mean(y_test == 1), mean(y_test == 0)), 3),
            "test_accuracy" : round(accuracy_score(y_test, y_pred_test), 3),
            "test_precision" : round(precision_score(y_test, y_pred_test, pos_label=1), 3),
            "test_recall" : round(recall_score(y_test, y_pred_test, pos_label=1), 3),
            "test_f1" : round(f1_score(y_test, y_pred_test, pos_label=1), 3),
            "test_roc_auc" : round(roc_auc_score(y_test, y_prob_test), 3),
            "test_confusion_matrix" : confusion_matrix(y_test, y_pred_test),
            "validation_baseline_accuracy" : round(max(mean(y_validation == 1), mean(y_validation == 0)), 3),
            "validation_accuracy" : round(accuracy_score(y_validation, y_pred_validation), 3),
            "validation_precision" : round(precision_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_recall" : round(recall_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_f1" : round(f1_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_roc_auc" : round(roc_auc_score(y_validation, y_prob_validation), 3),
            "validation_confusion_matrix" : confusion_matrix(y_validation, y_pred_validation),
            }

    pred_ds = split_ds.test.copy(deepcopy=True)
    pred_ds.labels = y_pred_test.reshape(-1, 1)

    cm = ClassificationMetric(
            split_ds.test,
            pred_ds,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP,
            )

    metrics_fair = {
            "statistical_parity_difference": round(cm.statistical_parity_difference(), 3),
            "disparate_impact": round(cm.disparate_impact(), 3),
            "equal_opportunity_difference": round(cm.equal_opportunity_difference(), 3),
            "average_odds_difference": round(cm.average_odds_difference(), 3),
            "false_positive_rate_diff": round(cm.false_positive_rate_difference(), 3),
            "false_discovery_rate_diff": round(cm.false_discovery_rate_difference(), 3),
            }

    feature_importance = DataFrame({
            "features" : [
            name for i, name in enumerate(split_ds.train.feature_names) 
            if name not in ["male", "race", "fam_inc", "tier"]
            ],
            "feature_importance" : model.feature_importances_
            })

    return {
            **metrics_std,
            **metrics_fair,
            "feature_importance" : feature_importance
            }


def _without_race(split_ds : SplitDataset) -> dict:
    model = RandomForestClassifier(
            n_estimators=100,
            min_samples_split=2,
            min_samples_leaf=2,
            max_features="sqrt",
            max_depth=5,
            random_state=42,
            )
    unprotected_features = [
            i for i, name in enumerate(split_ds.train.feature_names) 
            if name not in ["race"]
            ]

    X_training = split_ds.train.features[:, unprotected_features]
    X_test = split_ds.test.features[:, unprotected_features]
    X_validation = split_ds.validation.features[:, unprotected_features]

    y_training = split_ds.train.labels.ravel()
    y_test = split_ds.test.labels.ravel()
    y_validation = split_ds.validation.labels.ravel()

    model.fit(X_training, y_training)

    y_pred_test = model.predict(X_test)
    y_pred_validation = model.predict(X_validation)

    y_prob_test = model.predict_proba(X_test)[:, 1]
    y_prob_validation = model.predict_proba(X_validation)[:, 1]

    metrics_std = {
            "test_baseline_accuracy" : round(max(mean(y_test == 1), mean(y_test == 0)), 3),
            "test_accuracy" : round(accuracy_score(y_test, y_pred_test), 3),
            "test_precision" : round(precision_score(y_test, y_pred_test, pos_label=1), 3),
            "test_recall" : round(recall_score(y_test, y_pred_test, pos_label=1), 3),
            "test_f1" : round(f1_score(y_test, y_pred_test, pos_label=1), 3),
            "test_roc_auc" : round(roc_auc_score(y_test, y_prob_test), 3),
            "test_confusion_matrix" : confusion_matrix(y_test, y_pred_test),
            "validation_baseline_accuracy" : round(max(mean(y_validation == 1), mean(y_validation == 0)), 3),
            "validation_accuracy" : round(accuracy_score(y_validation, y_pred_validation), 3),
            "validation_precision" : round(precision_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_recall" : round(recall_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_f1" : round(f1_score(y_validation, y_pred_validation, pos_label=1), 3),
            "validation_roc_auc" : round(roc_auc_score(y_validation, y_prob_validation), 3),
            "validation_confusion_matrix" : confusion_matrix(y_validation, y_pred_validation),
            }

    pred_ds = split_ds.test.copy(deepcopy=True)
    pred_ds.labels = y_pred_test.reshape(-1, 1)

    cm = ClassificationMetric(
            split_ds.test,
            pred_ds,
            unprivileged_groups=UNPRIVILEGED_GROUP,
            privileged_groups=PRIVILEGED_GROUP,
            )

    metrics_fair = {
            "statistical_parity_difference": round(cm.statistical_parity_difference(), 3),
            "disparate_impact": round(cm.disparate_impact(), 3),
            "equal_opportunity_difference": round(cm.equal_opportunity_difference(), 3),
            "average_odds_difference": round(cm.average_odds_difference(), 3),
            "false_positive_rate_diff": round(cm.false_positive_rate_difference(), 3),
            "false_discovery_rate_diff": round(cm.false_discovery_rate_difference(), 3),
            }

    feature_importance = DataFrame({
            "features" : [
            name for i, name in enumerate(split_ds.train.feature_names) 
            if name not in ["race"]
            ],
            "feature_importance" : model.feature_importances_
            })

    return {
            **metrics_std,
            **metrics_fair,
            "feature_importance" : feature_importance
            }


def evaluate(df : DataFrame, s : SplitDataset) -> None:
    d = {
            "metrics" : [],
            "true_raw" : [],
            "without_protection" : [],
            "without_race" : [],
            }

    al = _all_features(df)
    wop = _without_protection(s)
    wor = _without_race(s)

    d["metrics"].extend([
        k for k in al.keys() 
        if k not in ["feature_importance", "validation_confusion_matrix", "test_confusion_matrix"]
        ])
    d["true_raw"].extend([
        al[k] for k in al.keys() 
        if k not in ["feature_importance", "validation_confusion_matrix", "test_confusion_matrix"]
        ])
    d["without_protection"].extend([
        wop[k] for k in wop.keys() 
        if k not in ["feature_importance", "validation_confusion_matrix", "test_confusion_matrix"]
        ])
    d["without_race"].extend([
        wor[k] for k in wor.keys() 
        if k not in ["feature_importance", "validation_confusion_matrix", "test_confusion_matrix"]
        ])

    def cm_to_df(cm) -> DataFrame:
        # [TN, FP]
        # [FN, TP]
        cm = {
                "/" : ["REAL NEGATIVE", "REAL POSITIVE"],
                "PREDICTED NEGATIVE" : [cm[0,0], cm[1,0]],
                "PREDICTED POSITIVE" : [cm[1,0], cm[1,1]]
                }

        return DataFrame(cm)


    d = DataFrame(d)

    with open(PATH_ROOT/"results"/"tables"/"raw_evaluation.md", "w") as file:
        file.write("\n\nTRUE RAW METRICS\n\n")
        d.to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        file.write("\n\nCONFUSION MATRIX RAW TRUE METRICS\n\n")
        cm_to_df(al["validation_confusion_matrix"]).to_markdown(file)
        file.write("\n\n")
        cm_to_df(al["test_confusion_matrix"]).to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        file.write("\n\nCONFUSION MATRIX WITHOUT PROTECTED ATTRIBUTES\n\n")
        cm_to_df(wop["validation_confusion_matrix"]).to_markdown(file)
        file.write("\n\n")
        cm_to_df(wop["test_confusion_matrix"]).to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        file.write("\n\nCONFUSION MATRIX WITHOUT RACE\n\n")
        cm_to_df(wor["validation_confusion_matrix"]).to_markdown(file)
        file.write("\n\n")
        cm_to_df(wor["test_confusion_matrix"]).to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        file.write("\n\nFEATURE IMPORTANCE TRUE RAW\n\n")
        al["feature_importance"].to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        file.write("\n\nCONFUSION MATRIX WITHOUT PROTECTED ATTRIBUTES\n\n")
        wop["feature_importance"].to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)

        file.write("\n\nCONFUSION MATRIX WITHOUT RACE\n\n")
        wor["feature_importance"].to_markdown(file)
        file.write("\n\n\n")
        file.write("_"*100)
    
    return
