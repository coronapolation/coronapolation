#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import storage

from bottle import route, run

@route('/bundeslaender')
def bundeslaender():
    return storage.load_bundeslaender()

@route('/landkreise/<id_bundesland>')
def laender(id_bundesland):
    return storage.load_landkreise(id_bundesland)

@route('/rki-data-germany-sum')
def index():
    pass

rki_data = storage.load_rki_data()
germany_sum = {}
for elem in rki_data:
    datekey = elem['Meldedatum'].strftime('%Y-%m-%d')
    if not datekey in germany_sum:
        germany_sum[datekey] = 0
    germany_sum[datekey] += elem['AnzahlFall']

run(host='0.0.0.0', port=8080)
