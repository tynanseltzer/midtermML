import pandas as pd
import os

print(os.getcwd())
generic = {2010: 6.8, 2012: -1.2, 2014: 5.7, 2016: 1.1, 2018: -7.3}
new_df = pd.read_csv("data/parties.csv", header=None)
new_df.loc[:, "generic"] = 0
for i, r in new_df.iterrows():
    if r[6] == "DEM" or r[31] == "REP":

        new_df.loc[i, "generic"] = -generic[r[7]]
    else:
        new_df.loc[i, "generic"] = -generic[r[7]]

print(new_df["generic"])

l = list(new_df.columns.values)
print(l)
l.insert(49, l.pop(25))
print(l)
l.append(l.pop(48))
print(l)
print(new_df[49])
new_df = new_df[l]
print(new_df[49])
print(list(new_df.columns.values))
l.pop(0)

new_df.to_csv("data/parties.csv", header=None)

new_df = pd.read_csv("data/parties.csv", header=None)
l = list(new_df.columns.values)
l.pop(0)
l.pop(0)
new_df = new_df[l]
print(new_df[2])

new_df.to_csv("data/parties.csv", header=None)