

TRUE RAW METRICS

|    | metrics                       |   true_raw |   without_protection |   without_race |
|---:|:------------------------------|-----------:|---------------------:|---------------:|
|  0 | test_baseline_accuracy        |      0.945 |                0.948 |          0.948 |
|  1 | test_accuracy                 |      0.947 |                0.85  |          0.848 |
|  2 | test_precision                |      0.947 |                0.979 |          0.979 |
|  3 | test_recall                   |      1     |                0.86  |          0.859 |
|  4 | test_f1                       |      0.973 |                0.916 |          0.915 |
|  5 | test_roc_auc                  |      0.873 |                0.868 |          0.872 |
|  6 | validation_baseline_accuracy  |      0.955 |                0.945 |          0.945 |
|  7 | validation_accuracy           |      0.958 |                0.861 |          0.869 |
|  8 | validation_precision          |      0.958 |                0.984 |          0.984 |
|  9 | validation_recall             |      1     |                0.867 |          0.875 |
| 10 | validation_f1                 |      0.979 |                0.922 |          0.926 |
| 11 | validation_roc_auc            |      0.87  |                0.883 |          0.884 |
| 12 | statistical_parity_difference |     -0.023 |               -0.501 |         -0.505 |
| 13 | disparate_impact              |      0.977 |                0.432 |          0.428 |
| 14 | equal_opportunity_difference  |     -0.002 |               -0.442 |         -0.449 |
| 15 | average_odds_difference       |     -0.046 |               -0.404 |         -0.413 |
| 16 | false_positive_rate_diff      |     -0.09  |               -0.365 |         -0.378 |
| 17 | false_discovery_rate_diff     |      0.161 |                0.037 |          0.042 |


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
|  0 | REAL NEGATIVE |                   35 |                   11 |
|  1 | REAL POSITIVE |                  104 |                  679 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  255 |                  132 |
|  1 | REAL POSITIVE |                  991 |                 6091 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   35 |                   11 |
|  1 | REAL POSITIVE |                   98 |                  685 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  254 |                  133 |
|  1 | REAL POSITIVE |                 1001 |                 6081 |


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
|  0 | ugpa       |             0.11217  |
|  1 | zgpa       |             0.629401 |
|  2 | lsat       |             0.258429 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | ugpa       |            0.0761766 |
|  1 | zgpa       |            0.612326  |
|  2 | lsat       |            0.239285  |
|  3 | tier       |            0.0446725 |
|  4 | fam_inc    |            0.0275401 |


____________________________________________________________________________________________________