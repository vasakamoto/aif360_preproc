
from src.configs import (
        GroupedProcessedDatasets,
        SplitDataset,
        TrainedModels,
        PATH_ROOT,
        DATASET
        )
from src.evaluation.standard import std_metrics
from src.evaluation.fairness import fair_metrics
from src.evaluation.preprocess import process_metrics
from src.evaluation.rf_internal import rf_metrics
from src.evaluation.lfr_tuning import lfr_exploration
from src.evaluation.raw_model import evaluate


def metrics(t : TrainedModels, g : GroupedProcessedDatasets, s : SplitDataset) -> None:
    (PATH_ROOT/"results"/"tables"/"evaluation.md").unlink(missing_ok=True)
    std_metrics(t, g, s)
    fair_metrics(t, s)
    process_metrics(g, s) 
    rf_metrics(t, g, s)
    #lfr_exploration(s)
    evaluate(DATASET, s)
