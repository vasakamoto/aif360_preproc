

TRUE RAW METRICS

|    | metrics                       |   true_raw |   without_protection |   without_race |
|---:|:------------------------------|-----------:|---------------------:|---------------:|
|  0 | test_baseline_accuracy        |      0.945 |                0.678 |          0.678 |
|  1 | test_accuracy                 |      0.947 |                0.801 |          0.809 |
|  2 | test_precision                |      0.947 |                0.826 |          0.836 |
|  3 | test_recall                   |      1     |                0.894 |          0.894 |
|  4 | test_f1                       |      0.973 |                0.859 |          0.864 |
|  5 | test_roc_auc                  |      0.873 |                0.874 |          0.878 |
|  6 | validation_baseline_accuracy  |      0.955 |                0.643 |          0.643 |
|  7 | validation_accuracy           |      0.958 |                0.802 |          0.81  |
|  8 | validation_precision          |      0.958 |                0.811 |          0.82  |
|  9 | validation_recall             |      1     |                0.901 |          0.901 |
| 10 | validation_f1                 |      0.979 |                0.854 |          0.859 |
| 11 | validation_roc_auc            |      0.87  |                0.89  |          0.897 |
| 12 | statistical_parity_difference |     -0.023 |               -0.652 |         -0.646 |
| 13 | disparate_impact              |      0.977 |                0.226 |          0.221 |
| 14 | equal_opportunity_difference  |     -0.002 |               -0.494 |         -0.464 |
| 15 | average_odds_difference       |     -0.046 |               -0.478 |         -0.454 |
| 16 | false_positive_rate_diff      |     -0.09  |               -0.462 |         -0.444 |
| 17 | false_discovery_rate_diff     |      0.161 |                0.232 |          0.181 |


____________________________________________________________________________________________________

CONFUSION MATRIX RAW TRUE METRICS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    3 |                   34 |
|  1 | REAL POSITIVE |                    0 |                  780 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   15 |                  391 |
|  1 | REAL POSITIVE |                    1 |                 6947 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT PROTECTED ATTRIBUTES

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   28 |                   17 |
|  1 | REAL POSITIVE |                    8 |                   73 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  222 |                  145 |
|  1 | REAL POSITIVE |                   82 |                  690 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   29 |                   16 |
|  1 | REAL POSITIVE |                    8 |                   73 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  232 |                  135 |
|  1 | REAL POSITIVE |                   82 |                  690 |


____________________________________________________________________________________________________

FEATURE IMPORTANCE TRUE RAW

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | decile1b   |          0.0541845   |
|  1 | decile3    |          0.100117    |
|  2 | decile1    |          0.0606519   |
|  3 | sex        |          0.00205659  |
|  4 | race       |          0.0293192   |
|  5 | cluster    |          0.0188105   |
|  6 | lsat       |          0.115336    |
|  7 | ugpa       |          0.0234779   |
|  8 | zfygpa     |          0.0804982   |
|  9 | DOB_yr     |          0.0242985   |
| 10 | zgpa       |          0.215925    |
| 11 | bar1_yr    |          0.00545501  |
| 12 | bar2_yr    |          0.0109109   |
| 13 | fulltime   |          0.00862504  |
| 14 | fam_inc    |          0.0064189   |
| 15 | age        |          0.0218917   |
| 16 | parttime   |          0.0049537   |
| 17 | male       |          0.00212556  |
| 18 | other      |          0.000530596 |
| 19 | asian      |          0.000516042 |
| 20 | black      |          0.0148613   |
| 21 | hisp       |          0.000233877 |
| 22 | tier       |          0.0317578   |
| 23 | index6040  |          0.140453    |
| 24 | gpa        |          0.0265901   |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT PROTECTED ATTRIBUTES

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | ugpa       |             0.11719  |
|  1 | zgpa       |             0.569215 |
|  2 | lsat       |             0.313595 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | ugpa       |            0.0792177 |
|  1 | zgpa       |            0.543309  |
|  2 | lsat       |            0.297854  |
|  3 | tier       |            0.0591965 |
|  4 | fam_inc    |            0.0204226 |


____________________________________________________________________________________________________