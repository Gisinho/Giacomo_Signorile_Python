"""Esercizio 2: Manipolazione e Aggregazione dei Dati
Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
Caricare i dati in un DataFrame.
Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
Trovare il prodotto più venduto in termini di Quantità.
Identificare la città con il maggior volume di vendite totali.
Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
Visualizzare il numero di vendite per ogni città."""

import pandas as pd
def crea_dataframe():
    data = {
        'Prodotto': ['Mela', 'Pera', 'Banana', 'Caco', 'Ciliegie'],
        'Quantità': [10, 5, 8, 12, 3],
        'Prezzo Unitario': [10, 15, 80, 20, 12],
        'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano']
    }

    df = pd.DataFrame(data)
    return df

def aggiungi_totale_vendite(df):
    df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
    print("\n Aggiunta colonna totale vendite\n",df)

def raggruppare_totale_vendite(df):
    print("\nTotale vendite per prodotto")
    print(df.groupby('Prodotto')['Totale Vendite'].sum())

def prodotto_piu_venduto(df):
    print("\nProdotto più venduto:")
    print("La quantità venduta massima è:",df['Quantità'].max(),"e il prodotto più venduto è: ", df.loc[df['Quantità'].idxmax(), 'Prodotto'])

def citta_massime_vendite(df):
    print("\nCittà con maggiore vendita")
    print(df.groupby('Città')['Totale Vendite'].sum().idxmax())
    
def df_maggiori_vendite(df):
    df2 = df[df['Totale Vendite'] > 120]
    print("Vendite maggiori di 120 euro: ")
    print(df2)

def vendite_desc(df):
    df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
    print("\nDataFrame ordinato per 'Totale Vendite' in ordine decrescente:")
    print(df_ordinato)
def quantita_per_citta(df):
    print("\n",df.groupby('Città')['Quantità'].sum())



