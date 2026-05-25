
# SOURCE

The original dataset is quite annoying to find, so I used the first one that I found 
it, the kaggle one (https://www.kaggle.com/datasets/danofer/law-school-admissions-bar-passage)
which have some processed data in it. For this analysis most of the processed features
will not be used, so it does not make that much difference between using the original
one (I hope). Also, doing a superficial research about this dataset, most of datasets
that I found it (https://github.com/tailequy/fairness_dataset/blob/main/Law_school/law_dataset.arff;
aifairness360 embedded dataset; yeah, I didn't look that much for it) have less features
(more specifically, does not have age related data in it, neither nominal data which 
makes a little inconvinient to understand properly what some data means, for example
race).


# DATA INSPECTION

First, some skimming over the dataset was held to identify variables, because most of
them weren't described in the dataset, some of them were appended after some processing
by the author that there is no necessity of analysis over it. After that, the "raw" data
was selected to conduct the analysis. Some other variables were discarded also, because 
they have no analytical significance (like grad that is a constant and ID which is an
unique identifier for the instance).


## VARIABLE IDENTIFICATION

There are no description for all columns, based on the original article and other EDAs,
was possible to identify and describe most columns:

 
| **variable**            | **variable type** | **data type** | **description**                                       |
|:------------------------|:------------------|:--------------|:------------------------------------------------------|
| DOB_yr                  | discrete          | integer       | candidate birth year                                  |
| Dropout                 | binary            | integer       | if candidate droped from law school                   | 
| ID                      | discrete          | integer       | instance unique identifier                            |
| age                     | discrete          | integer       | should be age, but the values are negative            |
| asian                   | binary            | integer       | one hot encoded from race for asian students          |
| bar                     | nominal           | string        | bar approval discriminated by attempt                 |
| bar1                    | binary            | integer       | bar approval on first attempt                         |
| bar1_yr                 | discrete          | integer       | difference between age and DOB_yr                     |
| bar2                    | binary            | integer       | bar approval for both attempts                        |
| bar2_yr                 | discrete          | integer       | year of passage in the bar exam                       |
| bar_passed              | binary            | boolean       | boolean for bar approvation                           |
| black                   | binary            | integer       | one hot encoded from race for black students          |
| cluster                 | ordinal           | integer       | reordered tier classification                         |
| decile1                 | ordinal           | integer       | ranking by gpa at first year                          |
| decile1b                | ordinal           | integer       |                                                       |
| decile3                 | ordinal           | integer       | ranking by gpa at third year                          |
| dnn_bar_pass_prediction | continuous        | float         | deep neural networks prediction                       |
| fam_inc                 | ordinal           | integer       | grouping by family income                             |
| fulltime                | binary            | integer       | boolean for student time dedication                   |
| gender                  | nominal           | string        | candidate gender                                      |
| gpa                     | continuous        | float         | probabily same as ugpa                                |
| grad                    | nominal           | string        | not sure                                              |
| hisp                    | binary            | integer       | one hot encoded from race for hispanic students       |
| index6040               | continuous        | float         | syntetic variable from gpa and lsat                   |
| indxgrp                 | nominal           | string        | categorization for index6040                          |
| indxgrp2                | nominal           | string        | categorization for index6040, more groups             |
| lsat                    | continuous        | float         | score from law school admission teste                 |
| male                    | binary            | integer       | one hot encoded from gender                           |
| other                   | binary            | integer       | one hot encoded from race for other ethinicities      |
| parttime                | binary            | integer       | inverse of fulltime                                   |
| pass_bar                | binary            | boolean       | boolean for student approvation on bar exam           |
| race                    | ordinal           | integer       | ordinal hot encode for students ethnicity             |
| race1                   | nominal           | string        | nominal classification for students ethnicity         |
| race2                   | nominal           | string        | grouped nominal classification for students ethnicity |
| sex                     | binary            | integer       | ordinal hot encoded from gender                       |
| tier                    | ordinal           | integer       | law school ranking                                    |
| ugpa                    | continuous        | float         | undergraduate general point average                   |
| zfygpa                  | continuous        | float         | z-score for first year GPA                            |
| zgpa                    | continuous        | float         | z-score for law school GPA                            |


## DROPABLE COLUMNS

Knowing that this dataset has some processed data already, like one hot encoded features,
unique identifiers, constants, redundant data and so on, it has no analytical significance.

| **variable**            | **justification**                                       |
| :---------------------- | :-------------------------------------------------------|
| ID                      | unique values: sample identifier                        |
| Dropout                 | constant: almost constant, 99.999% "NO"                 |
| decile3                 | transformed: ranking by gpa                             |
| decile1                 | transformed: ranking by zfygpa                          |
| decile1b                | mostly equal to decile1                                 |
| grad                    | constant: almost constant, 99.999% "Y"                  |
| cluster                 | redundant: tier rearranged                              |
| parttime                | redundant: inverse of fulltime                          |
| male                    | redundant: same as sex                                  |
| gender                  | redundant: same as sex                                  |
| race1                   | redundant: same as race                                 |
| race2                   | redundant: grouping from race                           |
| asian                   | hotencoded: from race                                   |
| black                   | hotencoded: from race                                   |
| hisp                    | hotencoded: from race                                   |
| other                   | hotencoded: from race                                   |
| bar_passed              | redundant: same as pass_bar                             |
| index6040               | transformed: syntetic variable from lsat and gpa        |
| indxgrp                 | redundat: categorization of indx6040                    |
| indxgrp2                | redundat: categorization of indx6040                    |
| bar                     | redundat: categorization of bar passage by attempts     |
| bar1                    | useless: approved at the first year                     |
| bar2                    | useless: approved at the second year                    |
| bar1_yr                 | redundat: difference between age and DOB_yr             |
| age                     | not sure what is exactly, strongly related with DOB_yr  |
| gpa                     | redundant: same as ugpa                                 |
| dnn_bar_pass_prediction | probability for approvation using deep neural networks  |


## SELECTED COLUMNS

All variables were present in the original dataset, with the addition of age only.

| **variable**            | **hypothesis for selection**                            |
| :---------------------- | :-------------------------------------------------------|
| sex                     | might be a source of bias if groups are not simetrical in distribution and variance                  |
| race                    | same reasoning for sex                                                                               |
| lsat                    | same as decile1                                                                                      |
| zfygpa                  | z-score for first year law school gpa, could be an estimator                                         |
| zgpa                    | z-score for law school gpa, same as decile3                                                          |
| fulltime                | intuitively, those who are full-time students tend to performe better at exams, more time to study   |
| fam_inc                 | same for sex                                                                                         |
| pass_bar                | target variable                                                                                      |
| tier                    | could either be a source of bias or estimator                                                        |
| ugpa                    | same as decile1                                                                                      |
| DOB_yr                  | can be used to find age of candidate                                                                 |
| bar2_yr                 | can be used to find age of candidate                                                                 |


# TRANSFORMATIONS

It was calculated age based on the date of birth and passage year, and then categorized
into 8 groups. There are so few samples with age bigger than 50 that these samples were
grouped together into one. Also, the ages between 20 and 30 were grouped into 3 instead
of 2 because the volume of samples in this range represents more than 50% of samples.
Also, race was reduced into white and non-white. This might inccor in some problems,
and the whole discussion would be problematic (assuming that every non-white group have



the same socioeconomic problems, and so on), nevertheless, the non-white group is already
so small that any sample removed have a great impact over it, leading to a more disbal


# UNIVARIATE ANALYSIS

In Random Forest models, variables with high variance and a normal distribution tend
to have the highest Feature Importance scores.

## TARGET VARIABLE

| pass_bar   |   abs_frequency |   rel_frequency |
|:-----------|----------------:|----------------:|
| 0          |            1169 |            5.22 |
| 1          |           21238 |           94.78 |
| <NA>       |               0 |            0    |

![Histogram for target variable](../../results/charts/univariate/hist_pass_bar.png)

There is a huge imbalance in the dataset as can be seen in the above table, 95% of 
samples reach the positive outcome. This distribution heavely favors a high accuracy
that have basically no discriminative power, with high false positive rate and a low
specificity (true negative rate).

Also, with a small sample for the negative outcome, there is more variance, which makes
more "unstable". Any sample have more weight in this class, which can change it drastically.
In such way that it can enhance bias or completly offuscate it.


## FEATURES

### AGE

At the same that age might favor a positive outcome with someone that have invested 
year into studying, the opposite can be true also, years without studying might make
someone more prone to a negative outcome.

| age          |   abs_frequency |   rel_frequency |
|:-------------|----------------:|----------------:|
| 23.0 - 30.75 |           17240 |           76.94 |
| 30.75 - 38.5 |            3576 |           15.96 |
| 38.5 - 46.25 |            1108 |            4.94 |
| 46.25 - 54.0 |             301 |            1.34 |
| 54.0 - 61.75 |              41 |            0.18 |
| 61.75 - 69.5 |              11 |            0.05 |
| 69.5 - 77.25 |               4 |            0.02 |
| 77.25 - 85.0 |               8 |            0.04 |
| nan          |              90 |            0.4  |

![Histogram for age](../../results/charts/univariate/hist_age.png)

Also have a huge imbalance, highly right-skewed, which makes older groups more instable.
Needs more information to conclude if might be a source of bias. Also, it would be better
to group together older groups into one to reduce this high potencial variance.


### FAMILY INCOME

Family income might be a proxy, because individuals with a higher family income have
a stronger tendency of having a more and better structure (study materials, time, etc.).
Also, might be a source of bias, favoring a positive outcome for higher income families.

| fam_inc   |   abs_frequency |   rel_frequency |
|:----------|----------------:|----------------:|
| 1         |             454 |            2.03 |
| 2         |            2183 |            9.74 |
| 3         |            7896 |           35.24 |
| 4         |            9771 |           43.61 |
| 5         |            1814 |            8.1  |
| <NA>      |             289 |            1.29 |

![Histogram for family income](../../results/charts/univariate/hist_fam_inc.png)

Most of individuals are situated in middle-upper family incomes, skewing data positively
(~85% of samples are in this middle-upper group).
Again, this makes the lower classes more susceptible to disturbances because of the low
number of samples.
The number of samples with null values are almost the same as the lowest group, which
is very far of being a good thing.


### FULLTIME 

Might be a proxy also, individuals who are not full time have other responsabilities
(job, family, etc.), which might indicate a vulnerable group.

| fulltime   |   abs_frequency |   rel_frequency |
|:-----------|----------------:|----------------:|
| 1          |           20653 |           92.17 |
| 2          |            1720 |            7.68 |
| <NA>       |              34 |            0.15 |

![Histogram for full-time](../../results/charts/univariate/hist_fulltime.png)

The same behavior for other imbalanced groups.


### LSAT

| lsat          |   abs_frequency |   rel_frequency |
|:--------------|----------------:|----------------:|
| 11.0 - 15.62  |               9 |            0.04 |
| 15.62 - 20.25 |              93 |            0.42 |
| 20.25 - 24.88 |             396 |            1.77 |
| 24.88 - 29.5  |            1680 |            7.5  |
| 29.5 - 34.12  |            4940 |           22.05 |
| 34.12 - 38.75 |            6448 |           28.78 |
| 38.75 - 43.38 |            6446 |           28.77 |
| 43.38 - 48.0  |            2394 |           10.68 |
| nan           |               0 |            0    |

![Histogram for lsat](../../results/charts/univariate/hist_lsat.png)

average = 36.76790735038158
median = 37.0
mode = 37.0
variance = 29.847073648828854
amplitude = 37.0

Even though have a negative skeweness, the average and median indicates that there is 
some central tendency and simetry (there are no outliers that impacts significatly the
average).
Also, variance indicates a good dispersion of samples, as can be seen by the relative
frequency, most samples (~80%) are between 29.5 and 43.38.
These can make lsat have a good discriminatory power, but, might be a proxy for other 
classes (again, the same with family income).


### GENDER

| male   |   abs_frequency |   rel_frequency |
|:-------|----------------:|----------------:|
| 0      |            9826 |           43.85 |
| 1      |           12576 |           56.13 |
| <NA>   |               5 |            0.02 |

![Histogram for gender](../../results/charts/univariate/hist_male.png)

It have a good overall distribution, almost 50-50. But, it might have some non linear
relationship with other features like race, family income and so on. It shall be evaluated
later.


### RACE

| race   |   abs_frequency |   rel_frequency |
|:-------|----------------:|----------------:|
| 0      |            3691 |           16.47 |
| 1      |           18716 |           83.53 |
| <NA>   |               0 |            0    |

![Histogram for race](../../results/charts/univariate/hist_race.png)

Strong imbalance, which might offuscate the unprivileged group. It needs further evaluation
to check for proxies.


### TIER

| tier   |   abs_frequency |   rel_frequency |
|:-------|----------------:|----------------:|
| 1      |             594 |            2.65 |
| 2      |            1694 |            7.56 |
| 3      |            7991 |           35.66 |
| 4      |            6083 |           27.15 |
| 5      |            3895 |           17.38 |
| 6      |            2054 |            9.17 |
| <NA>   |              96 |            0.43 |

![Histogram for tier](../../results/charts/univariate/hist_tier.png)

Even though it has a good distribution (most samples are in near median), it might be
a proxy for other variables. Needs further evaluation.


### UGPA

| ugpa      |   abs_frequency |   rel_frequency |
|:----------|----------------:|----------------:|
| 1.5 - 1.8 |              13 |            0.06 |
| 1.8 - 2.1 |             170 |            0.76 |
| 2.1 - 2.4 |             766 |            3.42 |
| 2.4 - 2.7 |            2104 |            9.39 |
| 2.7 - 3.0 |            4230 |           18.88 |
| 3.0 - 3.3 |            5987 |           26.72 |
| 3.3 - 3.6 |            5767 |           25.74 |
| 3.6 - 3.9 |            3369 |           15.04 |
| nan       |               0 |            0    |

![Histogram for undergraduate gpa](../../results/charts/univariate/hist_ugpa.png)

average = 3.2154505288525908
median = 3.2
mode = 3.4
variance = 0.16327461514376654
amplitude = 2.4

Have a negative skeweness with more significance then lsat, also, have a small variance
which indicates that samples are more concentrated towards the average. There is some
central tendency, but it isn't symmetrical. 


### ZFYGPA

| zfygpa        |   abs_frequency |   rel_frequency |
|:--------------|----------------:|----------------:|
| -3.35 - -2.53 |              42 |            0.19 |
| -2.53 - -1.7  |             520 |            2.32 |
| -1.7 - -0.88  |            2728 |           12.17 |
| -0.88 - -0.05 |            6335 |           28.27 |
| -0.05 - 0.77  |            6739 |           30.08 |
| 0.77 - 1.6    |            3924 |           17.51 |
| 1.6 - 2.42    |            1060 |            4.73 |
| 2.42 - 3.25   |              74 |            0.33 |
| nan           |             984 |            4.39 |

![Histogram for z-score for first year gpa](../../results/charts/univariate/hist_zfygpa.png)

average = 0.08606777762218178
median = 0.08
mode = -0.03
variance = 0.8624511973479084
amplitude = 6.6

There are a good number of samples with NaN values, which must be treated before training.
Also, it might have a stronger predictive power because ugpa says about the performance
with subjects that might not be related with legislation and such.
Also, have an overall nice distribution, being an z-score, it displays a normal distribution
with a "good" variance, making a viable option to use as a predictive feature.

### ZGPA

| zgpa          |   abs_frequency |   rel_frequency |
|:--------------|----------------:|----------------:|
| -6.44 - -5.2  |               0 |            0    |
| -5.2 - -3.97  |               0 |            0    |
| -3.97 - -2.73 |              30 |            0.13 |
| -2.73 - -1.5  |            1280 |            5.71 |
| -1.5 - -0.26  |            7102 |           31.7  |
| -0.26 - 0.98  |            9166 |           40.91 |
| 0.98 - 2.21   |            3322 |           14.83 |
| 2.21 - 3.45   |             217 |            0.97 |
| nan           |            1289 |            5.75 |

![Histogram for final gpa](../../results/charts/univariate/hist_zgpa.png)

average = 0.008756037503551474
median = 0.0
mode = 0    0.0
variance = 0.9623467547996978
amplitude = 9.89

Same behavior with zfygpa.
Cumulative GPA is the ultimate reflection of the entire academic journey. If a 
protected group (such as race or fam_inc) faced systematic difficulties during the 
course, zgpa will be the variable that best "hides" (or encodes) those difficulties.

# BIVARIATE ANALYSIS

Looking at univariate analysis we can see that some attributes might be proxies for 
bias, such as **fam_inc**, **tier**, **fulltime**. Also, there are some features that
might bias the model such as **gender**, **race** and **age**, so, first let's check
if there might have some direct bias towards these features.


## PREDICTIVE FEATURES

Before we take a look at these features that can carry some direct bias, we shall look
at features that in are directly used to evaluate student performance, such as **lsat**,
**ugpa**, **zfygpa**, **zgpa**. To evaluate if these features are dependent of each
other was calculated the pearson matrix as the following:

**PEARSON MATRIX**
|        |      lsat |      ugpa |     zfygpa |       zgpa |
|:-------|----------:|----------:|-----------:|-----------:|
| lsat   |  1        |  0.243069 |  0.281868  |  0.295502  |
| ugpa   |  0.243069 |  1        |  0.173866  |  0.224647  |
| zfygpa |  0.281868 |  0.173866 |  1         |  0.871557  |
| zgpa   |  0.295502 |  0.224647 |  0.871557  |  1         |

There is a strong correlation between zfygpa and zgpa, which makes sense, after all
the gpa at the first year is used to compute the overall gpa, in such way, this feature
can be discarded. This correlation can be illustrated by the scatter plot bellow:

![Scatter plot zfygpa vs zgpa](../../results/charts/bivariate/scatter_zfygpa_zgpa.png)

Running Student's and Mann-Whitney test to check if groups within these features have
the same outcome, which would indicate that this feature has no correlation with 
**pass_bar**.

**STUDENT'S T AND MANN-WHITNEY U TEST**
**lsat X pass_bar**
|    |   group_a |   group_b |   t_test |   t_test_p_value |   mann_whitney |   mann_whitney_p_value |
|---:|----------:|----------:|---------:|-----------------:|---------------:|-----------------------:|
|  0 |         0 |         1 | -36.7515 |     3.58197e-287 |     5.9824e+06 |           1.60136e-196 |

**ugpa X pass_bar**
|    |   group_a |   group_b |   t_test |   t_test_p_value |   mann_whitney |   mann_whitney_p_value |
|---:|----------:|----------:|---------:|-----------------:|---------------:|-----------------------:|
|  0 |         0 |         1 | -21.6696 |      4.5428e-103 |    8.15636e+06 |            1.77445e-87 |

**zgpa X pass_bar**
|    |   group_a |   group_b |   t_test |   t_test_p_value |   mann_whitney |   mann_whitney_p_value |
|---:|----------:|----------:|---------:|-----------------:|---------------:|-----------------------:|
|  0 |         0 |         1 | -42.1869 |                0 |    3.32412e+06 |                      0 |

Looking at these values, it is clear that these variables have some correlation with 
**pass_bar**.


## RACE

First, checking the contigency table with **pass_bar** we have the following:

|           |   abs_frequency |   rel_frequency_tot |   rel_f_race_by_pass_bar |   rel_f_pass_bar_by_race |
|:----------|----------------:|--------------------:|-------------------------:|-------------------------:|
| (1, 0)    |              19 |                0.08 |                 18.0952  |                1.62532   |
| (1, 1)    |              86 |                0.38 |                 81.9048  |                0.404935  |
| (2, 0)    |              70 |                0.31 |                  7.80379 |                5.98802   |
| (2, 1)    |             827 |                3.69 |                 92.1962  |                3.89396   |
| (3, 0)    |             298 |                1.33 |                 22.1891  |               25.4919    |
| (3, 1)    |            1045 |                4.66 |                 77.8109  |                4.92043   |
| (4, 0)    |              46 |                0.21 |                 11.6162  |                3.93499   |
| (4, 1)    |             350 |                1.56 |                 88.3838  |                1.64799   |
| (5, 0)    |              26 |                0.12 |                 20.8     |                2.22412   |
| (5, 1)    |              99 |                0.44 |                 79.2     |                0.466146  |
| (6, 0)    |              56 |                0.25 |                 11.0672  |                4.79042   |
| (6, 1)    |             450 |                2.01 |                 88.9328  |                2.11884   |
| (7, 0)    |             629 |                2.81 |                  3.36076 |               53.8067    |
| (7, 1)    |           18087 |               80.72 |                 96.6392  |               85.1634    |
| (8, 0)    |              23 |                0.1  |                  7.59076 |                1.96749   |
| (8, 1)    |             280 |                1.25 |                 92.4092  |                1.31839   |
| (<NA>, 0) |               2 |                0.01 |                nan       |                0.171086  |
| (<NA>, 1) |              14 |                0.06 |                nan       |                0.0659196 |

![Stacked bar race by pass_bar](../../results/charts/bivariate/stacked_race_pass_bar.png)

25.49% of those that failed the bar exam where from group 3 (black) and that this group
have a failure rate of 22.19% within this group. This by itself might skew the prediction
for this group. We have other groups such 1 (indigenous folk) and 5 (mexican) that have
high failure rates, 18.10% and 20.80% respective, and having such a few samples makes
it a more instable group.

The **Cramer's V** for **bar approval**, which resulted in a value of 0.220314, indicates
that there is a moderate dependency them, which indicates a bias towards this attribute.
To check if this dependency can be justified by the predictive features or if this 
dependency is arbitrary to see if this possible bias originates from some socioeconomic
/ historical bias or if there is some direct bias towards these groups.

Looking at the **Kruskal-Wallis** test to check if the predictive features are evenly
distributed or if these features are disbalanced.

| label   |       p_race |   s_race |
|:--------|-------------:|---------:|
| lsat    | 0            | 2343.53  |
| ugpa    | 9.94951e-212 | 1000.38  |
| zfygpa  | 0            | 1819.33  |
| zgpa    | 0            | 2014.31  |
| age     | 2.9028e-19   | 102.759  |

With the test is clear that predictive features aren't evenly distributed between races,
this might indicate that predictive features can be proxy for bias. This possible proxy
can be better illustrated by the violin charts bellow:

![Violin chart lsat x race](../../results/charts/multivariate/violin_race_lsat.png)

![Violin chart ugpa x race](../../results/charts/multivariate/violin_race_ugpa.png)

![Violin chart zfygpa x race](../../results/charts/multivariate/violin_race_zfygpa.png)

![Violin chart zgpa x race](../../results/charts/multivariate/violin_race_zgpa.png)

In general, it can observed that all groups have different score between them, with
the exception of groups 1 (indigenous), 4 (porto rico) and 5 (mexican). This differences
between these groups can be illustrated clearly with the violin charts and with their
**disparate impacts** **statistical parity differences**. In every feature the group
3 underperforms in comparison with other groups. 

|   privileged_group |   priv_rate |   unprivileged_group |   unpriv_rate |   disparate_impact |   statistical_parity_difference |
|:-------------------|------------:|---------------------:|--------------:|-------------------:|--------------------------------:|
|                  7 |    0.966392 |                    1 |      0.819048 |           0.847531 |                     -0.147345   |
|                  7 |    0.966392 |                    2 |      0.921962 |           0.954025 |                     -0.0444303  |
|                  7 |    0.966392 |                    3 |      0.778109 |           0.805168 |                     -0.188284   |
|                  7 |    0.966392 |                    4 |      0.883838 |           0.914575 |                     -0.082554   |
|                  7 |    0.966392 |                    5 |      0.792    |           0.819543 |                     -0.174392   |
|                  7 |    0.966392 |                    6 |      0.889328 |           0.920256 |                     -0.0770643  |
|                  7 |    0.966392 |                    8 |      0.924092 |           0.956229 |                     -0.0423     |

This implies that simply discarding the race feature will not result in a fair model
because the bias is not directly in the dataset, the bias is socioeconomic. Even if
race was removed the model (Random Forests) would recreate bias through predictive
features.


## GENDER

Gender fits into the definition for what might configure as a protected attribute. But,
looking at the contigency table bellow doesn't look like there is a huge difference
within this category.

|           |   abs_frequency |   rel_frequency_tot |   rel_f_male_by_pass_bar |   rel_f_pass_bar_by_male |
|:----------|----------------:|--------------------:|-------------------------:|-------------------------:|
| (0, 0)    |             568 |                2.53 |                  5.78058 |               48.5885    |
| (0, 1)    |            9258 |               41.32 |                 94.2194  |               43.5917    |
| (1, 0)    |             601 |                2.68 |                  4.77894 |               51.4115    |
| (1, 1)    |           11975 |               53.44 |                 95.2211  |               56.3848    |
| (<NA>, 1) |               5 |                0.02 |                nan       |                0.0235427 |

![Relative frequency for gender and approval](../../results/charts/bivariate/stacked_pass_bar_male.png)

Checking the Cramer's V we have a value of 0.0211153 which is inexpressive, but the
Kruskal-Wallis test accuses that might be some difference in distribution between these
groups.

| label   |      p_male |     s_male |
|:--------|------------:|-----------:|
| lsat    | 2.58072e-28 | 121.779    |
| ugpa    | 7.94825e-87 | 390.081    |
| zfygpa  | 5.8033e-12  |  47.3949   |
| zgpa    | 0.355348    |   0.854267 |

Looking at the violin charts we see that there is no significative difference between
these groups, which is corroborated by **disparate impact** and **statistical parity
difference**, favoring dropping this column.

|   privileged_group |   priv_rate |   unprivileged_group |   unpriv_rate |   disparate_impact |   statistical_parity_difference |
|:-------------------|------------:|---------------------:|--------------:|-------------------:|--------------------------------:|
|                  1 |    0.952211 |                    0 |      0.942194 |           0.989481 |                     -0.0100164  |

![Distribution between gender and lsat](../../results/charts/bivariate/violin_male_lsat.png)

![Distribution between gender and ugpa](../../results/charts/bivariate/violin_male_ugpa.png)

![Distribution between gender and zfygpa](../../results/charts/bivariate/violin_male_zfygpa.png)

![Distribution between gender and zgpa](../../results/charts/bivariate/violin_male_zgpa.png)


## AGE

Age is the weirdest feature, the lack of samples for older groups impacts greatly the
variance as the univariate analysis showed. Through the **point biserial test** it is
shown that have no almost no correlation with bar approval.

| label   |   correlation |      p_value |
|:--------|--------------:|-------------:|
| age     |    -0.0956216 | 1.71859e-46  |

But **Kruskal-Wallis test** indicates otherwise:

| label   |       p_race |   p_fulltime |    p_fam_inc |      p_male |   p_pass_bar |      p_tier |   s_race |   s_fulltime |   s_fam_inc |     s_male |   s_pass_bar |     s_tier |
|:--------|-------------:|-------------:|-------------:|------------:|-------------:|------------:|---------:|-------------:|------------:|-----------:|-------------:|-----------:|
| age     | 2.9028e-19   |  0           | 2.63473e-219 | 8.95889e-07 | 1.2637e-46   | 3.39277e-69 |  102.759 |   1979.78    |   1019.07   |  24.1398   |      205.583 |  330.081   |

Also, the violin charts indicate otherwise:

![Distribution between age and pass_bar](../../results/charts/bivariate/violin_pass_bar_age.png)

There is no noticeable trend looking at the scatter plots for age:

![Scatter plot age vs lsat](../../results/charts/bivariate/scatter_lsat_age.png)

![Scatter plot age vs ugpa](../../results/charts/bivariate/scatter_ugpa.png)

![Scatter plot age vs zfygpa](../../results/charts/bivariate/scatter_zfygpa_age.png)

![Scatter plot age vs zgpa](../../results/charts/bivariate/scatter_zgpa_age.png)


## FAMILY INCOME

Family can be a strong bias factor, having that those with a better family income tends
to have a background with better educational institutions, extracurricular activies and
so on. But **Cramer's V** indicates that there is no strong correlation between family income
and approval at the exam (V = 0.0867781). However, **Kruskal-Wallis test** indicates
otherwise, having different distribution within this group

| label   |    p_fam_inc |   s_fam_inc |
|:--------|-------------:|------------:|
| lsat    | 4.23459e-124 |    579.499  |
| ugpa    | 3.19165e-07  |     35.7931 |
| zfygpa  | 3.44223e-37  |    176.906  |
| zgpa    | 2.89522e-40  |    191.222  |

But, verifying disparate impact and statistical parity difference we see that there is
no huge difference within this group, group 1 and 5 (poorest and richest) have a disparate
impact of 0.894775 and a statistical parity difference of -0.10128, which is indicates
that the poorer group have lower approval scores, but nothing significative as seem
with race.

|   privileged_group |   priv_rate |   unprivileged_group |   unpriv_rate |   disparate_impact |   statistical_parity_difference |
|:-------------------|------------:|---------------------:|--------------:|-------------------:|--------------------------------:|
|                  5 |    0.962514 |                    1 |      0.861233 |           0.894775 |                     -0.10128    |
|                  5 |    0.962514 |                    2 |      0.912964 |           0.94852  |                     -0.04955    |
|                  5 |    0.962514 |                    3 |      0.943389 |           0.98013  |                     -0.0191247  |
|                  5 |    0.962514 |                    4 |      0.961314 |           0.998754 |                     -0.00119969 |

Looking at the distribution between is visible that race is correlated with this feature.

![Frequency between race and family income](../../results/charts/bivariate/stacked_fam_inc_race.png)

Even though it has some significative values for Kruskal-Wallis test, the disparate
impact and statistical parity difference with the low value for Cramer's V makes this
feature dropable. The race bias is embedded in this feature already with the Cramer's
V for race and family income showing a weak correlation (V = 0.121).

## TIER

Checking **Cramer's V** for pass_bar we have a significative value, indicating a weak 
correlation with bar approval, **0.14156**. But observing the values for the **Kruskal-Wallis**
it seens that the distribution with **zfygpa** and **zgpa**, which are the strongest 
predictive feature, there is no significative difference in their distribution, this 
is illustrated by the violin charts between these features. However, there is a strong
difference between **lsat** and **ugpa**. These differences makes sense, because it's
expected that after law school ingression their scores normalize.

| label   |      p_tier |     s_tier |
|:--------|------------:|-----------:|
| lsat    | 0           | 4643.1     |
| ugpa    | 0           | 2430.39    |
| zfygpa  | 0.111271    |    8.94518 |
| zgpa    | 0.574295    |    3.82896 |

![Distribution between tier and lsat](../../results/charts/bivariate/violin_tier_lsat.png)

![Distribution between tier and ugpa](../../results/charts/bivariate/violin_tier_ugpa.png)

![Distribution between tier and zfygpa](../../results/charts/bivariate/violin_tier_zfygpa.png)

![Distribution between tier and zgpa](../../results/charts/bivariate/violin_tier_zgpa.png)

Also, the **Cramer's V** for **race** is significative, 0.125303. Acting as a stronger
bias source then family income. This is corroborated by the **disparate impact** (0.792045)
and **statistical parity difference** (-0.204209)

|   privileged_group |   priv_rate |   unprivileged_group |   unpriv_rate |   disparate_impact |   statistical_parity_difference |
|:-------------------|------------:|---------------------:|--------------:|-------------------:|--------------------------------:|
|                  6 |    0.981986 |                    1 |      0.777778 |           0.792045 |                     -0.204209   |
|                  6 |    0.981986 |                    2 |      0.916765 |           0.933582 |                     -0.0652213  |
|                  6 |    0.981986 |                    3 |      0.946815 |           0.964184 |                     -0.0351712  |
|                  6 |    0.981986 |                    4 |      0.960217 |           0.977831 |                     -0.0217694  |
|                  6 |    0.981986 |                    5 |      0.953273 |           0.97076  |                     -0.0287129  |

![Frequency between tier and bar approval](../../results/charts/bivariate/stacked_tier_pass_bar.png)

![Frequency between tier and race](../../results/charts/bivariate/stacked_tier_race.png)

## FULLTIME

Full time dedication might seen as a source of bias, specially when observing **Kruskal
-Wallis test**. But **Cramer's V** (0.0661584), **disparate impact** (0.941458) and 
**statistical parity difference** (-0.0557471) indicates otherwise,

| label   |   p_fulltime |   s_fulltime |
|:--------|-------------:|-------------:|
| lsat    |  1.72939e-55 |    246.223   |
| ugpa    |  5.43982e-59 |    262.289   |
| zfygpa  |  0.00868133  |      6.88724 |
| zgpa    |  0.109672    |      2.55895 |
| age     |  0           |   1979.78    |

![Distribution between fulltime and lsat](../../results/charts/bivariate/violin_fulltime_lsat.png)

![Distribution between fulltime and ugpa](../../results/charts/bivariate/violin_fulltime_ugpa.png)

![Distribution between fulltime and zfygpa](../../results/charts/bivariate/violin_fulltime_zfygpa.png)

![Distribution between fulltime and zgpa](../../results/charts/bivariate/violin_fulltime_zgpa.png)

|    | variable   |   privileged_group |   priv_rate |   unprivileged_group |   unpriv_rate |   disparate_impact |   statistical_parity_difference |
|---:|:-----------|-------------------:|------------:|---------------------:|--------------:|-------------------:|--------------------------------:|
|  7 | fulltime   |                  1 |    0.952259 |                    2 |      0.896512 |           0.941458 |                     -0.0557471  |

Also, values for **Cramer's V** for **race** (0.0303889) and for **family income** 
(0.0769144) demonstrate that there is no direct correlation between them, however,
there is a weak correlation with **tier** (0.109763).

![Frequency between fulltime and bar approval](../../results/charts/bivariate/stacked_fulltime_pass_bar.png)

![Frequency between fulltime and race](../../results/charts/bivariate/stacked_race_fulltime.png)

![Frequency between fulltime and tier](../../results/charts/bivariate/stacked_fulltime_tier.png)


# MULTIVARIATE ANALYSIS

Through **principal component analysis** becomes clear that **age**, **fulltime** and
**gender** have almost no value for the model. Also, through **spearman correlation 
matrix** it is visible these features are dropable. The only feature that correlates
with **gender** is **ugpa** and stills is a weak correlation, and their impact is miserable
on the model. **Fulltime** and **age** correlates only between themselves and their
impact over the model is also miserable as shown in the **principal component analysis**.

Also, evaluating **variance inflation factor** and the above analysis, it becomes clear
that **zgpa** and **zfygpa** are strongly correlated, which makes sense as explained
in the previous section. **zfygpa** will be droped, because of this strong correlation
and because zgpa tells a bigger picture about students overall performance.

**PRINCIPAL COMPONENT ANALYSIS**
|          |   PC1_Weight |
|:---------|-------------:|
| zgpa     |    0.51335   |
| zfygpa   |    0.503006  |
| lsat     |    0.419925  |
| race     |    0.335608  |
| ugpa     |    0.307452  |
| tier     |    0.203609  |
| fam_inc  |    0.185134  |
| male     |    0.0374946 |
| fulltime |   -0.0744161 |
| age      |   -0.131474  |

**VARIANCE INFLATION FACTOR**
|          |       0 |
|:---------|--------:|
| race     | 1.22385 |
| lsat     | 1.53981 |
| ugpa     | 1.27036 |
| zfygpa   | 4.23721 |
| zgpa     | 4.38549 |
| fulltime | 1.11346 |
| fam_inc  | 1.10219 |
| male     | 1.04605 |
| tier     | 1.42369 |
| age      | 1.17312 |

![Spearman correlation matrix](../../results/charts/multivariate/corr_matrix.png)
