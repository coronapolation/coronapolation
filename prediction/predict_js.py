# -*- coding: utf-8 -*-
import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import requests
from numpy.random import randn
from scipy.stats import norm

from pathlib import Path
from numpy import loadtxt

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
if False:
    sqlite_db = sys.argv[1]
    cnx = sqlite3.connect(sqlite_db)
    dataset1 = pd.read_sql_query("SELECT * FROM RKI_COVID19", cnx)

    cases_by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlFall"]
    cases_by_state = dataset.groupby(["Bundesland", "Meldedatum"])["AnzahlFall"]

    deaths_by_district = dataset.groupby(["Landkreis", "Meldedatum"])["AnzahlTodesfall"]
    deaths_by_state = dataset.groupby(["Bundesland", "Meldedatum"])["AnzahlTodesfall"]


if False:
    start_day='2020-02-24'
    until_day='2020-03-20'
    url = f'https://coronapolation.baremetal.rocks/api/infizierte/05111?since={start_day}&until={until_day}'
    response = requests.get(url)
    resp = response.json()

    data_y = []
    for data in resp['days']:
        data_y.append(data[1])


def create_training_validation_testing_data(filename):
    """ loads csv file and if not already exists creates a
    shuffled file and returns train, test, validation data """
    n = 5
    print(f"using file: {filename}")
    file_to_open = Path("Influenza/") / filename

    try:
        dataset = pd.read_csv(file_to_open, sep=';', header=None)
        #inputs = dataset[:, :]
        #print(inputs[0][0], inputs[0][-1])
        print(dataset)
        exit(1)
        targets = dataset[:, 1:]

        # split into train and validation and test (n_total = 45000)
        n_sequenes = int(len(inputs)/n)
        n_train = n*(int(0.8*n_sequenes))   # 80 % used as training values
        n_validation = n*(int((n_sequenes*0.2)/2)) # 10% used as validation values
        n_test = 5000

        self.training_input, self.validation_input, self.testing_input = inputs[:n_train, :], inputs[
                                                                                              n_train:n_train + n_validation,
                                                                                              :], inputs[
                                                                                                  n_train + n_validation:,
                                                                                                  :]
        self.training_target, self.validation_target, self.testing_target = targets[:n_train, :], targets[
                                                                                                  n_train:n_train + n_validation,
                                                                                                  :], targets[
                                                                                                      n_train + n_validation:,
                                                                                                      :]
        self.indexes = dataset[n_train + n_validation:, 0]

    except(FileNotFoundError, IOError):
        print(f"{file_to_open} not found!")


create_training_validation_testing_data('All_clean.csv')