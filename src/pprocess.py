
from aif360.datasets import BinaryLabelDataset, StandardDataset
from aif360.algorithms.preprocessing import (
    DisparateImpactRemover,
    LFR,
    OptimPreproc,
    Reweighing,
)
from numpy import linspace
from pandas import merge

from .configs import (
    PRIVILEGED_GROUP,
    UNPRIVILEGED_GROUP,
    TARGET,
    FAVORABLE_OUTCOME,
    PROTECTED_ATTRIBUTES,
    SAMPLES
)


def dir(samples : dict) -> BinaryLabelDataset:
    for level in linspace(0., 1., 11):
        di = DisparateImpactRemover(repair_level=level)
        train_repd = di.fit_transform(train)
        test_repd = di.fit_transform(test)
        
        X_tr = np.delete(train_repd.features, index, axis=1)
        X_te = np.delete(test_repd.features, index, axis=1)
        y_tr = train_repd.labels.ravel()


def lfr():
    pass


def opt():
    pass

def rw(samples : dict) -> StandardDataset:
    odf = merge(samples["train"][0], samples["train"][1], right_index=True, left_index=True) 
    sds = StandardDataset(
        odf,
        label_name=TARGET,
        favorable_classes=FAVORABLE_OUTCOME,
        protected_attribute_names=PROTECTED_ATTRIBUTES,
        privileged_classes=[[p["race"] for p in PRIVILEGED_GROUP]],
    )
    rw = Reweighing(
        privileged_groups=PRIVILEGED_GROUP,
        unprivileged_groups=UNPRIVILEGED_GROUP,
    )
    return rw.fit_transform(sds)

