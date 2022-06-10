import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penguins = pd.read_csv("penguins.csv").dropna().reset_index().drop(columns=["Unnamed: 0", "index"])
show = False

# Correlation Graphics
def scatterSexSpecies(xAxis, yAxis):
    # Add Data to Plot
    axes = plt.subplot()

    for species, group in penguins.groupby(["sex", "species"]):
        print(group["species"])
        axes.plot(group[xAxis], group[yAxis], marker='o', linestyle='', ms=5, label=species)

    # Add Linear Regression to Plot
    slope, intercept = np.polyfit(penguins[xAxis], penguins[yAxis], 1)
    plt.plot(penguins[xAxis], slope * penguins[xAxis] + intercept)

    # Add Correlation and Linear Regression
    plt.plot([], [], " ", label="Correlation: " + str(round(penguins[[xAxis, yAxis]].corr().iloc[1, 0], 2)))
    plt.plot([], [], " ", label="Linear Regression: " + str(round(slope, 2)) + "x+" + str(round(intercept, 2)))

    # Add Labels to Plot
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)

    plt.legend()
    plt.show()


def scatterIslandSpecies(xAxis, yAxis):
    # Add Data to Plot
    axes = plt.subplot()

    for species, group in penguins.groupby(["island", "species"]):
        print(group["species"])
        axes.plot(group[xAxis], group[yAxis], marker='o', linestyle='', ms=5, label=species)

    # Add Linear Regression to Plot
    slope, intercept = np.polyfit(penguins[xAxis], penguins[yAxis], 1)
    plt.plot(penguins[xAxis], slope * penguins[xAxis] + intercept)

    # Add Correlation and Linear Regression
    plt.plot([], [], " ", label="Correlation: " + str(round(penguins[[xAxis, yAxis]].corr().iloc[1, 0], 2)))
    plt.plot([], [], " ", label="Linear Regression: " + str(round(slope, 2)) + "x+" + str(round(intercept, 2)))

    # Add Labels to Plot
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)

    plt.legend()
    plt.show()


if show:
    scatterSexSpecies("bill_length_mm", "bill_depth_mm")
    scatterSexSpecies("bill_length_mm", "flipper_length_mm")
    scatterSexSpecies("bill_length_mm", "body_mass_g")
    scatterSexSpecies("bill_depth_mm", "flipper_length_mm")
    scatterSexSpecies("bill_depth_mm", "body_mass_g")
    scatterSexSpecies("flipper_length_mm", "body_mass_g")
else:
    scatterIslandSpecies("bill_length_mm", "bill_depth_mm")
    scatterIslandSpecies("bill_length_mm", "flipper_length_mm")
    scatterIslandSpecies("bill_length_mm", "body_mass_g")
    scatterIslandSpecies("bill_depth_mm", "flipper_length_mm")
    scatterIslandSpecies("bill_depth_mm", "body_mass_g")
    scatterIslandSpecies("flipper_length_mm", "body_mass_g")
