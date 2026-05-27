

TRUE RAW METRICS

|    | metrics                       |   true_raw |   without_protection |   without_race |
|---:|:------------------------------|-----------:|---------------------:|---------------:|
|  0 | test_baseline_accuracy        |      0.945 |                0.948 |          0.948 |
|  1 | test_accuracy                 |      0.947 |                0.95  |          0.951 |
|  2 | test_precision                |      0.947 |                0.951 |          0.951 |
|  3 | test_recall                   |      1     |                0.999 |          0.999 |
|  4 | test_f1                       |      0.973 |                0.974 |          0.975 |
|  5 | test_roc_auc                  |      0.873 |                0.868 |          0.873 |
|  6 | validation_baseline_accuracy  |      0.955 |                0.945 |          0.945 |
|  7 | validation_accuracy           |      0.958 |                0.946 |          0.949 |
|  8 | validation_precision          |      0.958 |                0.946 |          0.949 |
|  9 | validation_recall             |      1     |                1     |          1     |
| 10 | validation_f1                 |      0.979 |                0.972 |          0.974 |
| 11 | validation_roc_auc            |      0.87  |                0.884 |          0.888 |
| 12 | statistical_parity_difference |     -0.023 |               -0.036 |         -0.042 |
| 13 | disparate_impact              |      0.977 |                0.964 |          0.958 |
| 14 | equal_opportunity_difference  |     -0.002 |               -0.007 |         -0.007 |
| 15 | average_odds_difference       |     -0.046 |               -0.073 |         -0.085 |
| 16 | false_positive_rate_diff      |     -0.09  |               -0.139 |         -0.163 |
| 17 | false_discovery_rate_diff     |      0.161 |                0.15  |          0.145 |


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
|  0 | REAL NEGATIVE |                    1 |                   45 |
|  1 | REAL POSITIVE |                    0 |                  783 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   20 |                  367 |
|  1 | REAL POSITIVE |                    7 |                 7075 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    4 |                   42 |
|  1 | REAL POSITIVE |                    0 |                  783 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   25 |                  362 |
|  1 | REAL POSITIVE |                    7 |                 7075 |


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
|  0 | ugpa       |             0.120636 |
|  1 | zgpa       |             0.536103 |
|  2 | lsat       |             0.343261 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | ugpa       |            0.0840339 |
|  1 | zgpa       |            0.516552  |
|  2 | lsat       |            0.298355  |
|  3 | tier       |            0.0722945 |
|  4 | fam_inc    |            0.0287642 |


____________________________________________________________________________________________________