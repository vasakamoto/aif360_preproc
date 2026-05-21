
from src.configs import (
        GroupedProcessedDatasets,
        SplitDataset,
        TrainedModels
        )
from src.evaluation.standard import std_metrics
from src.evaluation.fairness import fair_metrics
from src.evaluation.preprocess import process_metrics
from src.evaluation.rf_internal import rf_metrics


def metrics(t : TrainedModels, g : GroupedProcessedDatasets, s : SplitDataset) -> None:
    std_metrics(t, g, s)
    fair_metrics(t, s)
    process_metrics(g, s) 
    rf_metrics(t, g, s)
