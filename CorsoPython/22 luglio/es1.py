"""L'obiettivo di questo esercizio è generare un set di dati di serie temporali
utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:
Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.
Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.
Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.
Visualizzazione dei Dati:
Creare un grafico a linee del numero di visitatori giornalieri.
Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.
Creare un secondo grafico che mostri la media mensile dei visitatori."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generazione dei Dati
giorni = 365
media_visitatori = 2000
deviazione_standard = 500

# Impostiamo un range che approssima la media e la deviazione standard
min_visitatori = media_visitatori - 2 * deviazione_standard
max_visitatori = media_visitatori + 2 * deviazione_standard

# Generazione dei visitatori giornalieri
visitatori = np.random.randint(min_visitatori, max_visitatori, size=giorni)

#aumento graduale fino a 500visitatori in piu
trend= np.linspace(0,500,giorni)

#aggiungo trend crescente ai dati simulati
visitatori= visitatori+trend
print(visitatori)

"""Creazione dataframe"""
date = pd.date_range(start='2023-01-01', periods=giorni, freq='D')
df = pd.DataFrame({'Date':date, 'Visitatori':visitatori})

df.set_index('Date', inplace=True)#utilizzato per modificare il df e settare Date come indice
print(df)


media_mensile=df.resample('ME').mean()
print("\nMedia mensile dei visitatori:\n", media_mensile)

dev_mensile=df.resample('ME').std()
print("\nDeviazione standard mensile:\n", dev_mensile)



#Grafico a linee del numero di visitatori giornalieri
plt.figure()
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri')
plt.title('Numero di visitatori giornalieri')
plt.xlabel('Date')
plt.ylabel('Numero di visitatori')
plt.legend()
plt.grid(True)
plt.show()


# Grafico della media mensile dei visitatori
plt.figure()
plt.plot(media_mensile.index, media_mensile['Visitatori'])
plt.title('Media mensile dei visitatori')
plt.xlabel('Mese')
plt.ylabel('Numero di visitatori')
plt.show()
