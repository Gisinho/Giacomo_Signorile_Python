"""Partendo dal dataset a questo link https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction , utilizzate i dati sugli anni delle case e la distanza dalla stazione metro per 
prevedere quanto queste caratteristiche influiscono sul costo delle case."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# CArico dati dal csv
file_path = '25 luglio/Real estate.csv'
df = pd.read_csv(file_path, index_col=None)

#variabili dipendenti
X = df[['X2 house age', 'X3 distance to the nearest MRT station']]
y = df['Y house price of unit area']

# Dividere i dati in set di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr = LinearRegression()
#prendo il modello e lo alleno
regr.fit(X_train, y_train)


#r_sw=coefficiente 
r_sq=regr.score(X_train, y_train)
print(r_sq)

# Prevedere i valori per il set di test
y_pred = regr.predict(X_test)


from sklearn.metrics import PredictionErrorDisplay
display = PredictionErrorDisplay(y_true=y_test, y_pred=y_pred)
display.plot()
plt.show()