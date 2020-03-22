# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

sqlite_db = sys.argv[1]
cnx = sqlite3.connect(sqlite_db)
dataset = pd.read_sql_query("SELECT * FROM RKI_COVID19", cnx)

cases_by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlFall"]
cases_by_state = dataset.groupby(["Bundesland", "Meldedatum"])["AnzahlFall"]

deaths_by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlTodesfall"]
deaths_by_state = dataset.groupby(["Bundesland", "Meldedatum"])["AnzahlTodesfall"]


# def train_model(x, y, polynomial_degree):
#     polynomial_features = PolynomialFeatures(degree=polynomial_degree)
#     x_poly = polynomial_features.fit_transform(x)

#     model = LinearRegression()
#     model.fit(x_poly, y)

#     return model


def plot_cases_by_district(dataset, district):
    plt.title("Amount of cases in " + district + " each day")
    plt.xlabel("Day")
    plt.ylabel("Cases")
    plt.show()


if __name__ == "__main__":
    print(cases_by_district.groups)
