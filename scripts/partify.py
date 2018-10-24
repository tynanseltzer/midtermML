import pandas as pd
candidates = pd.read_csv("../data/winners.csv", engine='python')


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

for year in [2010, 2012, 2014, 2016, 2018]:
    for state in states:
        for num in range(55):
            my_df = df.loc[(df["Cand_Office_St"] == state) & (df["Cand_Office_Dist"] == num) & (df["Year"] == year)]

