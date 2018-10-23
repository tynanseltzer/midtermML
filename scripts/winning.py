import pandas as pd
from difflib import SequenceMatcher
candidates = pd.read_csv("../data/Aggregated.csv", engine='python')
match1 = pd.read_csv("../data/timetomatch2tynan.csv", header=None, engine='python', names=['0', '1', '2', '3', '4', '5', 'foo'])
match2 = pd.read_csv("../data/house_district_forecast.csv", skiprows=64954, nrows=1031, header=None, engine='python')
candidates["won"] = 0

R = 0.4

def sim(name, state, district, year):
    t_df = candidates.loc[(candidates["Year"] == year) & (candidates["Cand_Office_St"] == state) & (candidates["Cand_Office_Dist"] == district)]
    rArray = []
    for index, row in t_df.iterrows():
        r = SequenceMatcher(None, name.lower(), row["Cand_Name"].lower()).ratio()
        rArray.append((r,index))
    m = max(rArray, key=lambda x:x[0])
    return m

def involved(row, df):
    for thing in df[df.columns[0]]:
        r = SequenceMatcher(None, thing.lower(), row["Cand_Name"].lower()).ratio()
        if r > R:
            return True
    return False

todrop = []
wins = []
for i, stuff, in candidates.iterrows():
    if stuff["Year"] != 2018:
        my_df = match1.loc[(stuff["Year"] == match1['4']) & (stuff["Cand_Office_Dist"] == match1['2']) & (stuff["Cand_Office_St"] == match1['1'])]
        if not involved(stuff, my_df):
            todrop.append(i)
            continue
        my_df = my_df.sort_values(by='foo', axis='index', ascending=False)
        if len(my_df.index) > 2:
            for j in range(2, len(my_df.index)):
                s = sim(my_df.iloc[j]['0'], my_df.iloc[j]['1'], my_df.iloc[j]['2'], my_df.iloc[j]['4'])
                if (s[0] > R):
                    todrop.append(s[1])

        if (len(my_df.index) > 0):
            s = sim(my_df.iloc[0]['0'], my_df.iloc[0]['1'], my_df.iloc[0]['2'], my_df.iloc[0]['4'])
            wins.append(s[1])
    else:
        my_df = match2.loc[(stuff["Cand_Office_Dist"] == match2[2]) & (stuff["Cand_Office_St"] == match2[1])]
        if not involved(stuff, my_df):
            todrop.append(i)
            continue
        my_df = my_df.sort_values(by=8, axis='index', ascending=False)
        if len(my_df.index) > 2:
            for j in range(2, len(my_df.index)):
                s = sim(my_df.iloc[j][4], my_df.iloc[j][1], my_df.iloc[j][2], 2018)
                if (s[0] > .6):
                    todrop.append(s[1])

candidates.loc[wins, "won"] = 1
todrop = set(todrop)
todrop = list(todrop)
candidates = candidates.drop(candidates.index[todrop])
candidates.to_csv("../data/winners.csv")
