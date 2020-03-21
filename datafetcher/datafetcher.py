#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


class DataFetcher:
    def __init__(self, config):
        self.config = config
        self.CREATE_RKI_TABLE_SQL = """CREATE TABLE IF NOT EXISTS RKI_COVID19 (
            ObjectId integer PRIMARY KEY,
            Meldedatum timestamp,
            IdBundesland integer,
            Bundesland text,
            IdLandkreis text,
            Landkreis text,
            Altersgruppe text,
            Geschlecht text,
            AnzahlFall integer,
            AnzahlTodesfall integer
        );"""
        self.INSERT_RKI_ELEM_SQL = """INSERT INTO RKI_COVID19 values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        self.EXISTS_RKI_ELEM_SQL = """SELECT EXISTS(SELECT 1 FROM RKI_COVID19 WHERE ObjectId=? LIMIT 1);"""
        self.CHECK_DESTATIS_TABLE_EXISTS_SQL = """SELECT count(*) FROM sqlite_master WHERE type='table' AND name='DESTATIS_DICHTE';"""
        self.CREATE_DESTATIS_TABLE_SQL = """CREATE TABLE DESTATIS_DICHTE (
            lkr_id text PRIMARY KEY,
            lkr_stadt_name text,
            lkr_flaeche real,
            lkr_einwohner integer,
            lkr_einwohner_m integer,
            lkr_einwohner_w integer,
            lkr_dichte integer
        );"""
        self.INSERT_DESTATIS_ELEM_SQL = """INSERT INTO DESTATIS_DICHTE values(?, ?, ?, ?, ?, ?, ?);"""

    def fetch_rki_data(self):
        import requests
        url = self.config.get('default', 'npgeo_covid19_dataset')
        r = requests.get(url)
        if r.status_code != 200:
            print('unable to retrieve %s' % url)
            sys.exit(1)
        self.update_rki_data(r.json())

    def read_bevoelkerungsdichte(self):
        import xlrd
        conn = self.db_conn()
        cur = conn.cursor()
        table_exists = cur.execute(self.CHECK_DESTATIS_TABLE_EXISTS_SQL).fetchone()[0]
        if not table_exists:
            cur.execute(self.CREATE_DESTATIS_TABLE_SQL)
            conn.commit()
            xlsx_file = self.config.get('default', 'destatis_bevoelkerungsdichte_xlsx')
            wb = xlrd.open_workbook(xlsx_file)
            sheet = wb.sheet_by_index(1)
            for row in range(sheet.nrows):
                landkreis_id = sheet.cell_value(row, 0)
                if isinstance(landkreis_id, str) and len(landkreis_id) == 5 and landkreis_id.isdecimal():
                    lkr_stadt_name = sheet.cell_value(row, 2)
                    lkr_flaeche = sheet.cell_value(row, 4)
                    lkr_einwohner = int(sheet.cell_value(row, 5))
                    lkr_einwohner_m = int(sheet.cell_value(row, 6))
                    lkr_einwohner_w = int(sheet.cell_value(row, 7))
                    lkr_dichte = int(sheet.cell_value(row, 8))
                    cur.execute(self.INSERT_DESTATIS_ELEM_SQL, (
                        landkreis_id, lkr_stadt_name, lkr_flaeche, lkr_einwohner, lkr_einwohner_m, lkr_einwohner_w,
                        lkr_dichte))
            conn.commit()
        conn.close()

    def db_conn(self):
        import sqlite3
        db_fname = os.path.expanduser(self.config.get('default', 'coronapolation_db'))
        return sqlite3.connect(db_fname)

    def update_rki_data(self, json_data):
        from datetime import datetime
        conn = self.db_conn()
        cur = conn.cursor()
        cur.execute(self.CREATE_RKI_TABLE_SQL)
        conn.commit()
        for elem in json_data['features']:
            data = elem['properties']
            exists = cur.execute(self.EXISTS_RKI_ELEM_SQL, (data['ObjectId'],)).fetchone()[0]
            if not exists:
                dt = datetime.fromisoformat(data['Meldedatum'].rstrip('Z'))
                cur.execute(self.INSERT_RKI_ELEM_SQL, (data['ObjectId'],
                                                       data['Meldedatum'],
                                                       data['IdBundesland'],
                                                       data['Bundesland'],
                                                       data['IdLandkreis'],
                                                       data['Landkreis'],
                                                       data['Altersgruppe'],
                                                       data['Geschlecht'],
                                                       data['AnzahlFall'],
                                                       data['AnzahlTodesfall']))
        conn.commit()
        conn.close()


def get_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--config', default='~/.coronapolation-fetcher.conf',
                        help='config file (defaults to ~/.coronapolation-fetcher.conf)')
    return parser.parse_args()


def get_conf(config_path):
    from configparser import ConfigParser
    expanded_path = os.path.expanduser(config_path)
    config = ConfigParser()
    config.read(expanded_path)
    return config


def main():
    args = get_args()
    config = get_conf(args.config)
    fetcher = DataFetcher(config)
    fetcher.fetch_rki_data()
    fetcher.read_bevoelkerungsdichte()


if __name__ == "__main__":
    main()
