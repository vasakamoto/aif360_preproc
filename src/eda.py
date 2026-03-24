
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

    return
