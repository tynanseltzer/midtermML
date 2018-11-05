import pandas as pd
from datetime import datetime
import math
Dates = {1998: '11/3/98', 1999: '11/2/99', 2000: '11/7/00', 2001: '11/6/01', 2002: "11/5/02",
         2003: "11/4/03", 2004: "11/2/04", 2005: "11/8/05", 2006: "11/7/06", 2007: "11/6/07",
         2008: "11/4/08", 2009: "11/3/09", 2010: "11/2/10", 2011: "11/8/11", 2012: "11/6/12",
         2013: "11/5/13", 2014: "11/4/14", 2015: "11/3/15", 2016: "11/8/16", 2017: "11/7/17",
         2018: "11/6/18"}
grades = {'A+': 0, "A": 1, "A-": 2, "B+": 3, "B": 4, "B-": 5,
          "C+": 6, "C": 7, "C-": 8, "D+": 9, "D": 10, "D-": 11, "F": 12}

generic = {2010: 6.8, 2010: -1.2, 2014: 5.7, 2016: 1.1, 2018: -7.3}
statesD = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
def days(s, f = False):
    if not f:
        d = datetime.strptime(s, "%m/%d/%y")
        key = d.year
        delta = d - datetime.strptime(Dates[key], "%m/%d/%y")
        days = delta.days
        return days
    else:
        d = datetime.strptime(s, "%Y-%m-%d")
        key = d.year
        delta = d - datetime.strptime(Dates[key], "%m/%d/%y")
        days = delta.days
        return days

def grade_sort(s):
    return grades[s]
df = pd.read_csv("../data/winners.csv", engine='python')
pollsh = pd.read_csv("../polls/historic.csv")
pollsh = pollsh[pollsh["type_simple"] == "House-G"]
polls2 = pd.read_csv("../polls/2018.csv")
polls2 = polls2[polls2["type"] == "house"]
foo = [0]*24
x = pd.Series(foo)
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



for year in [2010, 2012, 2014, 2016, 2018]:
    for state in states:
        for num in range(55):
            my_df = df.loc[(df["Cand_Office_St"] == state) & (df["Cand_Office_Dist"] == num) & (df["Year"] == year)]

            if len(my_df) == 2:
                if year != 2018:
                    foo = num
                    if state in ["AK", "MT", "WY", "SD", "VT", "DE", "ND"]:
                        foo += 1
                    q = state + "-" + str(foo)
                    ph = pollsh.loc[(pollsh["year"] == year) & (pollsh["location"] == q)]
                    avg = 0
                    if len(ph) > 0:
                        ph.assign(f = ph["polldate"].apply(days, f = False)).sort_values('f').drop('f', axis=1)
                        if len(ph.index) > 2:
                            avg = ph["margin_poll"][:3].mean()/200
                        else:
                            avg = ph["margin_poll"].mean()/200
                else:
                    foo = num
                    if state in ["AK", "MT", "WY", "SD", "VT", "DE", "ND"]:
                        foo += 1
                    q = state + "-" + str(foo)
                    ph = polls2.loc[(polls2["state"] == statesD[state]) & (foo == polls2["district"])]
                    avg = 0
                    if len(ph) > 0:
                        ph.assign(f= ph["endDate"].apply(days, f = True)).sort_values('f').drop(
                            'f', axis=1)
                        avg = ph["answers/0/pct"] - ph["answers/1/pct"]
                        for i, r in ph.iterrows():
                            if r["answers/0/party"] == "Rep" or r["answers/1/party"] == "Dem":
                                avg[i] *= -1
                        if len(ph.index) > 2:

                            avg = avg[:3].mean() / 200
                        else:
                            avg = avg.mean() / 200



                if (avg == 0):

                    my_df.loc[:, "polls"] = 0
                    my_df.loc[my_df.index[0], "polls"] = my_df.loc[my_df.index[0],"Party_Previous_Vote_Share"]
                    t1 = my_df.iloc[0]
                    my_df.loc[my_df.index[1], "polls"] = my_df.loc[my_df.index[1], "Party_Previous_Vote_Share"]
                    t2 = my_df.iloc[1]

                else:
                    if my_df.loc[my_df.index[0], "Cand_Party_Affiliation"] == "DEM" or my_df.loc[my_df.index[1], "Cand_Party_Affiliation"] == "REP":
                        my_df.loc[:, "polls"] = 0
                        my_df.loc[my_df.index[0], "polls"] = (.5 + avg)
                        t1 = my_df.iloc[0]
                        my_df.loc[my_df.index[1], "polls"] = (.5 - avg)
                        t2 = my_df.iloc[1]
                    else:
                        my_df.loc[:, "polls"] = 0
                        my_df.loc[my_df.index[0], "polls"] = (.5 - avg)
                        t1 = my_df.iloc[0]
                        my_df.loc[my_df.index[1], "polls"] = (.5 + avg)
                        t2 = my_df.iloc[1]
                foob = my_df.iloc[0].append(my_df.iloc[1]).to_frame().T
                foob.to_csv("../data/parties.csv", mode='a', header=False)
    print(year)




