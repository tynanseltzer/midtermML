import pandas as pd
import numpy as np
df = pd.read_csv("../data/2017_Gaz_115CDs_national.txt", delim_whitespace=True)



states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

df = df[df["USPS"] == "AK"]
df = df[["INTPTLAT", "INTPTLONG"]]
print(len(df.index))
min = 0
m = np.zeros((435,435))
for i, val in df.iterrows():
    for j, val2 in df.iterrows():
        if i == j:
            m[i,j] = .25
            continue

        m[i,j] = abs(val["INTPTLAT"] - val2["INTPTLAT"]) + abs(val["INTPTLONG"] - val2["INTPTLONG"])
m = m / np.max(m)
print(m)