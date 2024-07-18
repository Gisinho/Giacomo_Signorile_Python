"""Esercizio 1: Analisi di Vendite Fittizie
Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.
Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". I dati
devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.
1.Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.
2.Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.
3.Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto."""

import datetime
import pandas as pd
import numpy as np

def genera_dati():
    #generazione randomica dati
    date = [f'2024-07-{day:02d}' for day in range(1, 32)] # Genera un intervallo di date per un mese (considerando 31 giorni per semplicità)
    prodotti  = ['Mela', 'Pera', 'Banana']
    città = ["Milano", "Bari", "Benevento"]
    
    num_righe = int(input("Inserisci il numero di righe: "))

    data = {
        'Data': np.random.choice(date, num_righe),
        'Città': np.random.choice(città, num_righe),
        'Prodotto': np.random.choice(prodotti, num_righe),
        'Vendite' : np.random.randint(0,100, num_righe)
    }
    # Creazione del DataFrame
    df = pd.DataFrame(data)
    print(df)
    return df

def tabella_pivot(df):
    t_pivot = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
    print(f"La vendite medie dei prodotti per città sono: \n{t_pivot}")

def group_by(df):
    

genera_dati()