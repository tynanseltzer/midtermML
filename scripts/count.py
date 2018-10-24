import pandas as pd
df = pd.read_csv("../data/winners.csv", engine='python')

foo = [0]*24
x = pd.Series(foo)
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
c = 0
for year in [2018]:
    for state in states:
        for num in range(55):
            my_df = df.loc[(df["Cand_Office_St"] == state) & (df["Cand_Office_Dist"] == num) & (df["Year"] == year)]
            if len(my_df.index) == 1:
                my_df.to_csv("../data/uncontested.csv", mode='a', header=False)
print(c)