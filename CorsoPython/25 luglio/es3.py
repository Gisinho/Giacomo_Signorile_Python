"""Partendo dal dataset a questo link https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression , utilizzate i dati sulle ore di studio e le ore di sonno per prevedere quanto queste 
caratteristiche influiscono sull'indice di prestazione degli studenti."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# CArico dati dal csv
file_path = '25 luglio/Student_Performance.csv'
df = pd.read_csv(file_path, index_col=None)


X = df[['Hours Studied', 'Sleep Hours']]
y = df['Performance Index']

# Dividere i dati in set di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr = linear_model.LinearRegression()
regr.fit(X, y)


# Prevedere i valori per il set di test
y_pred = regr.predict(X_test)

# Visualizzo
plt.scatter(y_test, y_pred)
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.xticks(())
plt.yticks(())
plt.title('Prestazioni Reali - Predette')
plt.show()