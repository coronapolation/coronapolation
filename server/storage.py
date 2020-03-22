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
    conn.close()
    return data

def load_landkreise(bundesland_id):
    conn = db_conn()
    cur = conn.cursor()
    rows = cur.execute(f'SELECT DISTINCT IdLandkreis, Landkreis FROM RKI_COVID19 WHERE IdBundesland == \'{bundesland_id}\'').fetchall()
    data = {}
    for row in rows:
        data[row[0]] = row[1]
    conn.close()
    return data

def load_landkreis_infections(landkreis_id):
    conn = db_conn()
    cur = conn.cursor()
    rows = cur.execute(f'SELECT * FROM RKI_COVID19 WHERE IdLandkreis == \'{landkreis_id}\'').fetchall()
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

def load_infections_per_day_for_landkreis(id_landkreis):
    infections_per_day = {}
    for entry in load_landkreis_infections(id_landkreis):
        datekey = entry['Meldedatum'].strftime('%Y-%m-%d')
        if not datekey in infections_per_day:
            infections_per_day[datekey] = 0
        infections_per_day[datekey] += entry['AnzahlFall']
    return infections_per_day

def load_bundesland_infections(bundesland_id):
    conn = db_conn()
    cur = conn.cursor()
    rows = cur.execute(f'SELECT * FROM RKI_COVID19 WHERE IdBundesland == \'{bundesland_id}\'').fetchall()
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

def load_infections_per_day_for_bundesland(id_bundesland):
    infections_per_day = {}
    for entry in load_bundesland_infections(id_bundesland):
        datekey = entry['Meldedatum'].strftime('%Y-%m-%d')
        if not datekey in infections_per_day:
            infections_per_day[datekey] = 0
        infections_per_day[datekey] += entry['AnzahlFall']
    return infections_per_day