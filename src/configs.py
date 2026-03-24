
from pandas import DataFrame


PROTECTED_ATTRIBUTES  = ["race"]#, "sex", "fam_inc"]
PRIVILEGED_GROUP = [{"race" : 1}]
UNPRIVILEGED_GROUP = [{"race" : 0}]
TARGET = "pass_bar"
FAVORABLE_OUTCOME = [1]

DATASET = DataFrame("./../bar_pass_prediction/bar_pass_prediction.csv")

BASE_DATA = None
SAMPLES = {
    "base" : DataFrame,
    "train" : list(),
    "test" :  list(),
    "validation" : list()
}
