

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.948 |        0.948 |                      0.948 |                           0.948 |
|  1 | test_accuracy                | 0.854 |        0.829 |                      0.905 |                           0.052 |
|  2 | test_precision               | 0.979 |        0.979 |                      0.968 |                           0     |
|  3 | test_recall                  | 0.865 |        0.837 |                      0.93  |                           0     |
|  4 | test_f1                      | 0.918 |        0.903 |                      0.949 |                           0     |
|  5 | test_roc_auc                 | 0.87  |        0.862 |                      0.842 |                           0.5   |
|  6 | validation_baseline_accuracy | 0.945 |        0.945 |                      0.945 |                           0.945 |
|  7 | validation_accuracy          | 0.864 |        0.848 |                      0.911 |                           0.055 |
|  8 | validation_precision         | 0.981 |        0.98  |                      0.967 |                           0     |
|  9 | validation_recall            | 0.872 |        0.857 |                      0.937 |                           0     |
| 10 | validation_f1                | 0.924 |        0.914 |                      0.952 |                           0     |
| 11 | validation_roc_auc           | 0.88  |        0.869 |                      0.842 |                           0.5   |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   33 |                   13 |
|  1 | REAL POSITIVE |                  100 |                  683 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  254 |                  133 |
|  1 | REAL POSITIVE |                  959 |                 6123 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   32 |                   14 |
|  1 | REAL POSITIVE |                  112 |                  671 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  262 |                  125 |
|  1 | REAL POSITIVE |                 1152 |                 5930 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   21 |                   25 |
|  1 | REAL POSITIVE |                   49 |                  734 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  170 |                  217 |
|  1 | REAL POSITIVE |                  496 |                 6586 |


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
|  0 | test_statistical_parity_difference       | -0.602 |       -0.288 |                     -0.704 |                               0 |
|  1 | test_disparate_impact                    |  0.329 |        0.659 |                      0.276 |                             nan |
|  2 | test_equal_opportunity_difference        | -0.55  |       -0.205 |                     -0.666 |                               0 |
|  3 | test_average_odds_difference             | -0.512 |       -0.213 |                     -0.685 |                               0 |
|  4 | test_false_positive_rate_diff            | -0.474 |       -0.22  |                     -0.704 |                               0 |
|  5 | test_false_discovery_rate_diff           |  0.013 |        0.053 |                      0.05  |                               0 |
|  6 | validation_statistical_parity_difference | -0.55  |       -0.269 |                     -0.693 |                               0 |
|  7 | validation_disparate_impact              |  0.388 |        0.687 |                      0.294 |                             nan |
|  8 | validation_equal_opportunity_difference  | -0.487 |       -0.174 |                     -0.615 |                               0 |
|  9 | validation_average_odds_difference       | -0.417 |       -0.177 |                     -0.721 |                               0 |
| 10 | validation_false_positive_rate_diff      | -0.347 |       -0.179 |                     -0.828 |                               0 |
| 11 | validation_false_discovery_rate_diff     |  0.025 |        0.059 |                     -0.034 |                               0 |


____________________________________________________________________________________________________

CONSUFION MATRIX - RAW

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  95 |                5544 |                  482 |                  110 |
|      3 |                  89 |                 115 |                  231 |                    2 |
|      2 |                  14 |                 204 |                   74 |                    8 |
|      6 |                  19 |                  95 |                   50 |                    6 |
|      4 |                  17 |                  55 |                   68 |                    2 |
|      8 |                   6 |                  77 |                   24 |                    2 |
|      5 |                   8 |                  18 |                   18 |                  nan |
|      1 |                   6 |                  15 |                   12 |                    3 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  13 |                 617 |                   47 |                   11 |
|      3 |                  13 |                  16 |                   26 |                    1 |
|      2 |                   4 |                  26 |                   10 |                    1 |
|      4 |                   1 |                   5 |                    7 |                  nan |
|      6 |                 nan |                   8 |                    5 |                  nan |
|      8 |                   1 |                   5 |                    2 |                  nan |
|      1 |                   1 |                   4 |                    2 |                  nan |
|      5 |                 nan |                   2 |                    1 |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - REWEIGHING

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 123 |                5204 |                  822 |                   82 |
|      3 |                  76 |                 228 |                  118 |                   15 |
|      2 |                  12 |                 222 |                   56 |                   10 |
|      6 |                  18 |                  92 |                   53 |                    7 |
|      4 |                  15 |                  70 |                   53 |                    4 |
|      8 |                   6 |                  74 |                   27 |                    2 |
|      5 |                   7 |                  20 |                   16 |                    1 |
|      1 |                   5 |                  20 |                    7 |                    4 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  16 |                 586 |                   78 |                    8 |
|      3 |                  11 |                  28 |                   14 |                    3 |
|      2 |                   2 |                  30 |                    6 |                    3 |
|      4 |                   1 |                   7 |                    5 |                  nan |
|      6 |                 nan |                   8 |                    5 |                  nan |
|      8 |                   1 |                   4 |                    3 |                  nan |
|      1 |                   1 |                   5 |                    1 |                  nan |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - DISPARATE_IMPACT_REMOVER

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  32 |                5942 |                   84 |                  173 |
|      3 |                  86 |                  92 |                  254 |                    5 |
|      2 |                  12 |                 229 |                   49 |                   10 |
|      6 |                  16 |                 129 |                   16 |                    9 |
|      4 |                  12 |                  67 |                   56 |                    7 |
|      8 |                   1 |                  91 |                   10 |                    7 |
|      5 |                   7 |                  21 |                   15 |                    1 |
|      1 |                   4 |                  15 |                   12 |                    5 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   3 |                 660 |                    4 |                   21 |
|      3 |                  14 |                  13 |                   29 |                  nan |
|      2 |                   2 |                  31 |                    5 |                    3 |
|      4 |                   1 |                   7 |                    5 |                  nan |
|      6 |                 nan |                  10 |                    3 |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                   1 |                   4 |                    2 |                  nan |
|      5 |                 nan |                   2 |                    1 |                  nan |


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
|  0 | reweighing                    |       -0.483 |       0.356 |       0     |      1     |      0.644 |       0.483 |
|  1 | disparate_impact_remover      |       -0.483 |       0.356 |      -0.483 |      0.356 |      0     |       0     |
|  2 | learning_fair_representations |       -0.483 |       0.356 |      -0.677 |      0.242 |     -0.114 |      -0.194 |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | ugpa  |                      0.308819 |                     0.308819 |                    0         |
|  1 | disparate_impact_remover      | ugpa  |                      0.308819 |                     0.290046 |                   -0.0187727 |
|  2 | learning_fair_representations | ugpa  |                      0.308819 |                     0.821488 |                    0.512669  |
|  3 | reweighing                    | zgpa  |                      0.97886  |                     0.97886  |                    0         |
|  4 | disparate_impact_remover      | zgpa  |                      0.97886  |                     0.150138 |                   -0.828723  |
|  5 | learning_fair_representations | zgpa  |                      0.97886  |                     8.03622  |                    7.05736   |
|  6 | reweighing                    | lsat  |                      7.72161  |                     7.72161  |                    0         |
|  7 | disparate_impact_remover      | lsat  |                      7.72161  |                     3.33066  |                   -4.39096   |
|  8 | learning_fair_representations | lsat  |                      7.72161  |                     4.50225  |                   -3.21937   |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | ugpa  |     0.02384 |    0.02384 |    0       |
|  1 | reweighing                    | zgpa  |     0.20757 |    0.20757 |    0       |
|  2 | reweighing                    | lsat  |     0.10569 |    0.10569 |    0       |
|  3 | disparate_impact_remover      | ugpa  |     0.02384 |    0.01892 |   -0.00493 |
|  4 | disparate_impact_remover      | zgpa  |     0.20757 |    0.11682 |   -0.09075 |
|  5 | disparate_impact_remover      | lsat  |     0.10569 |    0.06381 |   -0.04188 |
|  6 | learning_fair_representations | ugpa  |     0.02384 |    0.55529 |    0.53144 |
|  7 | learning_fair_representations | zgpa  |     0.20757 |    0.5601  |    0.35253 |
|  8 | learning_fair_representations | lsat  |     0.10569 |    0.55933 |    0.45364 |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | ugpa       | 0.0678812 |    0.0692307 |                  0.0899297 |                      0.121259   |
|  1 | zgpa       | 0.54112   |    0.637638  |                  0.416783  |                      0.308193   |
|  2 | lsat       | 0.206243  |    0.167736  |                  0.166052  |                      0.194527   |
|  3 | race       | 0.123057  |    0.0398373 |                  0.248554  |                      0.0775101  |
|  4 | tier       | 0.0383429 |    0.0566312 |                  0.0540084 |                      0.00072624 |
|  5 | fam_inc    | 0.0233554 |    0.0289264 |                  0.0246725 |                      0.297784   |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.869639 |                  0.455197  |              0          |
| Reweighing |     0.861572 |                  0.46      |              0.00806682 |
| DIR        |     0.854331 |                  0.65625   |              0.0153083  |
| LFR        |     0.999986 |                  0.0001485 |             -0.130347   |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.936939 |                            0.102691  |
| DIR Space      |               0.936939 |                            0.102691  |
| LFR Space      |               0.87977  |                            0.0455215 |


____________________________________________________________________________________________________