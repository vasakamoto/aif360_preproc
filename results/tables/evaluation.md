

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.678 |        0.678 |                      0.678 |                           0.678 |
|  1 | test_accuracy                | 0.789 |        0.809 |                      0.777 |                           0.695 |
|  2 | test_precision               | 0.815 |        0.839 |                      0.778 |                           0.695 |
|  3 | test_recall                  | 0.891 |        0.89  |                      0.939 |                           0.979 |
|  4 | test_f1                      | 0.851 |        0.864 |                      0.851 |                           0.813 |
|  5 | test_roc_auc                 | 0.874 |        0.875 |                      0.849 |                           0.631 |
|  6 | validation_baseline_accuracy | 0.643 |        0.643 |                      0.643 |                           0.643 |
|  7 | validation_accuracy          | 0.786 |        0.786 |                      0.77  |                           0.667 |
|  8 | validation_precision         | 0.8   |        0.807 |                      0.765 |                           0.664 |
|  9 | validation_recall            | 0.889 |        0.877 |                      0.926 |                           0.975 |
| 10 | validation_f1                | 0.842 |        0.84  |                      0.838 |                           0.79  |
| 11 | validation_roc_auc           | 0.883 |        0.894 |                      0.834 |                           0.619 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   27 |                   18 |
|  1 | REAL POSITIVE |                    9 |                   72 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  211 |                  156 |
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
|  0 | REAL NEGATIVE |                  235 |                  132 |
|  1 | REAL POSITIVE |                   85 |                  687 |


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
|  0 | REAL NEGATIVE |                  160 |                  207 |
|  1 | REAL POSITIVE |                   47 |                  725 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    5 |                   40 |
|  1 | REAL POSITIVE |                    2 |                   79 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   36 |                  331 |
|  1 | REAL POSITIVE |                   16 |                  756 |


____________________________________________________________________________________________________

FAIRNESS METRICS

|    | metrics                                  |    raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------------------|-------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_statistical_parity_difference       | -0.73  |       -0.559 |                     -0.835 |                          -0.172 |
|  1 | test_disparate_impact                    |  0.157 |        0.311 |                      0.122 |                           0.825 |
|  2 | test_equal_opportunity_difference        | -0.602 |       -0.376 |                     -0.672 |                          -0.088 |
|  3 | test_average_odds_difference             | -0.591 |       -0.355 |                     -0.743 |                          -0.139 |
|  4 | test_false_positive_rate_diff            | -0.581 |       -0.334 |                     -0.813 |                          -0.19  |
|  5 | test_false_discovery_rate_diff           |  0.171 |        0.29  |                      0.078 |                           0.469 |
|  6 | validation_statistical_parity_difference | -0.805 |       -0.658 |                     -0.886 |                          -0.253 |
|  7 | validation_disparate_impact              |  0.061 |        0.193 |                      0.056 |                           0.744 |
|  8 | validation_equal_opportunity_difference  | -0.757 |       -0.529 |                     -0.8   |                          -0.186 |
|  9 | validation_average_odds_difference       | -0.682 |       -0.496 |                     -0.793 |                          -0.236 |
| 10 | validation_false_positive_rate_diff      | -0.607 |       -0.464 |                     -0.786 |                          -0.286 |
| 11 | validation_false_discovery_rate_diff     | -0.202 |        0.146 |                     -0.239 |                           0.426 |


____________________________________________________________________________________________________

CONSUFION MATRIX - RAW

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  61 |                 632 |                   34 |                  135 |
|      3 |                  90 |                  10 |                   24 |                    5 |
|      2 |                  17 |                  21 |                   11 |                    7 |
|      4 |                  12 |                  12 |                    5 |                    2 |
|      6 |                  14 |                   6 |                    6 |                    4 |
|      8 |                   6 |                   4 |                    2 |                    1 |
|      5 |                   8 |                   2 |                  nan |                    1 |
|      1 |                   3 |                   1 |                    2 |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  11 |                  66 |                    3 |                   17 |
|      3 |                  13 |                   1 |                    3 |                  nan |
|      4 |                   2 |                   1 |                    1 |                  nan |
|      8 |                 nan |                   2 |                  nan |                    1 |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                   1 |                    1 |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - REWEIGHING

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  99 |                 613 |                   53 |                   97 |
|      3 |                  81 |                  16 |                   18 |                   14 |
|      2 |                  15 |                  25 |                    7 |                    9 |
|      4 |                   9 |                  15 |                    2 |                    5 |
|      6 |                  14 |                   8 |                    4 |                    4 |
|      8 |                   6 |                   5 |                    1 |                    1 |
|      5 |                   8 |                   2 |                  nan |                    1 |
|      1 |                   3 |                   3 |                  nan |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  13 |                  64 |                    5 |                   15 |
|      3 |                  12 |                   2 |                    2 |                    1 |
|      4 |                   2 |                   2 |                  nan |                  nan |
|      8 |                 nan |                   1 |                    1 |                    1 |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                   1 |                    1 |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - DISPARATE_IMPACT_REMOVER

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  18 |                 659 |                    7 |                  178 |
|      3 |                  92 |                   8 |                   26 |                    3 |
|      2 |                  13 |                  25 |                    7 |                   11 |
|      4 |                  10 |                  14 |                    3 |                    4 |
|      6 |                  11 |                   9 |                    3 |                    7 |
|      8 |                   5 |                   6 |                  nan |                    2 |
|      5 |                   8 |                   2 |                  nan |                    1 |
|      1 |                   3 |                   2 |                    1 |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   6 |                  69 |                  nan |                   22 |
|      3 |                  13 |                   1 |                    3 |                  nan |
|      4 |                   2 |                   1 |                    1 |                  nan |
|      8 |                 nan |                   2 |                  nan |                    1 |
|      5 |                   1 |                 nan |                    1 |                  nan |
|      6 |                 nan |                   1 |                    1 |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - LEARNING_FAIR_REPRESENTATIONS

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   5 |                 656 |                   10 |                  191 |
|      3 |                  23 |                  30 |                    4 |                   72 |
|      2 |                   2 |                  32 |                  nan |                   22 |
|      4 |                   3 |                  16 |                    1 |                   11 |
|      6 |                 nan |                  12 |                  nan |                   18 |
|      8 |                   2 |                   5 |                    1 |                    5 |
|      5 |                 nan |                   2 |                  nan |                    9 |
|      1 |                   1 |                   3 |                  nan |                    3 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                  68 |                    1 |                   28 |
|      3 |                   4 |                   3 |                    1 |                    9 |
|      4 |                   1 |                   2 |                  nan |                    1 |
|      8 |                 nan |                   2 |                  nan |                    1 |
|      5 |                 nan |                   1 |                  nan |                    1 |
|      6 |                 nan |                   2 |                  nan |                  nan |
|      2 |                 nan |                   1 |                  nan |                  nan |


____________________________________________________________________________________________________

PROCESSING METRICS

STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT

|    | method                        |   before_spd |   before_di |   after_spd |   after_di |   delta_di |   delta_spd |
|---:|:------------------------------|-------------:|------------:|------------:|-----------:|-----------:|------------:|
|  0 | reweighing                    |       -0.464 |       0.379 |       0     |      1     |      0.621 |       0.464 |
|  1 | disparate_impact_remover      |       -0.464 |       0.379 |      -0.464 |      0.379 |      0     |       0     |
|  2 | learning_fair_representations |       -0.464 |       0.379 |      -0.595 |      0.294 |     -0.085 |      -0.131 |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | ugpa  |                      0.324746 |                     0.324746 |                   0          |
|  1 | disparate_impact_remover      | ugpa  |                      0.324746 |                     0.315638 |                  -0.00910774 |
|  2 | learning_fair_representations | ugpa  |                      0.324746 |                     0.317772 |                  -0.00697366 |
|  3 | reweighing                    | zgpa  |                      0.910652 |                     0.910652 |                   0          |
|  4 | disparate_impact_remover      | zgpa  |                      0.910652 |                     0.128715 |                  -0.781937   |
|  5 | learning_fair_representations | zgpa  |                      0.910652 |                     8.34599  |                   7.43534    |
|  6 | reweighing                    | lsat  |                      7.4684   |                     7.4684   |                   0          |
|  7 | disparate_impact_remover      | lsat  |                      7.4684   |                     2.99607  |                  -4.47233    |
|  8 | learning_fair_representations | lsat  |                      7.4684   |                     6.24189  |                  -1.22651    |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | ugpa  |     0.03984 |    0.03984 |    0       |
|  1 | reweighing                    | zgpa  |     0.17039 |    0.17039 |    0       |
|  2 | reweighing                    | lsat  |     0.10254 |    0.10254 |    0       |
|  3 | disparate_impact_remover      | ugpa  |     0.03984 |    0.02558 |   -0.01426 |
|  4 | disparate_impact_remover      | zgpa  |     0.17039 |    0.11314 |   -0.05726 |
|  5 | disparate_impact_remover      | lsat  |     0.10254 |    0.08079 |   -0.02175 |
|  6 | learning_fair_representations | ugpa  |     0.03984 |    0.60145 |    0.5616  |
|  7 | learning_fair_representations | zgpa  |     0.17039 |    0.60599 |    0.4356  |
|  8 | learning_fair_representations | lsat  |     0.10254 |    0.60703 |    0.50449 |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | ugpa       | 0.0615821 |    0.0688482 |                  0.0768839 |                     0.0566843   |
|  1 | zgpa       | 0.506891  |    0.598569  |                  0.385423  |                     0.280869    |
|  2 | lsat       | 0.253352  |    0.204721  |                  0.240163  |                     0.220267    |
|  3 | race       | 0.109121  |    0.0337159 |                  0.206383  |                     0.000144897 |
|  4 | tier       | 0.0505807 |    0.0709863 |                  0.0677146 |                     0.241745    |
|  5 | fam_inc    | 0.0184738 |    0.02316   |                  0.0234326 |                     0.20029     |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.874043 |                   0.391026 |             0           |
| Reweighing |     0.874748 |                   0.391026 |            -0.000704141 |
| DIR        |     0.865954 |                   0.39011  |             0.00808968  |
| LFR        |     1        |                   0        |            -0.125957    |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.933275 |                            0.176471  |
| DIR Space      |               0.920983 |                            0.164179  |
| LFR Space      |               0.841089 |                            0.0842845 |


____________________________________________________________________________________________________