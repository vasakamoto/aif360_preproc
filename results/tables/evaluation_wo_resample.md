

STANDARD METRICS

|    | metrics                      |   raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------|------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_baseline_accuracy       | 0.948 |        0.948 |                      0.948 |                           0.948 |
|  1 | test_accuracy                | 0.95  |        0.948 |                      0.951 |                           0.946 |
|  2 | test_precision               | 0.95  |        0.948 |                      0.951 |                           0.948 |
|  3 | test_recall                  | 1     |        1     |                      0.999 |                           0.997 |
|  4 | test_f1                      | 0.974 |        0.973 |                      0.975 |                           0.972 |
|  5 | test_roc_auc                 | 0.871 |        0.868 |                      0.852 |                           0.656 |
|  6 | validation_baseline_accuracy | 0.945 |        0.945 |                      0.945 |                           0.945 |
|  7 | validation_accuracy          | 0.947 |        0.945 |                      0.946 |                           0.946 |
|  8 | validation_precision         | 0.947 |        0.945 |                      0.947 |                           0.947 |
|  9 | validation_recall            | 1     |        1     |                      0.999 |                           0.999 |
| 10 | validation_f1                | 0.973 |        0.971 |                      0.972 |                           0.972 |
| 11 | validation_roc_auc           | 0.881 |        0.876 |                      0.861 |                           0.624 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    2 |                   44 |
|  1 | REAL POSITIVE |                    0 |                  783 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX RAW

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   16 |                  371 |
|  1 | REAL POSITIVE |                    1 |                 7081 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    0 |                   46 |
|  1 | REAL POSITIVE |                    0 |                  783 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX REWEIGHING

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    0 |                  387 |
|  1 | REAL POSITIVE |                    0 |                 7082 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    2 |                   44 |
|  1 | REAL POSITIVE |                    1 |                  782 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX DISPARATE_IMPACT_REMOVER

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                   26 |                  361 |
|  1 | REAL POSITIVE |                    8 |                 7074 |


____________________________________________________________________________________________________

VALIDATION CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    2 |                   44 |
|  1 | REAL POSITIVE |                    1 |                  782 |


____________________________________________________________________________________________________

TEST CONFUSION MATRIX LEARNING_FAIR_REPRESENTATIONS

|    | /             |   PREDICTED NEGATIVE |   PREDICTED POSITIVE |
|---:|:--------------|---------------------:|---------------------:|
|  0 | REAL NEGATIVE |                    3 |                  384 |
|  1 | REAL POSITIVE |                   22 |                 7060 |


____________________________________________________________________________________________________

FAIRNESS METRICS

|    | metrics                                  |    raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------------------------------------|-------:|-------------:|---------------------------:|--------------------------------:|
|  0 | test_statistical_parity_difference       | -0.023 |        0     |                     -0.058 |                          -0.018 |
|  1 | test_disparate_impact                    |  0.977 |        1     |                      0.942 |                           0.982 |
|  2 | test_equal_opportunity_difference        |  0     |        0     |                     -0.015 |                          -0.015 |
|  3 | test_average_odds_difference             | -0.051 |        0     |                     -0.118 |                          -0.021 |
|  4 | test_false_positive_rate_diff            | -0.102 |        0     |                     -0.222 |                          -0.028 |
|  5 | test_false_discovery_rate_diff           |  0.156 |        0.174 |                      0.138 |                           0.172 |
|  6 | validation_statistical_parity_difference | -0.03  |        0     |                     -0.045 |                           0.001 |
|  7 | validation_disparate_impact              |  0.97  |        1     |                      0.955 |                           1.001 |
|  8 | validation_equal_opportunity_difference  |  0     |        0     |                     -0.02  |                           0     |
|  9 | validation_average_odds_difference       | -0.067 |        0     |                     -0.076 |                           0.017 |
| 10 | validation_false_positive_rate_diff      | -0.133 |        0     |                     -0.133 |                           0.034 |
| 11 | validation_false_discovery_rate_diff     |  0.163 |        0.187 |                      0.167 |                           0.189 |


____________________________________________________________________________________________________

CONSUFION MATRIX - RAW

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                6026 |                  nan |                  205 |
|      3 |                  11 |                 346 |                  nan |                   80 |
|      2 |                   2 |                 278 |                  nan |                   20 |
|      6 |                   2 |                 144 |                    1 |                   23 |
|      4 |                 nan |                 123 |                  nan |                   19 |
|      8 |                 nan |                 101 |                  nan |                    8 |
|      5 |                   1 |                  36 |                  nan |                    7 |
|      1 |                 nan |                  27 |                  nan |                    9 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                 664 |                  nan |                   24 |
|      3 |                   2 |                  42 |                  nan |                   12 |
|      2 |                 nan |                  36 |                  nan |                    5 |
|      4 |                 nan |                  12 |                  nan |                    1 |
|      6 |                 nan |                  13 |                  nan |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                 nan |                   6 |                  nan |                    1 |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - REWEIGHING

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                6026 |                  nan |                  205 |
|      3 |                 nan |                 346 |                  nan |                   91 |
|      2 |                 nan |                 278 |                  nan |                   22 |
|      6 |                 nan |                 145 |                  nan |                   25 |
|      4 |                 nan |                 123 |                  nan |                   19 |
|      8 |                 nan |                 101 |                  nan |                    8 |
|      5 |                 nan |                  36 |                  nan |                    8 |
|      1 |                 nan |                  27 |                  nan |                    9 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                 664 |                  nan |                   24 |
|      3 |                 nan |                  42 |                  nan |                   14 |
|      2 |                 nan |                  36 |                  nan |                    5 |
|      4 |                 nan |                  12 |                  nan |                    1 |
|      6 |                 nan |                  13 |                  nan |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                 nan |                   6 |                  nan |                    1 |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - DISPARATE_IMPACT_REMOVER

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                6026 |                  nan |                  205 |
|      3 |                  21 |                 341 |                    5 |                   70 |
|      2 |                 nan |                 278 |                  nan |                   22 |
|      6 |                   2 |                 144 |                    1 |                   23 |
|      4 |                 nan |                 122 |                    1 |                   19 |
|      8 |                 nan |                 101 |                  nan |                    8 |
|      5 |                   3 |                  35 |                    1 |                    5 |
|      1 |                 nan |                  27 |                  nan |                    9 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                 664 |                  nan |                   24 |
|      3 |                   2 |                  41 |                    1 |                   12 |
|      2 |                 nan |                  36 |                  nan |                    5 |
|      4 |                 nan |                  12 |                  nan |                    1 |
|      6 |                 nan |                  13 |                  nan |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                 nan |                   6 |                  nan |                    1 |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

CONSUFION MATRIX - LEARNING_FAIR_REPRESENTATIONS

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                 nan |                6015 |                   11 |                  205 |
|      3 |                   3 |                 339 |                    7 |                   88 |
|      2 |                 nan |                 277 |                    1 |                   22 |
|      6 |                 nan |                 143 |                    2 |                   25 |
|      4 |                 nan |                 123 |                  nan |                   19 |
|      8 |                 nan |                 100 |                    1 |                    8 |
|      5 |                 nan |                  36 |                  nan |                    8 |
|      1 |                 nan |                  27 |                  nan |                    9 |

|   race |   abs_true_negative |   abs_true_positive |   abs_false_negative |   abs_false_positive |
|-------:|--------------------:|--------------------:|---------------------:|---------------------:|
|      7 |                   1 |                 664 |                  nan |                   23 |
|      3 |                 nan |                  42 |                  nan |                   14 |
|      2 |                 nan |                  36 |                  nan |                    5 |
|      4 |                   1 |                  11 |                    1 |                  nan |
|      6 |                 nan |                  13 |                  nan |                  nan |
|      8 |                 nan |                   7 |                  nan |                    1 |
|      1 |                 nan |                   6 |                  nan |                    1 |
|      5 |                 nan |                   3 |                  nan |                  nan |


____________________________________________________________________________________________________

PROCESSING METRICS

STATISTICAL PARITY DIFFERENCE AND DISPARATE IMPACT

|    | method                        |   before_spd |   before_di |   after_spd |   after_di |   delta_di |   delta_spd |
|---:|:------------------------------|-------------:|------------:|------------:|-----------:|-----------:|------------:|
|  0 | reweighing                    |       -0.187 |       0.807 |      -0     |      1     |      0.193 |       0.187 |
|  1 | disparate_impact_remover      |       -0.187 |       0.807 |      -0.187 |      0.807 |      0     |       0     |
|  2 | learning_fair_representations |       -0.187 |       0.807 |      -0.067 |      0.932 |      0.125 |       0.12  |


____________________________________________________________________________________________________

WASSERSTEIN DISTANCE

|    | method                        | var   |   wasserstein_distance_before |   wasserstein_distance_after |   wasserstein_distance_delta |
|---:|:------------------------------|:------|------------------------------:|-----------------------------:|-----------------------------:|
|  0 | reweighing                    | ugpa  |                      0.24694  |                     0.24694  |                    0         |
|  1 | disparate_impact_remover      | ugpa  |                      0.24694  |                     0.31547  |                    0.0685301 |
|  2 | learning_fair_representations | ugpa  |                      0.24694  |                     1.29091  |                    1.04397   |
|  3 | reweighing                    | zgpa  |                      0.862883 |                     0.862883 |                    0         |
|  4 | disparate_impact_remover      | zgpa  |                      0.862883 |                     0.263341 |                   -0.599542  |
|  5 | learning_fair_representations | zgpa  |                      0.862883 |                     1.51657  |                    0.653685  |
|  6 | reweighing                    | lsat  |                      5.77125  |                     5.77125  |                    0         |
|  7 | disparate_impact_remover      | lsat  |                      5.77125  |                     3.781    |                   -1.99025   |
|  8 | learning_fair_representations | lsat  |                      5.77125  |                     9.68358  |                    3.91233   |


____________________________________________________________________________________________________

ATTRIBUTE-TARGET MUTUAL INFORMATION

|    | method                        | var   |   mi_before |   mi_after |   mi_delta |
|---:|:------------------------------|:------|------------:|-----------:|-----------:|
|  0 | reweighing                    | ugpa  |     0.00664 |    0.00664 |    0       |
|  1 | reweighing                    | zgpa  |     0.0445  |    0.0445  |    0       |
|  2 | reweighing                    | lsat  |     0.02614 |    0.02614 |    0       |
|  3 | disparate_impact_remover      | ugpa  |     0.00664 |    0.00881 |    0.00217 |
|  4 | disparate_impact_remover      | zgpa  |     0.0445  |    0.03212 |   -0.01237 |
|  5 | disparate_impact_remover      | lsat  |     0.02614 |    0.02147 |   -0.00467 |
|  6 | learning_fair_representations | ugpa  |     0.00664 |    0.22292 |    0.21628 |
|  7 | learning_fair_representations | zgpa  |     0.0445  |    0.22263 |    0.17813 |
|  8 | learning_fair_representations | lsat  |     0.02614 |    0.22291 |    0.19677 |


____________________________________________________________________________________________________

FEATURE IMPORTANCES

|    | features   |       raw |   reweighing |   disparate_impact_remover |   learning_fair_representations |
|---:|:-----------|----------:|-------------:|---------------------------:|--------------------------------:|
|  0 | ugpa       | 0.0732124 |    0.0767032 |                  0.0869131 |                     0.209983    |
|  1 | zgpa       | 0.465282  |    0.567595  |                  0.441855  |                     0.229757    |
|  2 | lsat       | 0.260626  |    0.170516  |                  0.214318  |                     0.15008     |
|  3 | race       | 0.101543  |    0.0851878 |                  0.151739  |                     0.000215659 |
|  4 | tier       | 0.0779557 |    0.0750009 |                  0.0820149 |                     0.220013    |
|  5 | fam_inc    | 0.0213807 |    0.024997  |                  0.0231593 |                     0.189951    |


____________________________________________________________________________________________________

Delta_AUC_Global_Loss

|            |   AUC_Global |   Delta_AUC_Interseccional |   Delta_AUC_Global_Loss |
|:-----------|-------------:|---------------------------:|------------------------:|
| Baseline   |     0.871147 |                   0.4      |              0          |
| Reweighing |     0.867914 |                   0.446667 |              0.00323308 |
| DIR        |     0.8666   |                   0.53125  |              0.00454659 |
| LFR        |     1        |                   0        |             -0.128853   |


____________________________________________________________________________________________________

Adversarial_Accuracy

|                |   Adversarial_Accuracy |   Information_Leakage_Above_Baseline |
|:---------------|-----------------------:|-------------------------------------:|
| Baseline Space |               0.991967 |                            0.157719  |
| DIR Space      |               0.991833 |                            0.157585  |
| LFR Space      |               0.862231 |                            0.0279823 |


____________________________________________________________________________________________________