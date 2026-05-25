

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.678 |        0.678 |                      0.678 |                           0.678 |
|  1 | test_accuracy                | 0.803 |        0.815 |                      0.783 |                           0.695 |
|  2 | test_precision               | 0.831 |        0.845 |                      0.784 |                           0.695 |
|  3 | test_recall                  | 0.891 |        0.89  |                      0.938 |                           0.979 |
|  4 | test_f1                      | 0.86  |        0.867 |                      0.854 |                           0.813 |
|  5 | test_roc_auc                 | 0.87  |        0.87  |                      0.84  |                           0.631 |
|  6 | validation_baseline_accuracy | 0.643 |        0.643 |                      0.643 |                           0.643 |
|  7 | validation_accuracy          | 0.754 |        0.794 |                      0.77  |                           0.667 |
|  8 | validation_precision         | 0.791 |        0.816 |                      0.765 |                           0.664 |
|  9 | validation_recall            | 0.84  |        0.877 |                      0.926 |                           0.975 |
| 10 | validation_f1                | 0.814 |        0.845 |                      0.838 |                           0.79  |
| 11 | validation_roc_auc           | 0.881 |        0.896 |                      0.841 |                           0.619 |


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
|  0 | REAL NEGATIVE |                   29 |                   16 |
|  1 | REAL POSITIVE |                   10 |                   71 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                  241 |                  126 |
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
|  0 | REAL NEGATIVE |                  168 |                  199 |
|  1 | REAL POSITIVE |                   48 |                  724 |


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
|  0 | test_statistical_parity_difference       | -0.721 |       -0.549 |                     -0.817 |                          -0.169 |
|  1 | test_disparate_impact                    |  0.145 |        0.315 |                      0.13  |                           0.827 |
|  2 | test_equal_opportunity_difference        | -0.653 |       -0.348 |                     -0.672 |                          -0.087 |
|  3 | test_average_odds_difference             | -0.574 |       -0.331 |                     -0.716 |                          -0.135 |
|  4 | test_false_positive_rate_diff            | -0.495 |       -0.315 |                     -0.759 |                          -0.183 |
|  5 | test_false_discovery_rate_diff           |  0.227 |        0.267 |                      0.122 |                           0.467 |
|  6 | validation_statistical_parity_difference | -0.842 |       -0.644 |                     -0.878 |                          -0.253 |
|  7 | validation_disparate_impact              |  0     |        0.197 |                      0.057 |                           0.744 |
|  8 | validation_equal_opportunity_difference  | -0.931 |       -0.303 |                     -0.786 |                          -0.186 |
|  9 | validation_average_odds_difference       | -0.776 |       -0.427 |                     -0.79  |                          -0.236 |
| 10 | validation_false_positive_rate_diff      | -0.621 |       -0.552 |                     -0.793 |                          -0.286 |
| 11 | validation_false_discovery_rate_diff     | -0.212 |       -0.198 |                     -0.245 |                           0.424 |


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
|      7 |                 103 |                 612 |                   54 |                   93 |
|      3 |                  82 |                  17 |                   17 |                   13 |
|      2 |                  15 |                  26 |                    6 |                    9 |
|      4 |                  10 |                  14 |                    3 |                    4 |
|      6 |                  14 |                   9 |                    3 |                    4 |
|      8 |                   6 |                   4 |                    2 |                    1 |
|      5 |                   8 |                   2 |                  nan |                    1 |
|      1 |                   3 |                   3 |                  nan |                    1 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                  13 |                  63 |                    6 |                   15 |
|      3 |                  13 |                   2 |                    2 |                  nan |
|      4 |                   2 |                   2 |                  nan |                  nan |
|      8 |                 nan |                   1 |                    1 |                    1 |
|      5 |                   1 |                   1 |                  nan |                  nan |
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
|  0 | reweighing                    |        -0.46 |        0.38 |       0     |      1     |      0.62  |       0.46  |
|  1 | disparate_impact_remover      |        -0.46 |        0.38 |      -0.46  |      0.38  |      0     |       0     |
|  2 | learning_fair_representations |        -0.46 |        0.38 |      -0.604 |      0.313 |     -0.067 |      -0.144 |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | zgpa  |                      0.910652 |                     0.910652 |                     0        |
|  1 | disparate_impact_remover      | zgpa  |                      0.910652 |                     0.128715 |                    -0.781937 |
|  2 | learning_fair_representations | zgpa  |                      0.910652 |                     6.20097  |                     5.29032  |
|  3 | reweighing                    | lsat  |                      7.4684   |                     7.4684   |                     0        |
|  4 | disparate_impact_remover      | lsat  |                      7.4684   |                     2.99607  |                    -4.47233  |
|  5 | learning_fair_representations | lsat  |                      7.4684   |                     4.34702  |                    -3.12138  |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | zgpa  |     0.17775 |    0.17775 |    0       |
|  1 | reweighing                    | lsat  |     0.11445 |    0.11445 |    0       |
|  2 | disparate_impact_remover      | zgpa  |     0.17775 |    0.09113 |   -0.08662 |
|  3 | disparate_impact_remover      | lsat  |     0.11445 |    0.09644 |   -0.01801 |
|  4 | learning_fair_representations | zgpa  |     0.17775 |    0.56015 |    0.38241 |
|  5 | learning_fair_representations | lsat  |     0.11445 |    0.56286 |    0.4484  |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | zgpa       | 0.535403  |    0.62972   |                  0.424197  |                      0.290682   |
|  1 | lsat       | 0.2785    |    0.22792   |                  0.233884  |                      0.311246   |
|  2 | race       | 0.103834  |    0.0377615 |                  0.230417  |                      0.00991221 |
|  3 | tier       | 0.0600389 |    0.0777539 |                  0.0812329 |                      0.300128   |
|  4 | fam_inc    | 0.0222247 |    0.0268449 |                  0.0302691 |                      0.0880317  |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.870466 |                   0.371429 |             0           |
| Reweighing |     0.86991  |                   0.349206 |             0.000555901 |
| DIR        |     0.862933 |                   0.406349 |             0.00753378  |
| LFR        |     0.999996 |                   0        |            -0.129529    |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.928007 |                             0.171203 |
| DIR Space      |               0.922739 |                             0.165935 |
| LFR Space      |               0.865672 |                             0.108867 |


____________________________________________________________________________________________________