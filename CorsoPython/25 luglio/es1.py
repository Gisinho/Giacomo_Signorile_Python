"""Utilizzate la linear regression per analizzare il dataframe di esempio in cui abbiamo le Calorie bruciate in base al peso della persona che fa esercizio fisico con la montain bike, 
allenate l'algoritmo, testatelo e poi realizzate un grafico"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Caricare i dati dal file CSV
file_path = '25 luglio/calories.csv'
df = pd.read_csv(file_path)

#print(df.head())

x = df['kg']
y = df['calories']
array_x = np.array(x)
array_y = np.array(y)
#print(x.shape)#righe totali
X= array_x[:,np.newaxis]
#print(X.shape)

# dividiamo i dati in train e test
X_train, X_test, y_train, y_test = train_test_split(
    X, array_y)
#print(X_train)
#print(X_test)
#print(y_train)
#print(y_test)

# Creaiamo l'oggetto del modello
regr = linear_model.LinearRegression()

# Alleniamo il modello sul set di allenamento
regr.fit(X_train, y_train)

# Facciamo una predizione sui dati usando i dati di test
y_pred = regr.predict(X_test)

# Stampiamo il coefficente
print("Coefficients: \n", regr.coef_)

# L'errore quadratico medio 
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# Il coefficiente di determinazione: 1 Ã¨ la previsione perfetta
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# Creiamo i grafici
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()