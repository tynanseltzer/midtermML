import pandas as pd
from datetime import datetime
import numpy as np
historic = pd.read_csv("../../polls/historic.csv")
two8 = pd.read_csv("../../polls/2018.csv")

names = list(two8.pollster.unique())
#new_h = historic[historic['pollster'].isin(names)]
historic = historic[historic["year"] == 2014]
new_h = historic.groupby(["race", "year", "location"])
grades = {'A+': 0, "A": 1, "A-": 2, "B+": 3, "B": 4, "B-": 5,
          "C+": 6, "C": 7, "C-": 8, "D+": 9, "D": 10, "D-": 11, "F": 12}
Dates = {1998: '11/3/98', 1999: '11/2/99', 2000: '11/7/00', 2001: '11/6/01', 2002: "11/5/02",
         2003: "11/4/03", 2004: "11/2/04", 2005: "11/8/05", 2006: "11/7/06", 2007: "11/6/07",
         2008: "11/4/08", 2009: "11/3/09", 2010: "11/2/10", 2011: "11/8/11", 2012: "11/6/12",
         2013: "11/5/13", 2014: "11/4/14", 2015: "11/3/15", 2016: "11/8/16", 2017: "11/7/17",
         2018: "11/6/18"}

ratings = pd.read_csv("../../polls/pollster-ratings.csv")

alpha = .98
beta = .8

def f(df, alpha, beta):
    num = len(df.index)
    coeff_array = []
    summed = 0
    for _, r in df.iterrows():
        try:
            letter = ratings.loc[ratings["Pollster"] == r["pollster"], "538 Grade"].iloc[0]
        except IndexError:
            letter = "C"

        grade = grades[letter]

# find poll rating

# number of days until election
        d = datetime.strptime(r["polldate"], "%m/%d/%y")
        key = d.year
        delta = d - datetime.strptime(Dates[key], "%m/%d/%y")
        days = delta.days
        days = abs(days)
        coeff = alpha**days + beta * (12 - grade)
        coeff_array.append(coeff)
# Multiply that by poll margin
        adjusted = coeff * r["error"]
        summed += adjusted
    c_sum = sum(coeff_array)
    summed /= c_sum
    return summed
# Diff with absolute margi
# Sum and divide by sample
smallest = 99999
for a in np.linspace(.2, .01, 30):
    for b in np.linspace(0,5,2):
        new = sum(new_h.apply(f, alpha = a, beta = b))
        if new < smallest:
            print(new)
            print(a,b)
            smallest = new