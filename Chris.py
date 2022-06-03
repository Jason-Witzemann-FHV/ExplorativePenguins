import pandas as pd
import matplotlib.pyplot as plt

penguins = pd.read_csv("penguins.csv").drop(columns="Unnamed: 0").dropna().reset_index()







# QUICK REFERENCE

printTests = False

if printTests:
    # SHOW DATA
    print(penguins)

    # GROUP BY WITH AGGREGATOR (MEAN, COUNT)
    subset = penguins.groupby("species").count()
    subset = penguins[["species", "body_mass_g"]].groupby("species").mean()
    subset = penguins[["species", "year", "body_mass_g"]].groupby(["species", "year"]).mean().sort_values("body_mass_g", ascending=False)
    print(subset)

    # SELECT COLUMN BY NAME -> DF[NAME FOR COLUMN]
    subset = penguins["species"]
    subset = penguins[["species", "island"]]
    print(subset)

    # SELECT ROW BY EXPRESSION -> DF[EXPRESSION FOR ROW]
    subset = penguins[penguins["island"] == "Dream"]
    subset = penguins[(penguins["island"] == "Dream") | (penguins["body_mass_g"] > 3000)]
    print(subset)

    # SELECT ROW+COLUMN BY EXPRESSION+NAME -> DF.LOC[EXPRESSION FOR ROW, NAME FOR COLUMN]
    subset = penguins.loc[penguins["island"] == "Dream", "species"]
    subset = penguins.loc[(penguins["island"] == "Dream") | (penguins["body_mass_g"] > 3000), ["species", "island"]]
    print(subset)

    # SELECT ROW+COLUMN BY INDEX -> DF.ILOC[ROWS, COLUMNS]
    subset = penguins.iloc[0:10, 0:4]
    print(subset)