

from pandas import DataFrame

from src.configs import DATASET
from src.eda.inspection import inspection_analysis
from src.eda.univariate import univariate_analysis
from src.eda.bivariate import bivariate_analysis
from src.eda.multivariate import multivariate_analysis


def execute(df : DataFrame) -> None:
    inspection_analysis(DATASET)
    univariate_analysis(df)
    bivariate_analysis(df)
    multivariate_analysis(df)
