

TRUE RAW METRICS

|    | metrics                       |   true_raw |   without_protection |   without_race |
|---:|:------------------------------|-----------:|---------------------:|---------------:|
|  0 | test_baseline_accuracy        |      0.945 |                0.948 |          0.948 |
|  1 | test_accuracy                 |      0.947 |                0.885 |          0.889 |
|  2 | test_precision                |      0.947 |                0.975 |          0.976 |
|  3 | test_recall                   |      1     |                0.901 |          0.905 |
|  4 | test_f1                       |      0.973 |                0.937 |          0.939 |
|  5 | test_roc_auc                  |      0.873 |                0.869 |          0.872 |
|  6 | validation_baseline_accuracy  |      0.955 |                0.945 |          0.945 |
|  7 | validation_accuracy           |      0.958 |                0.891 |          0.888 |
|  8 | validation_precision          |      0.958 |                0.975 |          0.974 |
|  9 | validation_recall             |      1     |                0.908 |          0.905 |
| 10 | validation_f1                 |      0.979 |                0.94  |          0.938 |
| 11 | validation_roc_auc            |      0.87  |                0.883 |          0.881 |
| 12 | statistical_parity_difference |     -0.023 |               -0.466 |         -0.473 |
| 13 | disparate_impact              |      0.977 |                0.494 |          0.488 |
| 14 | equal_opportunity_difference  |     -0.002 |               -0.397 |         -0.396 |
| 15 | average_odds_difference       |     -0.046 |               -0.411 |         -0.427 |
| 16 | false_positive_rate_diff      |     -0.09  |               -0.425 |         -0.457 |
| 17 | false_discovery_rate_diff     |      0.161 |                0.046 |          0.03  |


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
|  0 | REAL NEGATIVE |                   28 |                   18 |
|  1 | REAL POSITIVE |                   72 |                  711 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  226 |                  161 |
|  1 | REAL POSITIVE |                  700 |                 6382 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   27 |                   19 |
|  1 | REAL POSITIVE |                   74 |                  709 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  232 |                  155 |
|  1 | REAL POSITIVE |                  674 |                 6408 |


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
|  0 | ugpa       |             0.155674 |
|  1 | zgpa       |             0.517962 |
|  2 | lsat       |             0.326364 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | ugpa       |            0.106787  |
|  1 | zgpa       |            0.513698  |
|  2 | lsat       |            0.284356  |
|  3 | tier       |            0.0730072 |
|  4 | fam_inc    |            0.0221522 |


____________________________________________________________________________________________________