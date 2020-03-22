# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd

# import matplotlib.pyplot as plt

sqlite_db = sys.argv[1]
cnx = sqlite3.connect(sqlite_db)
dataset = pd.read_sql_query("SELECT * FROM RKI_COVID19", cnx)

by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlFall"].count()
print(by_district.tail(10))

by_state = dataset.groupby(["Bundesland", "Meldedatum"])["AnzahlFall"].count()
print(by_state.tail(10))
