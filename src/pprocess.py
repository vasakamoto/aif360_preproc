
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


def _build_dataset(samples: dict, split: str = "train") -> StandardDataset:
    odf = merge(samples[split][0], samples[split][1], right_index=True, left_index=True)
    return StandardDataset(
        odf,
        label_name=TARGET,
        favorable_classes=FAVORABLE_OUTCOME,
        protected_attribute_names=PROTECTED_ATTRIBUTES,
        privileged_classes=[[p["race"] for p in PRIVILEGED_GROUP]],
    )


def _build_all_splits(samples: dict) -> dict:
    return {
        "train": _build_dataset(samples, "train"),
        "test": _build_dataset(samples, "test"),
        "validation": _build_dataset(samples, "validation"),
    }


def original(samples: dict) -> dict:
    return _build_all_splits(samples)


def rw(samples: dict) -> dict:
    splits = _build_all_splits(samples)
    model = Reweighing(
        privileged_groups=PRIVILEGED_GROUP,
        unprivileged_groups=UNPRIVILEGED_GROUP,
    )
    model.fit(splits["train"])
    splits["train"] = model.transform(splits["train"])
    return splits


def dir(samples: dict, repair_level: float = 1.0) -> dict:
    splits = _build_all_splits(samples)
    di = DisparateImpactRemover(
        repair_level=repair_level,
        sensitive_attribute=PROTECTED_ATTRIBUTES[0],
    )
    return {name: di.fit_transform(ds) for name, ds in splits.items()}


def lfr(samples: dict, k: int = 5, Ax: float = 0.01, Ay: float = 1.0, Az: float = 50.0) -> dict:
    splits = _build_all_splits(samples)
    model = LFR(
        unprivileged_groups=UNPRIVILEGED_GROUP,
        privileged_groups=PRIVILEGED_GROUP,
        k=k,
        Ax=Ax,
        Ay=Ay,
        Az=Az,
        verbose=0,
    )
    model.fit(splits["train"])
    return {name: model.transform(ds) for name, ds in splits.items()}


def opt(samples: dict, n_bins: int = 10) -> dict:
    splits = _build_all_splits(samples)

    # OptimPreproc requires discrete features for conditional probability estimation;
    # continuous features are binned before transformation.
    for key in splits:
        df = splits[key].convert_to_dataframe()[0]
        for col in df.columns:
            if col not in (TARGET, *PROTECTED_ATTRIBUTES) and df[col].nunique() > n_bins:
                df[col] = cut(df[col], bins=n_bins, labels=False)
        splits[key] = StandardDataset(
            df,
            label_name=TARGET,
            favorable_classes=FAVORABLE_OUTCOME,
            protected_attribute_names=PROTECTED_ATTRIBUTES,
            privileged_classes=[[p["race"] for p in PRIVILEGED_GROUP]],
        )

    op = OptimPreproc(
        OptTools,
        _optim_options(),
        unprivileged_groups=UNPRIVILEGED_GROUP,
        privileged_groups=PRIVILEGED_GROUP,
        verbose=0,
    )
    op.fit(splits["train"])

    return {
        name: splits[name].align_datasets(op.transform(ds, transform_Y=True))
        for name, ds in splits.items()
    }


def _optim_options() -> dict:
    def distortion(vold, vnew):
        return sum(1.0 for key in vold if vold[key] != vnew[key])

    return {
        "distortion_fun": distortion,
        "epsilon": 0.05,
        "clist": [0.99, 1.99, 2.99],
        "dlist": [0.1, 0.05, 0.0],
    }
