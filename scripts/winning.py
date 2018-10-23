import pandas as pd
from difflib import SequenceMatcher
candidates = pd.read_csv("../data/importantCandidates.csv", engine='python')
match1 = pd.read_csv("../data/timetomatch2tynan.csv", header=None, engine='python', names=['0', '1', '2', '3', '4', '5', 'foo'])
match2 = pd.read_csv("../data/house_district_forecast.csv", skiprows=64954, nrows=1031, header=None, engine='python')
candidates["won"] = 0


def sim(name, state, district, year):
    t_df = candidates.loc[(candidates["Year"] == year) & (candidates["Cand_Office_St"] == state) & (candidates["Cand_Office_Dist"] == district)]
    rArray = []
    for index, row in t_df.iterrows():
        r = SequenceMatcher(None, name, row["Cand_Name"]).ratio()
        rArray.append((r,index))
    m = max(rArray, key=lambda x:x[0])
    return m[1]



todrop = []
wins = []
for i, stuff, in candidates.iterrows():
    if stuff["Year"] != 2018:
        my_df = match1.loc[(stuff["Year"] == match1['4']) & (stuff["Cand_Office_Dist"] == match1['2']) & (stuff["Cand_Office_St"] == match1['1'])]

        #my_df.rename(columns =['0', '1', '2', '3', '4', '5', 'foo'], inplace=True)
        my_df = my_df.sort_values(by='foo', axis='index', ascending=False)
        if len(my_df.index) > 2:
            for i in range(2, len(my_df.index)):
                todrop.append(sim(my_df.iloc[i]['0'], my_df.iloc[i]['1'], my_df.iloc[i]['2'], my_df.iloc[i]['4']))

        if (len(my_df.index) > 0):
            wins.append(sim(my_df.iloc[0]['0'], my_df.iloc[0]['1'], my_df.iloc[0]['2'], my_df.iloc[0]['4']))
    else:
        my_df = match2.loc[(stuff["Cand_Office_Dist"] == match2[2]) & (stuff["Cand_Office_St"] == match2[1])]
        my_df = my_df.sort_values(by=8, axis='index', ascending=False)
        if len(my_df.index) > 2:
            for i in range(2, len(my_df.index)):
                todrop.append(sim(my_df.iloc[i][4], my_df.iloc[i][1], my_df.iloc[i][2], 2018))

candidates.loc[wins, "won"] = 1
candidates = candidates.drop(candidates.index[todrop])
candidates.to_csv("../data/winners.csv")
