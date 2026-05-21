
import os
from time import perf_counter

os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
os.system("clear")

from src import (
        #    charts,
        configs,
        etl,
        evaluation,
        eda,
        training
        #    models,
        #    pprocess,
        #    results,
        )


if __name__ == "__main__":
    stime = perf_counter()
    df = etl.run(configs.DATASET)
    #eda.execute(df)
    t = training.execute(df)
    evaluation.metrics(t["models"], t["grouped_ds"], t["split_ds"])
    etime = perf_counter()
    print(f"\n\nEXECUTION TIME: {etime - stime:.3f}")

