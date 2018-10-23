import pandas as pd
from difflib import SequenceMatcher
candidates = pd.read_csv("../data/Aggregated.csv", engine='python')
match1 = pd.read_csv("../data/timetomatch2tynan.csv", header=None, engine='python', names=['0', '1', '2', '3', '4', '5', 'foo'])
match2 = pd.read_csv("../data/house_district_forecast.csv", skiprows=64954, nrows=1031, header=None, engine='python')
candidates["won"] = 0

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
def sim(name, state, district, year):
    if (state in ["AK", "DE", "VT", "ND", "SD", "WY", "MT"]):
        district = 0
    t_df = candidates.loc[(candidates["Year"] == year) & (candidates["Cand_Office_St"] == state) & (candidates["Cand_Office_Dist"] == district)]
    rArray = []
    for index, row in t_df.iterrows():
        r = SequenceMatcher(None, name.lower(), row["Cand_Name"].lower()).ratio()
        rArray.append((r,index))
    m = max(rArray, key=lambda x:x[0])
    return m

toAdd = []
wins = []
for state in states:
    for num in range(70):
        for year in [2010, 2012, 2014, 2016, 2018]:
            if year != 2018:
                if not (state == "WV" and num == 5 ):
                    my_df = match1.loc[(match1["1"] == state) & (match1['2'] == num) & (year == match1['4'])]
                    my_df = my_df.sort_values(by='foo', axis='index', ascending=False)
                    for j in range(min(2,len(my_df.index))):
                        s = sim(my_df.iloc[j]['0'], my_df.iloc[j]['1'], my_df.iloc[j]['2'], my_df.iloc[j]['4'])
                        toAdd.append(s[1])
                        if j == 0:
                            wins.append(s[1])

            else:
                my_df = match2.loc[(match2[1] == state) & (match2[2] == num)]
                my_df = my_df.sort_values(by=8, axis='index', ascending=False)
                for j in range(min(2, len(my_df.index))):
                    s = sim(my_df.iloc[j][4], my_df.iloc[j][1], my_df.iloc[j][2], 2018)
                    toAdd.append(s[1])


candidates.loc[wins, "won"] = 1
toAdd = set(toAdd)
toAdd = list(toAdd)
toAdd = sorted(toAdd)
candidates = candidates.iloc[toAdd]
candidates.to_csv("../data/winners.csv")