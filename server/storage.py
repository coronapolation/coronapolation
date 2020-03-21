import config
import sqlite3
import os

from datetime import datetime

def db_conn():
    db_fname = os.path.expanduser(config.coronapolation_db)
    return sqlite3.connect(db_fname)

def load_bundeslaender():
    conn = db_conn()
    cur = conn.cursor()
    rows = cur.execute('SELECT DISTINCT IdBundesland, Bundesland FROM RKI_COVID19 WHERE IdBundesland != -1').fetchall()
    data = {}
    for row in rows:
        data[row[0]] = row[1]
    return data

def load_rki_data():
    conn = db_conn()
    cur = conn.cursor()
    rows = cur.execute('SELECT * FROM RKI_COVID19 WHERE IdBundesland != -1').fetchall()
    rki_data = []
    for row in rows:
        rki_data.append({
            'ObjectId': row[0],
            'Meldedatum': datetime.fromisoformat(row[1].rstrip('Z')),
            'IdBundesland': row[2],
            'Bundesland': row[3],
            'IdLandkreis': row[4],
            'Landkreis': row[5],
            'Altersgruppe': row[6],
            'Geschlecht': row[7],
            'AnzahlFall': row[8],
            'AnzahlTodesfall': row[9]
        })
    conn.close()
    return rki_data
