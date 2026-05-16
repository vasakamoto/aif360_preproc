
import os
from time import perf_counter

os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
os.system("clear")

import eda
from src import (
#    charts,
    configs,
    etl,
#    models,
#    pprocess,
#    results,
)


#def main():
#    etl.load()
#    samples = configs.SAMPLES
#
#    methods = {
#        "Original":                     (pprocess.original(samples), False),
#        "Reweighing":                   (pprocess.rw(samples),       True),
#        "Disparate Impact Remover":     (pprocess.dir(samples),      False),
#        "Learning Fair Representations":(pprocess.lfr(samples),      False),
#        "Optimized Preprocessing":      (pprocess.opt(samples),      False),
#    }
#
#    all_results = {}
#    models_data = {}
#
#    for name, (data, use_weights) in methods.items():
#        print(f"\n{'=' * 60}")
#        print(f"  {name}")
#        print(f"{'=' * 60}")
#
#        model = models.rf(data["train"], use_weights=use_weights)
#        metrics = results.all_metrics(model, data)
#        results.print_metrics(metrics)
#
#        all_results[name] = metrics
#        models_data[name] = {"model": model, "data": data}
#
#    charts.generate_all(all_results, models_data)

df = etl.run(configs.DATASET)

def run_eda() -> None:
    #eda.inspection_analysis(configs.DATASET)               ## needs some attention return an object or something I don't know
    eda.univariate_analysis(df)
    eda.bivariate_analysis(df)
    eda.multivariate_analysis(df)


def run_training() -> None:

    return

if __name__ == "__main__":
    stime = perf_counter()
    #run_eda()
    run_training()
    etime = perf_counter()
    print(f"\n\nEXECUTION TIME: {etime - stime:.3f}")

