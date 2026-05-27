

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.948 |        0.948 |                      0.948 |                           0.948 |
|  1 | test_accuracy                | 0.894 |        0.887 |                      0.919 |                           0.912 |
|  2 | test_precision               | 0.972 |        0.973 |                      0.966 |                           0.95  |
|  3 | test_recall                  | 0.915 |        0.905 |                      0.948 |                           0.957 |
|  4 | test_f1                      | 0.943 |        0.938 |                      0.957 |                           0.953 |
|  5 | test_roc_auc                 | 0.868 |        0.861 |                      0.85  |                           0.519 |
|  6 | validation_baseline_accuracy | 0.945 |        0.945 |                      0.945 |                           0.945 |
|  7 | validation_accuracy          | 0.908 |        0.899 |                      0.923 |                           0.901 |
|  8 | validation_precision         | 0.976 |        0.974 |                      0.966 |                           0.949 |
|  9 | validation_recall            | 0.926 |        0.917 |                      0.951 |                           0.946 |
| 10 | validation_f1                | 0.95  |        0.945 |                      0.959 |                           0.948 |
| 11 | validation_roc_auc           | 0.886 |        0.882 |                      0.863 |                           0.538 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   28 |                   18 |
|  1 | REAL POSITIVE |                   58 |                  725 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  198 |                  189 |
|  1 | REAL POSITIVE |                  599 |                 6483 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   27 |                   19 |
|  1 | REAL POSITIVE |                   65 |                  718 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  210 |                  177 |
|  1 | REAL POSITIVE |                  670 |                 6412 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   20 |                   26 |
|  1 | REAL POSITIVE |                   38 |                  745 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  151 |                  236 |
|  1 | REAL POSITIVE |                  369 |                 6713 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    6 |                   40 |
|  1 | REAL POSITIVE |                   42 |                  741 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   31 |                  356 |
|  1 | REAL POSITIVE |                  305 |                 6777 |


____________________________________________________________________________________________________

FAIRNESS METRICS

|    | metrics                                  |    raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------------------|-------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_statistical_parity_difference       | -0.526 |       -0.323 |                     -0.622 |                          -0.024 |
|  1 | test_disparate_impact                    |  0.442 |        0.646 |                      0.369 |                           0.975 |
|  2 | test_equal_opportunity_difference        | -0.462 |       -0.246 |                     -0.561 |                          -0.022 |
|  3 | test_average_odds_difference             | -0.505 |       -0.286 |                     -0.661 |                          -0.004 |
|  4 | test_false_positive_rate_diff            | -0.548 |       -0.327 |                     -0.761 |                           0.014 |
|  5 | test_false_discovery_rate_diff           |  0.044 |        0.067 |                      0.038 |                           0.173 |
|  6 | validation_statistical_parity_difference | -0.537 |       -0.279 |                     -0.574 |                          -0.05  |
|  7 | validation_disparate_impact              |  0.432 |        0.696 |                      0.416 |                           0.947 |
|  8 | validation_equal_opportunity_difference  | -0.452 |       -0.249 |                     -0.48  |                          -0.066 |
|  9 | validation_average_odds_difference       | -0.486 |       -0.098 |                     -0.621 |                           0.02  |
| 10 | validation_false_positive_rate_diff      | -0.52  |        0.053 |                     -0.761 |                           0.106 |
| 11 | validation_false_discovery_rate_diff     |  0.012 |        0.149 |                      0.004 |                           0.202 |


____________________________________________________________________________________________________

CONSUFION MATRIX - RAW

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  57 |                5769 |                  257 |                  148 |
|      3 |                  82 |                 158 |                  188 |                    9 |
|      2 |                  14 |                 225 |                   53 |                    8 |
|      6 |                  17 |                 119 |                   26 |                    8 |
|      4 |                  12 |                  84 |                   39 |                    7 |
|      8 |                   5 |                  86 |                   15 |                    3 |
|      5 |                   7 |                  24 |                   12 |                    1 |
|      1 |                   4 |                  18 |                    9 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   9 |                 642 |                   22 |                   15 |
|      3 |                  13 |                  18 |                   24 |                    1 |
|      2 |                   3 |                  31 |                    5 |                    2 |
|      4 |                   1 |                   9 |                    3 |                  nan |
|      6 |                 nan |                  10 |                    3 |                  nan |
|      8 |                   1 |                   7 |                  nan |                  nan |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - REWEIGHING

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  82 |                5616 |                  410 |                  123 |
|      3 |                  70 |                 231 |                  115 |                   21 |
|      2 |                  14 |                 218 |                   60 |                    8 |
|      6 |                  17 |                 121 |                   24 |                    8 |
|      4 |                  10 |                  94 |                   29 |                    9 |
|      8 |                   6 |                  85 |                   16 |                    2 |
|      5 |                   7 |                  29 |                    7 |                    1 |
|      1 |                   4 |                  18 |                    9 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  13 |                 626 |                   38 |                   11 |
|      3 |                   7 |                  27 |                   15 |                    7 |
|      2 |                   4 |                  29 |                    7 |                    1 |
|      4 |                   1 |                  11 |                    1 |                  nan |
|      6 |                 nan |                  10 |                    3 |                  nan |
|      8 |                   1 |                   7 |                  nan |                  nan |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - DISPARATE_IMPACT_REMOVER

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  16 |                6002 |                   24 |                  189 |
|      3 |                  84 |                 134 |                  212 |                    7 |
|      2 |                  11 |                 233 |                   45 |                   11 |
|      6 |                  16 |                 129 |                   16 |                    9 |
|      4 |                  12 |                  80 |                   43 |                    7 |
|      8 |                   1 |                  94 |                    7 |                    7 |
|      5 |                   7 |                  25 |                   11 |                    1 |
|      1 |                   4 |                  16 |                   11 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   2 |                 661 |                    3 |                   22 |
|      3 |                  13 |                  18 |                   24 |                    1 |
|      2 |                   3 |                  32 |                    4 |                    2 |
|      4 |                   1 |                   8 |                    4 |                  nan |
|      6 |                 nan |                  11 |                    2 |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - LEARNING_FAIR_REPRESENTATIONS

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                6026 |                  nan |                  205 |
|      3 |                 nan |                 346 |                  nan |                   91 |
|      2 |                  22 |                 nan |                  278 |                  nan |
|      6 |                 nan |                 145 |                  nan |                   25 |
|      4 |                 nan |                 123 |                  nan |                   19 |
|      8 |                 nan |                 101 |                  nan |                    8 |
|      5 |                 nan |                  36 |                  nan |                    8 |
|      1 |                   9 |                 nan |                   27 |                  nan |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                 664 |                  nan |                   24 |
|      3 |                 nan |                  42 |                  nan |                   14 |
|      2 |                   5 |                 nan |                   36 |                  nan |
|      4 |                 nan |                  12 |                  nan |                    1 |
|      6 |                 nan |                  13 |                  nan |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                   1 |                 nan |                    6 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

PROCESSING METRICS

STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT

|    | method                        |   before_spd |   before_di |   after_spd |   after_di |   delta_di |   delta_spd |
|---:|:------------------------------|-------------:|------------:|------------:|-----------:|-----------:|------------:|
|  0 | reweighing                    |       -0.444 |       0.461 |      -0     |      1     |      0.539 |       0.444 |
|  1 | disparate_impact_remover      |       -0.444 |       0.461 |      -0.444 |      0.461 |      0     |       0     |
|  2 | learning_fair_representations |       -0.444 |       0.461 |      -0.631 |      0.319 |     -0.142 |      -0.187 |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | ugpa  |                      0.295586 |                    0.295586  |                    0         |
|  1 | disparate_impact_remover      | ugpa  |                      0.295586 |                    0.248481  |                   -0.0471049 |
|  2 | learning_fair_representations | ugpa  |                      0.295586 |                    1.3854    |                    1.08981   |
|  3 | reweighing                    | zgpa  |                      0.878162 |                    0.878162  |                    0         |
|  4 | disparate_impact_remover      | zgpa  |                      0.878162 |                    0.0401638 |                   -0.837998  |
|  5 | learning_fair_representations | zgpa  |                      0.878162 |                    9.36258   |                    8.48442   |
|  6 | reweighing                    | lsat  |                      6.91051  |                    6.91051   |                    0         |
|  7 | disparate_impact_remover      | lsat  |                      6.91051  |                    2.24983   |                   -4.66068   |
|  8 | learning_fair_representations | lsat  |                      6.91051  |                    5.78455   |                   -1.12596   |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | ugpa  |     0.07219 |    0.07219 |    0       |
|  1 | reweighing                    | zgpa  |     0.18813 |    0.18813 |    0       |
|  2 | reweighing                    | lsat  |     0.12732 |    0.12732 |    0       |
|  3 | disparate_impact_remover      | ugpa  |     0.07219 |    0.05147 |   -0.02071 |
|  4 | disparate_impact_remover      | zgpa  |     0.18813 |    0.08742 |   -0.10071 |
|  5 | disparate_impact_remover      | lsat  |     0.12732 |    0.08233 |   -0.04499 |
|  6 | learning_fair_representations | ugpa  |     0.07219 |    0.66016 |    0.58798 |
|  7 | learning_fair_representations | zgpa  |     0.18813 |    0.67699 |    0.48887 |
|  8 | learning_fair_representations | lsat  |     0.12732 |    0.67628 |    0.54896 |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | ugpa       | 0.0944058 |    0.111326  |                  0.109313  |                     0.0557374   |
|  1 | zgpa       | 0.436133  |    0.496881  |                  0.30378   |                     0.263786    |
|  2 | lsat       | 0.265409  |    0.200181  |                  0.208702  |                     0.21242     |
|  3 | race       | 0.111836  |    0.0694651 |                  0.251048  |                     0.305872    |
|  4 | tier       | 0.0690542 |    0.0870648 |                  0.103553  |                     0.000780948 |
|  5 | fam_inc    | 0.0231622 |    0.0350822 |                  0.0236042 |                     0.161404    |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.867676 |                0.433333    |              0          |
| Reweighing |     0.861354 |                0.406667    |              0.00632185 |
| DIR        |     0.85453  |                0.53125     |              0.0131457  |
| LFR        |     0.999998 |                7.69734e-06 |             -0.132322   |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.943232 |                            0.108984  |
| DIR Space      |               0.939885 |                            0.105637  |
| LFR Space      |               0.870398 |                            0.0361494 |


____________________________________________________________________________________________________