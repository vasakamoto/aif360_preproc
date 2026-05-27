

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.948 |        0.948 |                      0.948 |                           0.948 |
|  1 | test_accuracy                | 0.902 |        0.874 |                      0.921 |                           0.052 |
|  2 | test_precision               | 0.971 |        0.977 |                      0.965 |                           0     |
|  3 | test_recall                  | 0.924 |        0.889 |                      0.951 |                           0     |
|  4 | test_f1                      | 0.947 |        0.931 |                      0.958 |                           0     |
|  5 | test_roc_auc                 | 0.87  |        0.864 |                      0.86  |                           0.612 |
|  6 | validation_baseline_accuracy | 0.945 |        0.945 |                      0.945 |                           0.945 |
|  7 | validation_accuracy          | 0.901 |        0.879 |                      0.923 |                           0.055 |
|  8 | validation_precision         | 0.969 |        0.979 |                      0.965 |                           0     |
|  9 | validation_recall            | 0.925 |        0.891 |                      0.953 |                           0     |
| 10 | validation_f1                | 0.946 |        0.933 |                      0.959 |                           0     |
| 11 | validation_roc_auc           | 0.872 |        0.873 |                      0.853 |                           0.664 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   23 |                   23 |
|  1 | REAL POSITIVE |                   59 |                  724 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  190 |                  197 |
|  1 | REAL POSITIVE |                  538 |                 6544 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   31 |                   15 |
|  1 | REAL POSITIVE |                   85 |                  698 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  236 |                  151 |
|  1 | REAL POSITIVE |                  787 |                 6295 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   19 |                   27 |
|  1 | REAL POSITIVE |                   37 |                  746 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  141 |                  246 |
|  1 | REAL POSITIVE |                  347 |                 6735 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   46 |                    0 |
|  1 | REAL POSITIVE |                  783 |                    0 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  387 |                    0 |
|  1 | REAL POSITIVE |                 7082 |                    0 |


____________________________________________________________________________________________________

FAIRNESS METRICS

|    | metrics                                  |    raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------------------|-------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_statistical_parity_difference       | -0.523 |       -0.362 |                     -0.604 |                               0 |
|  1 | test_disparate_impact                    |  0.45  |        0.597 |                      0.388 |                             nan |
|  2 | test_equal_opportunity_difference        | -0.447 |       -0.287 |                     -0.532 |                               0 |
|  3 | test_average_odds_difference             | -0.534 |       -0.295 |                     -0.676 |                               0 |
|  4 | test_false_positive_rate_diff            | -0.62  |       -0.303 |                     -0.819 |                               0 |
|  5 | test_false_discovery_rate_diff           |  0.028 |        0.057 |                      0.023 |                               0 |
|  6 | validation_statistical_parity_difference | -0.544 |       -0.365 |                     -0.562 |                               0 |
|  7 | validation_disparate_impact              |  0.429 |        0.592 |                      0.43  |                             nan |
|  8 | validation_equal_opportunity_difference  | -0.452 |       -0.288 |                     -0.483 |                               0 |
|  9 | validation_average_odds_difference       | -0.572 |       -0.251 |                     -0.589 |                               0 |
| 10 | validation_false_positive_rate_diff      | -0.692 |       -0.214 |                     -0.694 |                               0 |
| 11 | validation_false_discovery_rate_diff     |  0.005 |        0.067 |                      0.038 |                               0 |


____________________________________________________________________________________________________

CONSUFION MATRIX - RAW

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  48 |                5813 |                  213 |                  157 |
|      3 |                  85 |                 169 |                  177 |                    6 |
|      2 |                  13 |                 228 |                   50 |                    9 |
|      6 |                  16 |                 122 |                   23 |                    9 |
|      4 |                  11 |                  86 |                   37 |                    8 |
|      8 |                   6 |                  86 |                   15 |                    2 |
|      5 |                   7 |                  22 |                   14 |                    1 |
|      1 |                   4 |                  18 |                    9 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   4 |                 641 |                   23 |                   20 |
|      3 |                  13 |                  18 |                   24 |                    1 |
|      2 |                   3 |                  32 |                    4 |                    2 |
|      4 |                   1 |                   8 |                    4 |                  nan |
|      6 |                 nan |                  10 |                    3 |                  nan |
|      8 |                   1 |                   7 |                  nan |                  nan |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - REWEIGHING

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 100 |                5530 |                  496 |                  105 |
|      3 |                  77 |                 213 |                  133 |                   14 |
|      2 |                  14 |                 222 |                   56 |                    8 |
|      6 |                  19 |                 115 |                   30 |                    6 |
|      4 |                  10 |                  92 |                   31 |                    9 |
|      8 |                   6 |                  80 |                   21 |                    2 |
|      5 |                   6 |                  24 |                   12 |                    2 |
|      1 |                   4 |                  19 |                    8 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  13 |                 613 |                   51 |                   11 |
|      3 |                  11 |                  24 |                   18 |                    3 |
|      2 |                   4 |                  28 |                    8 |                    1 |
|      4 |                   1 |                   9 |                    3 |                  nan |
|      6 |                 nan |                  10 |                    3 |                  nan |
|      8 |                   1 |                   6 |                    1 |                  nan |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - DISPARATE_IMPACT_REMOVER

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   6 |                6003 |                   23 |                  199 |
|      3 |                  87 |                 145 |                  201 |                    4 |
|      2 |                  12 |                 236 |                   42 |                   10 |
|      6 |                  12 |                 133 |                   12 |                   13 |
|      4 |                  13 |                  83 |                   40 |                    6 |
|      8 |                   1 |                  93 |                    8 |                    7 |
|      5 |                   6 |                  24 |                   12 |                    2 |
|      1 |                   4 |                  18 |                    9 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   2 |                 662 |                    2 |                   22 |
|      3 |                  12 |                  18 |                   24 |                    2 |
|      2 |                   3 |                  33 |                    3 |                    2 |
|      4 |                   1 |                   7 |                    5 |                  nan |
|      6 |                 nan |                  11 |                    2 |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - LEARNING_FAIR_REPRESENTATIONS

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 205 |                 nan |                 6026 |                  nan |
|      3 |                  91 |                 nan |                  346 |                  nan |
|      2 |                  22 |                 nan |                  278 |                  nan |
|      6 |                  25 |                 nan |                  145 |                  nan |
|      4 |                  19 |                 nan |                  123 |                  nan |
|      8 |                   8 |                 nan |                  101 |                  nan |
|      5 |                   8 |                 nan |                   36 |                  nan |
|      1 |                   9 |                 nan |                   27 |                  nan |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  24 |                 nan |                  664 |                  nan |
|      3 |                  14 |                 nan |                   42 |                  nan |
|      2 |                   5 |                 nan |                   36 |                  nan |
|      4 |                   1 |                 nan |                   12 |                  nan |
|      6 |                 nan |                 nan |                   13 |                  nan |
|      8 |                   1 |                 nan |                    7 |                  nan |
|      1 |                   1 |                 nan |                    6 |                  nan |
|      5 |                 nan |                 nan |                    3 |                  nan |


____________________________________________________________________________________________________

PROCESSING METRICS

STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT

|    | method                        |   before_spd |   before_di |   after_spd |   after_di |   delta_di |   delta_spd |
|---:|:------------------------------|-------------:|------------:|------------:|-----------:|-----------:|------------:|
|  0 | reweighing                    |       -0.446 |       0.457 |       0     |      1     |      0.543 |       0.446 |
|  1 | disparate_impact_remover      |       -0.446 |       0.457 |      -0.446 |      0.457 |      0     |       0     |
|  2 | learning_fair_representations |       -0.446 |       0.457 |      -0.628 |      0.336 |     -0.121 |      -0.182 |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | ugpa  |                      0.253623 |                    0.253623  |                    0         |
|  1 | disparate_impact_remover      | ugpa  |                      0.253623 |                    0.261364  |                    0.0077413 |
|  2 | learning_fair_representations | ugpa  |                      0.253623 |                    0.869786  |                    0.616163  |
|  3 | reweighing                    | zgpa  |                      0.863318 |                    0.863318  |                    0         |
|  4 | disparate_impact_remover      | zgpa  |                      0.863318 |                    0.0615231 |                   -0.801795  |
|  5 | learning_fair_representations | zgpa  |                      0.863318 |                    7.70178   |                    6.83846   |
|  6 | reweighing                    | lsat  |                      6.92139  |                    6.92139   |                    0         |
|  7 | disparate_impact_remover      | lsat  |                      6.92139  |                    1.73296   |                   -5.18843   |
|  8 | learning_fair_representations | lsat  |                      6.92139  |                    5.36612   |                   -1.55527   |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | ugpa  |     0.0702  |    0.0702  |    0       |
|  1 | reweighing                    | zgpa  |     0.19015 |    0.19015 |    0       |
|  2 | reweighing                    | lsat  |     0.11185 |    0.11185 |    0       |
|  3 | disparate_impact_remover      | ugpa  |     0.0702  |    0.06189 |   -0.00832 |
|  4 | disparate_impact_remover      | zgpa  |     0.19015 |    0.09543 |   -0.09472 |
|  5 | disparate_impact_remover      | lsat  |     0.11185 |    0.05313 |   -0.05872 |
|  6 | learning_fair_representations | ugpa  |     0.0702  |    0.65754 |    0.58733 |
|  7 | learning_fair_representations | zgpa  |     0.19015 |    0.66486 |    0.47471 |
|  8 | learning_fair_representations | lsat  |     0.11185 |    0.66086 |    0.54901 |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | ugpa       | 0.10341   |    0.0961243 |                  0.105199  |                     0.0569718   |
|  1 | zgpa       | 0.461141  |    0.573636  |                  0.356156  |                     0.25004     |
|  2 | lsat       | 0.238085  |    0.166777  |                  0.179191  |                     0.129444    |
|  3 | race       | 0.105856  |    0.0631879 |                  0.237916  |                     0.281903    |
|  4 | tier       | 0.0723838 |    0.073877  |                  0.100874  |                     0.000514452 |
|  5 | fam_inc    | 0.0191237 |    0.0263972 |                  0.0206637 |                     0.281127    |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.870099 |                   0.436667 |              0          |
| Reweighing |     0.864215 |                   0.386667 |              0.00588401 |
| DIR        |     0.864488 |                   0.448333 |              0.00561072 |
| LFR        |     1        |                   0        |             -0.129901   |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.942295 |                             0.108047 |
| DIR Space      |               0.939617 |                             0.105369 |
| LFR Space      |               0.863837 |                             0.029589 |


____________________________________________________________________________________________________