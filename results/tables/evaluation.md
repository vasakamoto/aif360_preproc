

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.678 |        0.678 |                      0.678 |                           0.678 |
|  1 | test_accuracy                | 0.803 |        0.808 |                      0.783 |                           0.322 |
|  2 | test_precision               | 0.831 |        0.83  |                      0.784 |                           0     |
|  3 | test_recall                  | 0.891 |        0.9   |                      0.938 |                           0     |
|  4 | test_f1                      | 0.86  |        0.864 |                      0.854 |                           0     |
|  5 | test_roc_auc                 | 0.87  |        0.869 |                      0.84  |                           0.539 |
|  6 | validation_baseline_accuracy | 0.643 |        0.643 |                      0.643 |                           0.643 |
|  7 | validation_accuracy          | 0.754 |        0.786 |                      0.77  |                           0.357 |
|  8 | validation_precision         | 0.791 |        0.807 |                      0.765 |                           0     |
|  9 | validation_recall            | 0.84  |        0.877 |                      0.926 |                           0     |
| 10 | validation_f1                | 0.814 |        0.84  |                      0.838 |                           0     |
| 11 | validation_roc_auc           | 0.881 |        0.904 |                      0.841 |                           0.543 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   27 |                   18 |
|  1 | REAL POSITIVE |                   13 |                   68 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  227 |                  140 |
|  1 | REAL POSITIVE |                   84 |                  688 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   28 |                   17 |
|  1 | REAL POSITIVE |                   10 |                   71 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  225 |                  142 |
|  1 | REAL POSITIVE |                   77 |                  695 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   22 |                   23 |
|  1 | REAL POSITIVE |                    6 |                   75 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  168 |                  199 |
|  1 | REAL POSITIVE |                   48 |                  724 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   45 |                    0 |
|  1 | REAL POSITIVE |                   81 |                    0 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  367 |                    0 |
|  1 | REAL POSITIVE |                  772 |                    0 |


____________________________________________________________________________________________________

FAIRNESS METRICS

|    | metrics                                  |    raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------------------|-------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_statistical_parity_difference       | -0.632 |       -0.435 |                     -0.691 |                               0 |
|  1 | test_disparate_impact                    |  0.256 |        0.47  |                      0.268 |                             nan |
|  2 | test_equal_opportunity_difference        | -0.492 |       -0.204 |                     -0.439 |                               0 |
|  3 | test_average_odds_difference             | -0.479 |       -0.243 |                     -0.581 |                               0 |
|  4 | test_false_positive_rate_diff            | -0.466 |       -0.282 |                     -0.723 |                               0 |
|  5 | test_false_discovery_rate_diff           |  0.152 |        0.23  |                      0.075 |                               0 |
|  6 | validation_statistical_parity_difference | -0.74  |       -0.485 |                     -0.679 |                               0 |
|  7 | validation_disparate_impact              |  0.127 |        0.399 |                      0.269 |                             nan |
|  8 | validation_equal_opportunity_difference  | -0.761 |       -0.278 |                     -0.44  |                               0 |
|  9 | validation_average_odds_difference       | -0.655 |       -0.348 |                     -0.584 |                               0 |
| 10 | validation_false_positive_rate_diff      | -0.548 |       -0.418 |                     -0.727 |                               0 |
| 11 | validation_false_discovery_rate_diff     |  0.129 |        0.032 |                     -0.099 |                               0 |


____________________________________________________________________________________________________

CONSUFION MATRIX - RAW

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  77 |                 636 |                   30 |                  119 |
|      3 |                  90 |                   8 |                   26 |                    5 |
|      2 |                  18 |                  19 |                   13 |                    6 |
|      4 |                  12 |                  12 |                    5 |                    2 |
|      6 |                  14 |                   7 |                    5 |                    4 |
|      8 |                   5 |                   3 |                    3 |                    2 |
|      5 |                   8 |                   2 |                  nan |                    1 |
|      1 |                   3 |                   1 |                    2 |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  11 |                  65 |                    4 |                   17 |
|      3 |                  13 |                 nan |                    4 |                  nan |
|      4 |                   2 |                 nan |                    2 |                  nan |
|      8 |                 nan |                   1 |                    1 |                    1 |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                   1 |                    1 |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - REWEIGHING

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  97 |                 616 |                   50 |                   99 |
|      3 |                  82 |                  17 |                   17 |                   13 |
|      2 |                  13 |                  26 |                    6 |                   11 |
|      4 |                   8 |                  15 |                    2 |                    6 |
|      6 |                  11 |                  11 |                    1 |                    7 |
|      8 |                   5 |                   5 |                    1 |                    2 |
|      5 |                   6 |                   2 |                  nan |                    3 |
|      1 |                   3 |                   3 |                  nan |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  13 |                  63 |                    6 |                   15 |
|      3 |                  12 |                   2 |                    2 |                    1 |
|      4 |                   2 |                   2 |                  nan |                  nan |
|      8 |                 nan |                   2 |                  nan |                    1 |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                   1 |                    1 |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - DISPARATE_IMPACT_REMOVER

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  23 |                 659 |                    7 |                  173 |
|      3 |                  91 |                   8 |                   26 |                    4 |
|      2 |                  14 |                  25 |                    7 |                   10 |
|      4 |                  11 |                  14 |                    3 |                    3 |
|      6 |                  13 |                   8 |                    4 |                    5 |
|      8 |                   5 |                   6 |                  nan |                    2 |
|      5 |                   8 |                   2 |                  nan |                    1 |
|      1 |                   3 |                   2 |                    1 |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   6 |                  68 |                    1 |                   22 |
|      3 |                  13 |                   1 |                    3 |                  nan |
|      4 |                   2 |                   2 |                  nan |                  nan |
|      8 |                 nan |                   2 |                  nan |                    1 |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                   1 |                    1 |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - LEARNING_FAIR_REPRESENTATIONS

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 196 |                 nan |                  666 |                  nan |
|      3 |                  95 |                 nan |                   34 |                  nan |
|      2 |                  24 |                 nan |                   32 |                  nan |
|      4 |                  14 |                 nan |                   17 |                  nan |
|      6 |                  18 |                 nan |                   12 |                  nan |
|      8 |                   7 |                 nan |                    6 |                  nan |
|      5 |                   9 |                 nan |                    2 |                  nan |
|      1 |                   4 |                 nan |                    3 |                  nan |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  28 |                 nan |                   69 |                  nan |
|      3 |                  13 |                 nan |                    4 |                  nan |
|      4 |                   2 |                 nan |                    2 |                  nan |
|      8 |                   1 |                 nan |                    2 |                  nan |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                 nan |                    2 |                  nan |
|      2 |                 nan |                 nan |                    1 |                  nan |


____________________________________________________________________________________________________

PROCESSING METRICS

STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT

|    | method                        |   before_spd |   before_di |   after_spd |   after_di |   delta_di |   delta_spd |
|---:|:------------------------------|-------------:|------------:|------------:|-----------:|-----------:|------------:|
|  0 | reweighing                    |       -0.409 |       0.451 |       0     |      1     |      0.549 |       0.409 |
|  1 | disparate_impact_remover      |       -0.409 |       0.451 |      -0.409 |      0.451 |      0     |       0     |
|  2 | learning_fair_representations |       -0.409 |       0.451 |      -0.525 |      0.372 |     -0.079 |      -0.116 |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | zgpa  |                      0.910652 |                     0.910652 |                     0        |
|  1 | disparate_impact_remover      | zgpa  |                      0.910652 |                     0.128715 |                    -0.781937 |
|  2 | learning_fair_representations | zgpa  |                      0.910652 |                     5.98558  |                     5.07492  |
|  3 | reweighing                    | lsat  |                      7.4684   |                     7.4684   |                     0        |
|  4 | disparate_impact_remover      | lsat  |                      7.4684   |                     2.99607  |                    -4.47233  |
|  5 | learning_fair_representations | lsat  |                      7.4684   |                     3.83042  |                    -3.63798  |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | zgpa  |     0.17775 |    0.17775 |    0       |
|  1 | reweighing                    | lsat  |     0.11445 |    0.11445 |    0       |
|  2 | disparate_impact_remover      | zgpa  |     0.17775 |    0.09113 |   -0.08662 |
|  3 | disparate_impact_remover      | lsat  |     0.11445 |    0.09644 |   -0.01801 |
|  4 | learning_fair_representations | zgpa  |     0.17775 |    0.58082 |    0.40307 |
|  5 | learning_fair_representations | lsat  |     0.11445 |    0.57551 |    0.46105 |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | zgpa       | 0.535403  |    0.630613  |                  0.424197  |                     0.320487    |
|  1 | lsat       | 0.2785    |    0.229981  |                  0.233884  |                     0.167686    |
|  2 | race       | 0.103834  |    0.0375826 |                  0.230417  |                     0.000198317 |
|  3 | tier       | 0.0600389 |    0.0757564 |                  0.0812329 |                     0.0973018   |
|  4 | fam_inc    | 0.0222247 |    0.0260664 |                  0.0302691 |                     0.414327    |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.870466 |                   0.371429 |              0          |
| Reweighing |     0.869286 |                   0.326984 |              0.00118063 |
| DIR        |     0.862933 |                   0.406349 |              0.00753378 |
| LFR        |     0.999992 |                   0        |             -0.129526   |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.928007 |                            0.171203  |
| DIR Space      |               0.922739 |                            0.165935  |
| LFR Space      |               0.832309 |                            0.0755048 |


____________________________________________________________________________________________________