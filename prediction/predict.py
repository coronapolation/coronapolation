# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd

db = sys.argv[1]
cnx = sqlite3.connect(db)
df = pd.read_sql_query("SELECT * FROM RKI_COVID19", cnx)
print(df.head(5))
