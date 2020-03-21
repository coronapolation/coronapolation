#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


class DataFetcher:
    def __init__(self, config):
        self.config = config
        self.create_table_sql = """CREATE TABLE RKI_COVID19 (
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
        self.insert_elem_sql = """INSERT INTO RKI_COVID19 values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    def fetch(self):
        import requests
        url = self.config.get('default', 'npgeo_covid19_dataset')
        r = requests.get(url)
        if r.status_code != 200:
            print('unable to retrieve %s' % url)
            sys.exit(1)
        self.dump(r.json())

    def dump(self, json_data):
        import sqlite3
        from datetime import datetime
        db_fname = os.path.expanduser(self.config.get('default', 'coronapolation_db'))
        try:
            os.remove(db_fname)
        except FileNotFoundError:
            pass
        conn = sqlite3.connect(db_fname)
        cur = conn.cursor()
        cur.execute(self.create_table_sql)
        conn.commit()
        for elem in json_data['features']:
            data = elem['properties']
            dt = datetime.fromisoformat(data['Meldedatum'].rstrip('Z'))
            cur.execute(self.insert_elem_sql, (data['ObjectId'],
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
    fetcher.fetch()


if __name__ == "__main__":
    main()
