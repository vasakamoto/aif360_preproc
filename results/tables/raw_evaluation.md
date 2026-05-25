

TRUE RAW METRICS

|    | metrics                       |   true_raw |   without_protection |   without_race |
|---:|:------------------------------|-----------:|---------------------:|---------------:|
|  0 | test_baseline_accuracy        |      0.945 |                0.678 |          0.678 |
|  1 | test_accuracy                 |      0.947 |                0.802 |          0.804 |
|  2 | test_precision                |      0.947 |                0.828 |          0.831 |
|  3 | test_recall                   |      1     |                0.895 |          0.892 |
|  4 | test_f1                       |      0.973 |                0.86  |          0.861 |
|  5 | test_roc_auc                  |      0.873 |                0.866 |          0.872 |
|  6 | validation_baseline_accuracy  |      0.955 |                0.643 |          0.643 |
|  7 | validation_accuracy           |      0.958 |                0.794 |          0.786 |
|  8 | validation_precision          |      0.958 |                0.809 |          0.807 |
|  9 | validation_recall             |      1     |                0.889 |          0.877 |
| 10 | validation_f1                 |      0.979 |                0.847 |          0.84  |
| 11 | validation_roc_auc            |      0.87  |                0.897 |          0.897 |
| 12 | statistical_parity_difference |     -0.023 |               -0.677 |         -0.652 |
| 13 | disparate_impact              |      0.977 |                0.194 |          0.213 |
| 14 | equal_opportunity_difference  |     -0.002 |               -0.547 |         -0.514 |
| 15 | average_odds_difference       |     -0.046 |               -0.509 |         -0.477 |
| 16 | false_positive_rate_diff      |     -0.09  |               -0.472 |         -0.44  |
| 17 | false_discovery_rate_diff     |      0.16  |                0.214 |          0.228 |


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
|  1 | REAL POSITIVE |                    9 |                   72 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  223 |                  144 |
|  1 | REAL POSITIVE |                   81 |                  691 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   28 |                   17 |
|  1 | REAL POSITIVE |                   10 |                   71 |

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  227 |                  140 |
|  1 | REAL POSITIVE |                   83 |                  689 |


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
|  0 | zgpa       |             0.622039 |
|  1 | lsat       |             0.377961 |


____________________________________________________________________________________________________

CONFUSION MATRIX WITHOUT RACE

|    | features   |   feature_importance |
|---:|:-----------|---------------------:|
|  0 | zgpa       |            0.609783  |
|  1 | lsat       |            0.299542  |
|  2 | tier       |            0.0662358 |
|  3 | fam_inc    |            0.0244396 |


____________________________________________________________________________________________________