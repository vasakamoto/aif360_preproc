
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

![Histogram for target variable](./img/uni_hist_pass_bar.png)

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

![Histogram for age](./img/uni_hist_age.png)

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

![Histogram for family income](./img/uni_hist_fam_inc.png)

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

![Histogram for full-time](./img/uni_hist_fulltime.png)

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

![Histogram for lsat](./img/uni_hist_fulltime.png)

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

![Histogram for gender](./img/uni_hist_fulltime.png)

It have a good overall distribution, almost 50-50. But, it might have some non linear
relationship with other features like race, family income and so on. It shall be evaluated
later.


### RACE

| race   |   abs_frequency |   rel_frequency |
|:-------|----------------:|----------------:|
| 0      |            3691 |           16.47 |
| 1      |           18716 |           83.53 |
| <NA>   |               0 |            0    |

![Histogram for race](./img/uni_hist_fulltime.png)

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

![Histogram for tier](./img/uni_hist_fulltime.png)

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

![Histogram for undergraduate gpa](./img/uni_hist_fulltime.png)

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

![Histogram for z-score for first year gpa](./img/uni_hist_fulltime.png)

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

![Histogram for final gpa](./img/uni_hist_fulltime.png)

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
# MULTIVARIATE ANALYSIS
