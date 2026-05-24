
from dataclasses import dataclass
from pathlib import Path

from pandas import read_csv
from aif360.algorithms import Transformer
from aif360.datasets import BinaryLabelDataset
from sklearn.ensemble import RandomForestClassifier


PATH_ROOT = Path(__file__).parent.parent

PROTECTED_ATTRIBUTES  = ["race"]
PRIVILEGED_GROUP = [
        {"race" : 2},
        {"race" : 7},
        ]
UNPRIVILEGED_GROUP = [
        {"race" : 0},
        {"race" : 1},
        {"race" : 3},
        {"race" : 4},
        {"race" : 5},
        {"race" : 6},
        {"race" : 8},
        ]
TARGET = "pass_bar"
FAVORABLE_OUTCOME = 1

DATASET = read_csv(PATH_ROOT / "dataset/bar_pass_prediction.csv")

SELECTED_COLUMNS = ["zgpa", "lsat", "race", "tier", "fam_inc", "pass_bar"]
SELECTED_QUANT = ["zgpa", "lsat"]
SELECTED_QUALI = ["race", "tier", "fam_inc"]

# YEAH, IT WOULD BE GREAT TO SEPARATE MODELS FROM OTHER KEY CONFIGS, BUT... I THOUGHT
# IT WOULD BE CONFUSING
@dataclass
class SplitDataset:
    train                   : BinaryLabelDataset
    test                    : BinaryLabelDataset
    validation              : BinaryLabelDataset

@dataclass
class ProcessedDataset:
    preprocess_model        : Transformer
    transformed_train       : BinaryLabelDataset
    transformed_test        : BinaryLabelDataset
    transformed_validation  : BinaryLabelDataset

@dataclass
class GroupedProcessedDatasets:
    reweighing                      : ProcessedDataset
    disparate_impact_remover        : ProcessedDataset
    learning_fair_representations   : ProcessedDataset
    optimized_preprocessing         : ProcessedDataset | None

@dataclass
class TrainedModels:
    raw                             : RandomForestClassifier
    reweighing                      : RandomForestClassifier
    disparate_impact_remover        : RandomForestClassifier
    learning_fair_representations   : RandomForestClassifier
