
from pathlib import Path

from pandas import (
        read_csv,
        DataFrame
)


PATH_ROOT = Path(__file__).parent.parent

PROTECTED_ATTRIBUTES  = ["race"]#, "sex", "fam_inc"]
PRIVILEGED_GROUP = [{"race" : 1}]
UNPRIVILEGED_GROUP = [{"race" : 0}]
TARGET = "pass_bar"
FAVORABLE_OUTCOME = [1]

DATASET = read_csv(PATH_ROOT / "bar_pass_prediction/bar_pass_prediction.csv")

BASE_DATA = None
SAMPLES = {
    "base" : DataFrame,
    "train" : list(),
    "test" :  list(),
    "validation" : list()
}
