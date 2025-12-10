
# TODO
#   Ingest dataset
#   Explore dataset
#       Describe columns
#       Select and justify columns
#       Check what distribution has the major cases of fail in pass_bar
#   Transformations 

from os import system
from pathlib import Path

from pandas import (
    DataFrame,
    read_csv,
    set_option,
    concat,
    merge
)
import matplotlib.pyplot as plt


set_option('display.max_columns', None)
set_option('display.max_rows', None)
set_option('display.precision', 3)

def _transform_indxgrp(category : str) -> int | None:
    indxgrp1 = {
        'a under 400' : 1,
        'b 400-460' : 2,
        'c 460-520' : 3,
        'd 520-580' : 4,
        'e 580-640' : 5,
        'f 640-700' : 6,
        'g 700+' : 7,
    }

    indxgrp2 = {
        'a under 400' : 1,
        'b 400-460' : 2,
        'c 460-520' : 3,
        'd 520-580' : 4,
        'e 580-640' : 5,
        'f 640-700' : 6,
        'g 700-760' : 7,
        'h 760-820' : 8,
        'i 820+' : 9,
    }

    try: 
        if not category:
            return

        if category in indxgrp2:
            return indxgrp2[category]
        return indxgrp1[category]

    except:
        print(category)
        exit()


def categorize_lsat(lsat : float) -> int | None:
    if 10 > lsat: return 1
    elif 10 <= lsat < 20: return 2
    elif 20 <= lsat < 30: return 3
    elif 30 <= lsat < 40: return 4
    elif 40 <= lsat: return 5
    else: return None


def categorize_index(c : float) -> int | None:
    if 200 > c: return 1
    elif 200 <= c < 300: return 2
    elif 300 <= c < 400: return 3
    elif 400 <= c < 500: return 4
    elif 500 <= c < 600: return 5
    elif 600 <= c < 700: return 6
    elif 700 <= c < 800: return 7
    elif 800 <= c < 900: return 8
    elif 900 <= c: return 9
    else: return None


def categorize_z(c : float) -> float | None:
    if -4.00 > c: return -4
    elif -4.00 <= c < -3.50: return -3.5
    elif -3.50 <= c < -3.00: return -3.0
    elif -3.00 <= c < -2.50: return -2.5
    elif -2.50 <= c < -2.00: return -2.0
    elif -2.00 <= c < -1.50: return -1.5
    elif -1.50 <= c < -1.00: return -1.0
    elif -1.00 <= c < -0.50: return -0.5
    elif -0.50 <= c < -0.00: return -0.5
    elif 0.00 <= c < 0.50: return 0.0
    elif 0.50 <= c < 1.00: return 0.5
    elif 1.00 <= c < 1.50: return 1.0
    elif 1.50 <= c < 2.00: return 1.5
    elif 2.00 <= c < 2.50: return 2.0
    elif 2.50 <= c < 3.00: return 2.5
    elif 3.00 <= c < 3.50: return 3.0
    elif 3.50 <= c < 4.00: return 3.5
    elif c >= 4.00: return 4.0
    else: return None


def cat_age(a : float) -> int | None:
    return



def eda():
    system('cls')

    path_csv = Path().cwd() / "tcc/bar_pass_prediction/bar_pass_prediction.csv"
    df = read_csv(
        path_csv, index_col='ID', encoding='utf-8', na_values="", on_bad_lines='warn',
    ).dropna()

    hr = "\n" + "="*50 + "\n"

    # COLUMNS:
    #   SCORE RELATED
    #       - gpa, grade point average
    #       - lsat, law school admission score
    #       - tier, grouping by average score in lsat's and gpa's universities

    #       - decile1, it looks like there is a strong correlation with zfygpa (z-score for first year)
    #       - decile3, it looks like there is a strong correlation with zgpa (final z-score)
    #       - index6040
    #       - zfygpa
    #       - zgpa, cannot make any sense for this variable, it doesn't look like z-score
    #           from gpa

    #   DATE RELATED
    #       - fulltime, there are more reprovations with parttime than with fulltime,
    #           but it doesn't look very significative, may be because of the dataset
    #           distribution

    #   PROTECTED ATTRIBUTES
    #       - sex, women tends to reprove more than man, but doesn't look statiscally 
    #           relevant
    #       - fam_inc
    #       - race1

    #   TARGET
    #       - pass_bar

    #   NOT SURE
    #       - age, not sure what is this age attribute, but has a strong correlation with
    #           BOD_yr and bar1_yr
    #       

    #   JUSTIFY WITH:
    #       test t (student)
    #       p values
    #       hypothesis test

    #   REDUNDANT / USELESS
    #       - ugpa, redundant with gpa
    #       - male, redundant with sex
    #       - gender, redundant with sex
    #       - bar_passed, redundant with pass_bar
    #       - race, doesn't have descriptions for the categories, but can infer from race1
    #       - indxgrp, categorization of index6040
    #       - indxgrp2, categorization of index6040
    #       - race2, redundant with race1, simple aggregation
    #       - decile1b, there is no much variance between decile1
    #       - bar1, if passed the first time, could be used to predict if person passes on the first try
    #       - bar2, if passed on the second time
    #       - bar, bar1 and bar2 are hor encoded from this, maybe

    #       - bar2_yr, year from the second attempt for the bar exam
    #       - bar1_yr, have no clue, but doesn't look like there is any correlation,
    #           same justification as DOB
    #       - DOB_yr, birth year, not useful, there is no strong correlation and there
    #           is no difference between the estimators from aproved and reproved
    #       - cluster, apparently is a reordering from tier
    #       - grad, useless all tuples have the same value
    #       - Dropout, inverse of grad
    #       - parttime, inverse of fulltime (probably if the person is a full time student)
    #       - other, hot encoded from race2
    #       - asian, hot encoded from race2
    #       - black, hot encoded from race2
    #       - hisp, hot encoded from race2
    #       - dnn_bar_pass_prediction, prediction for bar passage from deep neural networks

    dcolumns = [ 
        "ugpa",
        "male",
        "gender",
        "bar_passed",
        #"race",
        "indxgrp",
        "indxgrp2",
        "race2",
        "decile1b",
        'bar1',
        'bar2',
        'bar',

        "bar2_yr",
        "bar1_yr",
        "DOB_yr",
        "cluster",
        "grad",
        "Dropout",
        "parttime",
        "other",
        "asian",
        "black",
        "hisp",
        "dnn_bar_pass_prediction",

        'race1',
    ]

    df.drop(columns=dcolumns, inplace=True)

    hr = "\n" + "="*50 + "\n"

    #df['clsat'] = df['lsat'].apply(categorize_lsat)
    #df['cindex6040'] = df['index6040'].apply(categorize_index)
    #df['czfygpa'] = df['zfygpa'].apply(categorize_z)
    #df['czgpa'] = df['zgpa'].apply(categorize_z)
    #df['cgpa'] = df['gpa'].apply(categorize_z)
    #df['t'] = df['index6040'] - df['lsat'].apply(lambda x : 20 * x)
    df['my_zgpa'] = (df['gpa'] - 3.213) / 0.402

    print(df.info())
    print(hr)
    print(df.describe())
    print(hr)
    #for column in list(df.columns):
    #    print(df[column].value_counts().sort_index())
    #    print(hr)
    print(df.corr())
    print(hr)
    
    repro = df.loc[df['pass_bar'] == 0]
    aprov = df.loc[df['pass_bar'] == 1].sample(1040)
    con = concat([repro, aprov])
    con['ti'] = con['index6040'] / (con['lsat'] * con['gpa'])
    con['ti2'] = con['ti'] / con['tier']
    print(repro.describe())
    print(hr)
    print(aprov.describe())
    print(hr)
    print(con.corr())
    print(hr)
    print(con[['decile1', 'decile3', 'tier', 'zgpa', 'gpa', 'lsat', 'index6040', 'ti', 'ti2']].sample(100))
    #for column in list(aprov.columns):
    #    print(repro[column].value_counts().sort_index())
    #    print(aprov[column].value_counts().sort_index())
    #    print(hr)

    ## IDENTIFYING WHAT TIER IS
    #print(df[['tier', 'gpa', 'lsat', 'pass_bar']].groupby('tier').mean())

    ## IDENTIFYING WHAT CLUSTER IS
    #print(df[['cluster', 'gpa', 'zgpa', 'lsat', 'pass_bar']].groupby('cluster').mean())
    ## so... cluster ain't directily related to gpa and stuff
    ## checking if is just a reordering
    #print(merge(df[['cluster']], df[['tier']], left_index=True, right_index=True).shape, df.shape)
    ## cluster | tier
    ##  6 | 1
    ##  5 | 6
    ##  1 | 4
    #print(df['cluster'].value_counts())
    #print(df['tier'].value_counts())
    #print(df[['cluster', 'tier']].loc[df['cluster'] == 6].value_counts())
    #print(df[['cluster', 'tier']].loc[df['cluster'] == 5].value_counts())
    #print(df[['cluster', 'tier']].loc[df['cluster'] == 1].value_counts())
    ## it is just a reordering


    #df_grade = df[[
    #    'decile1', 'decile1b', 'decile3', 
    #    #'lsat', 'gpa', 'ugpa', 'zfygpa', 'zgpa',
    #    'tier', 
    #    'cluster',
    #    #'index6040', 'indxgrp', 'indxgrp2', 
    #    'pass_bar'
    #]].dropna()
    #df_grade['indxgrp'] = df_grade['indxgrp'].apply(_transform_indxgrp)
    #df_grade['indxgrp2'] = df_grade['indxgrp2'].apply(_transform_indxgrp)
    #print(df_grade.sample(20))
    #print(hr)
    #print(df_grade.describe())
    #print(hr)
    #print(df_grade['index6040'].nunique())
    #print(hr)
    #print(df_grade[['indxgrp', 'indxgrp2', 'index6040', 'pass_bar']].loc[df_grade['pass_bar'] < 1])
    #print(hr)
    #print(df_grade.corr(method='kendall'))
    #print(hr)

    # gpa and ugpa have same values
    # decile1b have a better correlation with the other variables, even though isn't 
    #   a strong correlation
    # TRANSFORM:
    #   categorize index6040
    #   drop ugpa, redundant with gpa
    #   drop decile1b, redundant with decile1
    #   drop indxgrp and indxgrp2, categories based on index6040

    #df_age = df[['DOB_yr', 'age', 'fulltime', 'parttime', 'pass_bar', 'bar1_yr', 'bar2_yr']].dropna()
    #df_age['age_real'] = df_age['bar2_yr'] - df_age['DOB_yr']
    #print(df_age.describe())
    #print(hr)
    #print(df_age.sample(20))
    #print(hr)
    #print(df_age.corr(method='kendall'))
    #print(hr)

    # DOB_yr is year of birth
    # cannot make anysense from column age, negative values, 
    # cannot make anysesnse from column bar1_yr, apparently is the difference between
    #   DOB_yr and age
    # fulltime and parttime contain the same information, the only difference is that
    #   fulltime is an int and parttime a "bool"
    # TRANSFORM:
    #   - fulltime to bool
    #   - append (bar2_yr - DOB_yr) age when passed bar exam
    #   - drop parttime
    #   - drop age
    #   - drop bar1_yr
    #   - drop bar2_yr
    #   - drop DOB_yr


    #drop_columns = [
    #    'decile1',
    #    'decile1b',
    #    'decile3',
    #    'bar1',
    #    'bar1_yr',
    #    'bar2',
    #    'bar2_yr',
    #    'other',
    #    'asian',
    #    'black',
    #    'hisp',
    #    'bar_passed',
    #    'indxgrp'
    #]

    #df.drop(columns=drop_columns, inplace=True)

    #print(df[['ugpa', 'gpa', 'zgpa']].head())
    #print(df['ugpa'].describe())
    #print(df['gpa'].describe())
    #print(df['zgpa'].describe())
    return
