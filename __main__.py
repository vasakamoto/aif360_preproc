
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"

from src import (
    charts,
    configs,
    eda,
    etl,
    models,
    pprocess,
    results,
)


def main():
    etl.load()
    samples = configs.SAMPLES

    methods = {
        "Original":                     (pprocess.original(samples), False),
        "Reweighing":                   (pprocess.rw(samples),       True),
        "Disparate Impact Remover":     (pprocess.dir(samples),      False),
        "Learning Fair Representations":(pprocess.lfr(samples),      False),
        "Optimized Preprocessing":      (pprocess.opt(samples),      False),
    }

    all_results = {}
    models_data = {}

    for name, (data, use_weights) in methods.items():
        print(f"\n{'=' * 60}")
        print(f"  {name}")
        print(f"{'=' * 60}")

        model = models.rf(data["train"], use_weights=use_weights)
        metrics = results.all_metrics(model, data)
        results.print_metrics(metrics)

        all_results[name] = metrics
        models_data[name] = {"model": model, "data": data}

    charts.generate_all(all_results, models_data)


if __name__ == "__main__":
    os.system("cls")
    main()
