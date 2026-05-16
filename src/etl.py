
from pandas import DataFrame

def run(df : DataFrame) -> DataFrame:

    data = df.drop(columns=[
        "decile1",                  # deciles from zfygpa
        "decile1b",                 # deciles from zfygpa
        "decile3",                  # deciles from gpa
        "ID",                       # unique identifier for instances
        "Dropout",                  # ???
        "grad",                     # ???
        "cluster",                  # reordered tier
        "parttime",                 # fulltime inverted
        "sex",                      # label encoding from gender
        "gender",                   # nominal for male 
        "race1",                    # nominal for race
        "race2",                    # grouped hisp, asian and other into other
        "asian",                    # hot encoded from race1
        "black",                    # hot encoded from race1
        "hisp",                     # hot encoded from race1
        "other",                    # hot encoded from race1
        "bar_passed",               # boolean for pass_bar
        "bar",                      # nominal for approval by attempt
        "bar1",                     # nominal for pass_bar
        "bar2",                     # nominal for pass_bar
        "index6040",                # derived from lsat
        "indxgrp",                  # grouped index6040
        "indxgrp2",                 # grouped index6040
        "gpa",                      # same as ugpa
        "dnn_bar_pass_prediction",  # prediction for deep neural networks
        "DOB_yr",                   # birth year
        "bar2_yr",                  # year of approval
        "age",                      # ??? but derived from 
        "bar1_yr",                  # difference between age and DOB_yr
        ])

    # transform bar2_yr and DOB_yr into age of approval
    data["age"] = df["bar2_yr"] - df["DOB_yr"]


    # changing race to binary "is white?"
    #data["race"] = data["race"].apply(lambda x : 0 if x != 7.0 else 1)

    # categorize age
    # that is because when the population is very small the variance can be huge, and
    # is the case here, with population older then 50 have 184 individuals with a huge
    # variance, from 12% of reprovation to 100%

    #def group_age(a : float) -> int:
    #    if a >= 49.99:
    #        return 8 # 50+
    #    if a >= 44.99 and a <= 50.00:
    #        return 7 # 45 ~ 50
    #    if a >= 39.99 and a <= 45.00:
    #        return 6 # 40 ~ 45
    #    if a >= 34.99 and a <= 40.00:
    #        return 5 # 35 ~ 40
    #    if a >= 29.99 and a <= 35.00:
    #        return 4 # 30 ~ 35
    #    if a >= 26.99 and a <= 30.00:
    #        return 3 # 27 ~ 30
    #    if a >= 24.99 and a <= 28.00:
    #        return 2 # 25 ~ 27
    #    else:
    #        return 1 # 25-
    #data["age"] = data["age"].apply(group_age)


    # type correctly
    def should_be_int(v : float) -> bool:
        try:
            if int(v) == v:
                return True
            return False
        except:
            return False

    for c in data.columns:
        if data[c].dropna().apply(should_be_int).all():
            data[c] = data[c].astype("Int64")

    data["age"] = data["age"].astype("float64")


    return data

