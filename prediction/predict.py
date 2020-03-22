# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

sqlite_db = sys.argv[1]
cnx = sqlite3.connect(sqlite_db)
dataset = pd.read_sql_query("SELECT * FROM RKI_COVID19", cnx)
dataset["Meldedatum"] = pd.to_datetime(dataset["Meldedatum"])
dataset.index = dataset["Meldedatum"]
dataset = dataset.sort_index()

cases_by_district = dataset.groupby("Landkreis")["AnzahlFall"]
cases_by_state = dataset.groupby("Bundesland")["AnzahlFall"]

deaths_by_district = dataset.groupby("Landkreis")["AnzahlTodesfall"]
deaths_by_state = dataset.groupby("Bundesland")["AnzahlTodesfall"]


# def train_model(x, y, polynomial_degree):
#     polynomial_features = PolynomialFeatures(degree=polynomial_degree)
#     x_poly = polynomial_features.fit_transform(x)

#     model = LinearRegression()
#     model.fit(x_poly, y)

#     return model


def plot_cases_by_district(dataset, district):
    df = dataset.get_group(district)

    ax = plt.gca()
    plt.setp(ax.get_xticklabels(), rotation=45)
    ax.bar(df.index, df)

    formatter = mdates.DateFormatter("%b %d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)

    ax.set_title("Cases in " + district + " each day")
    ax.set_ylabel("Cases")
    ax.set_xlabel("Date")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_cases_by_district(cases_by_district, "StadtRegion Aachen")
