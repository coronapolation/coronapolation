# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd

sqlite_db = sys.argv[1]
cnx = sqlite3.connect(sqlite_db)
dataset = pd.read_sql_query("SELECT * FROM RKI_COVID19", cnx)

cases_by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlFall"].count()
cases_by_state = dataset.groupby(["Bundesland", "Meldedatum"])["AnzahlFall"].count()

deaths_by_district = dataset.groupby(["Landkreis", "Meldedatum"])[
    "AnzahlTodesfall"
].count()
deaths_by_state = dataset.groupby(["Bundesland", "Meldedatum"])[
    "AnzahlTodesfall"
].count()

if __name__ == "__main__":
    print(cases_by_district.tail(10))
    print(cases_by_state.tail(10))
