#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import storage
import datetime

from bottle import route, run, request

@route('/api/bundeslaender')
def bundeslaender():
    return storage.load_bundeslaender()

@route('/api/landkreise/<id_bundesland>')
def laender(id_bundesland):
    return storage.load_landkreise(id_bundesland)

@route('/api/neuinfizierte/<id_landkreis>')
def neuinfizierte(id_landkreis):
    since = datetime.datetime.strptime(request.query.since, '%Y-%m-%d') if len(request.query.since) > 0 else datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    until = datetime.datetime.strptime(request.query.until, '%Y-%m-%d') if len(request.query.until) > 0 else datetime.datetime.combine(datetime.datetime.now().date(), datetime.datetime.min.time())
    days = []
    while True:
        days.append([since.strftime('%Y-%m-%d'), 0])
        if since >= until:
            break
        since += datetime.timedelta(days=1)
    infections_per_day = storage.load_infections_per_day_for_landkreis(id_landkreis)
    for i in range(len(days)):
        if days[i][0] in infections_per_day:
            days[i][1] = infections_per_day[days[i][0]]
    return {'days': days}

@route('/api/infizierte/<id_landkreis>')
def infizierte(id_landkreis):
    start = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    since = datetime.datetime.strptime(request.query.since, '%Y-%m-%d') if len(request.query.since) > 0 else datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    until = datetime.datetime.strptime(request.query.until, '%Y-%m-%d') if len(request.query.until) > 0 else datetime.datetime.combine(datetime.datetime.now().date(), datetime.datetime.min.time())
    days = []
    while True:
        days.append([start.strftime('%Y-%m-%d'), None])
        if start >= until:
            break
        start += datetime.timedelta(days=1)
    infections_per_day = storage.load_infections_per_day_for_landkreis(id_landkreis)
    for i in range(len(days)):
        if i == 0:
            if days[i][0] in infections_per_day:
                days[i][1] = infections_per_day[days[i][0]]
            else:
                days[i][1] = 0
        else:
            days[i][1] = days[i-1][1]
            if days[i][0] in infections_per_day:
                days[i][1] += infections_per_day[days[i][0]]
    days = list(filter(lambda l: datetime.datetime.strptime(l[0], '%Y-%m-%d') >= since, days))
    return {'days': days}

@route('/api/neuinfizierte_bundesland/<id_bundesland>')
def neuinfizierte_bundesland(id_bundesland):
    since = datetime.datetime.strptime(request.query.since, '%Y-%m-%d') if len(request.query.since) > 0 else datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    until = datetime.datetime.strptime(request.query.until, '%Y-%m-%d') if len(request.query.until) > 0 else datetime.datetime.combine(datetime.datetime.now().date(), datetime.datetime.min.time())
    days = []
    while True:
        days.append([since.strftime('%Y-%m-%d'), 0])
        if since >= until:
            break
        since += datetime.timedelta(days=1)
    infections_per_day = storage.load_infections_per_day_for_bundesland(id_bundesland)
    for i in range(len(days)):
        if days[i][0] in infections_per_day:
            days[i][1] = infections_per_day[days[i][0]]
    return {'days': days}

@route('/api/infizierte_bundesland/<id_bundesland>')
def infizierte_bundesland(id_bundesland):
    start = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    since = datetime.datetime.strptime(request.query.since, '%Y-%m-%d') if len(request.query.since) > 0 else datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    until = datetime.datetime.strptime(request.query.until, '%Y-%m-%d') if len(request.query.until) > 0 else datetime.datetime.combine(datetime.datetime.now().date(), datetime.datetime.min.time())
    days = []
    while True:
        days.append([start.strftime('%Y-%m-%d'), None])
        if start >= until:
            break
        start += datetime.timedelta(days=1)
    infections_per_day = storage.load_infections_per_day_for_bundesland(id_bundesland)
    for i in range(len(days)):
        if i == 0:
            if days[i][0] in infections_per_day:
                days[i][1] = infections_per_day[days[i][0]]
            else:
                days[i][1] = 0
        else:
            days[i][1] = days[i-1][1]
            if days[i][0] in infections_per_day:
                days[i][1] += infections_per_day[days[i][0]]
    days = list(filter(lambda l: datetime.datetime.strptime(l[0], '%Y-%m-%d') >= since, days))
    return {'days': days}

run(host='127.0.0.1', port=8080)

