# COLUMNS:

## SCORE RELATED

    - gpa, grade point average
    - lsat, law school admission score
    - tier, grouping by average score in lsat's and gpa's universities
    
    - decile1, it looks like there is a strong correlation with zfygpa (z-score for first year)
    - decile3, it looks like there is a strong correlation with zgpa (final z-score)
    - index6040
    - zfygpa
    - zgpa, cannot make any sense for this variable, it doesn't look like z-score
        from gpa

## DATE RELATED

    - fulltime, there are more reprovations with parttime than with fulltime, but it 
        doesn't look very significative, may be because of the dataset distribution

## PROTECTED ATTRIBUTES

    - sex, women tends to reprove more than man, but doesn't look statiscally relevant
    - fam_inc
    - race1

## TARGET

    - pass_bar

## NOT SURE

    - age, not sure what is this age attribute, but has a strong correlation with
        BOD_yr and bar1_yr
       

# REDUNDANT / USELESS

    - ugpa, redundant with gpa
    - male, redundant with sex
    - gender, redundant with sex
    - bar_passed, redundant with pass_bar
    - race, doesn't have descriptions for the categories, but can infer from race1
    - indxgrp, categorization of index6040
    - indxgrp2, categorization of index6040
    - race2, redundant with race1, simple aggregation
    - decile1b, there is no much variance between decile1
    - bar1, if passed the first time, could be used to predict if person passes on the first try
    - bar2, if passed on the second time
    - bar, bar1 and bar2 are hot encoded from this, maybe
    
    - bar2_yr, year from the second attempt for the bar exam
    - bar1_yr, have no clue, but doesn't look like there is any correlation,
        same justification as DOB
    - DOB_yr, birth year, not useful, there is no strong correlation and there
        is no difference between the estimators from aproved and reproved
    - cluster, apparently is a reordering from tier
    - grad, useless all tuples have the same value
    - Dropout, inverse of grad
    - parttime, inverse of fulltime (probably if the person is a full time student)
    - other, hot encoded from race2
    - asian, hot encoded from race2
    - black, hot encoded from race2
    - hisp, hot encoded from race2
    - dnn_bar_pass_prediction, prediction for bar passage from deep neural networks


# ANALYSIS

## CORRELATION

Independent variables that are function of each other
**SPEARMAN CORRELATION MATRIX:**
captures non-linear relationships



# JUSTIFY WITH:

       test t (student)
       p values
       hypothesis test

