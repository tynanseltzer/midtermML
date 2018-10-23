import pandas as pd
aggregate = pd.read_csv("../data/Aggregated.csv", engine='python')
match1 = pd.read_csv("../data/timetomatch2tynan.csv", header=None, engine='python')
match2 = pd.read_csv("../data/house_district_forecast.csv", skiprows=64954, nrows=1031, header=None, engine='python')
from difflib import SequenceMatcher


# Basically, check that they get at least 10% of the vote
def important(row):
    my_df = match1.loc[(match1[4] == row['Year']) &
                       (match1[1] == row['Cand_Office_St']) & (match1[6] > .1)]
    for _, check in my_df.iterrows():
        if row['Year'] == check[4] and row['Cand_Office_St'] == check[1] and \
                check[6] > .1:

            r = SequenceMatcher(None, row['Cand_Name'].lower(),
                                check[0].lower()).ratio()
            if r > .6:
                return True
    return False


def eimportant(row):
    my_df = match2.loc[(match2[1] == row['Cand_Office_St']) & (match2[9] > 10)]
    for _, check in my_df.iterrows():
        if row['Cand_Office_St'] == check[1] and check[9] > 10:

            r = SequenceMatcher(None, row['Cand_Name'].lower(),
                                check[4].lower()).ratio()
            if r > .6:
                return True
    return False


todrop = []
x = 0
for i, row in aggregate.iterrows():
    x += 1
    print(x)
    print(len(todrop))
    if row['Year'] != 2018:
        if not important(row):
            todrop.append(i)
    else:
        if not eimportant(row):
            todrop.append(i)

aggregate.drop(aggregate.index[todrop], inplace=True)
print(todrop)
aggregate.to_csv('../data/importantCandidates.csv')