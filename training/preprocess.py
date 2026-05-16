
from aif360.datasets import BinaryLabelDataset, StandardDataset
from aif360.algorithms.preprocessing import (
    DisparateImpactRemover,
    LFR,
    OptimPreproc,
    Reweighing,
)
from aif360.algorithms.preprocessing.optim_preproc_helpers.opt_tools import OptTools
from pandas import merge, cut

from .configs import (
    PRIVILEGED_GROUP,
    UNPRIVILEGED_GROUP,
    TARGET,
    FAVORABLE_OUTCOME,
    PROTECTED_ATTRIBUTES,
)
