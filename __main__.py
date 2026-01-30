
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"

from src import (
    configs,
    eda,
    etl,
    models,
    results,
)


def main():
    etl.load()

    #vrf = models.rf(data, "original_samples")
    #metrics = results.all_metrics(vrf, data["original_dataframe"], data, "original_samples")
    #results.print_metrics(metrics)

    #rwrf = models.rf(data, "reweighted_samples")
    #metrics = results.all_metrics(rwrf, data["reweighted_dataframe"], data, "reweighted_samples")
    #results.print_metrics(metrics)
        

if __name__ == "__main__":
    os.system("cls")
    main()
