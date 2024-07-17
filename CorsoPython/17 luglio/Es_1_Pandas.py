""" Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.
Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 
Caricare i dati in un DataFrame autogenerandoli casualmente .
Visualizzare le prime e le ultime cinque righe del DataFrame.
Visualizzare il tipo di dati di ciascuna colonna.
Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
Identificare e rimuovere eventuali duplicati.
Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
Salvare il DataFrame pulito in un nuovo file CSV. """

import pandas as pd
import numpy as np

def genera_dati():
    #generazione randomica dati
    nomi  = ["Maria", "Carlo", "Gianni", "Rosa","Giacomo","Lucia","Valentina"]
    città = ["Milano", "Roma", "Bari", "Benevento", "Napoli","San Giorgio La Molara"]
    
    num_righe = int(input("Inserisci il numero di righe: "))

    data = {
        'Nome': np.random.choice(nomi, num_righe),
        'Età': np.random.randint(0,100, num_righe),
        'Città': np.random.choice(città, num_righe),
        'Salario' : np.random.randint(15000,40000, num_righe)
    }
    # Creazione del DataFrame
    df = pd.DataFrame(data)
    print(df)
    return df

def prime_ultime_5_righe(df):
    print("\nLe prime cinque righe sono: ")
    print(df.head())
    print("\nLe ultime cinque righe sono: ")
    print(df.tail())

def tipo_dati(df):
   print(df.dtypes)          

def statistiche_età(df):
    media = df['Età'].mean()
    mediana = df['Età'].median()
    deviazione_standard = df['Età'].std()
    print(f"La media delle età è: {media:.2f}")
    print(f"La mediana delle età è: {mediana:.2f}")
    print(f"La deviazione standard delle età è: {deviazione_standard:.2f}")

def statistiche_salario(df):
    media = df['Salario'].mean()
    mediana = df['Salario'].median()
    deviazione_standard = df['Salario'].std()
    print(f"La media dei salari è: {media:.2f}")
    print(f"La mediana dei salari è: {mediana:.2f}")
    print(f"La deviazione standard dei salari è: {deviazione_standard:.2f}")

def rimuovi_duplicati(df):
    duplicati = df.duplicated()
    print(f"\nDuplicati trovati:\n{duplicati}")
    
    df = df.drop_duplicates()
    print("\nDataFrame dopo la rimozione dei duplicati:")
    print(df)

def sostituisci_mancanti(df):
    chiavi = ["Età", "Salario"]
    for i in chiavi:
        df[i] =df[i].fillna(df[i].median())

    print("\nDataFrame dopo la sostituzione dei valori mancanti:")
    print(df)

def aggiungi_categoria_età(df):
    condizioni = [
        (df['Età'] <= 18),
        (df['Età'] > 18) & (df['Età'] <= 65),
        (df['Età'] > 65)
    ]
    #categorie da assegnare in base alle condizioni
    categorie = ['Giovane', 'Adulto', 'Senior'] 
    #np.select crea uno nuovo array basato sulle condizioni e sulle categorie fornite
    #Se una condizione è vera, viene assegnata la categoria corrispondente
    df['Categoria Età'] = np.select(condizioni, categorie, default='')
    print("\nDataFrame con la nuova colonna 'Categoria Età':")
    print(df)
    return df


def salva_df(df):
    df.to_csv("file.csv", index=False)
    print("Salvato in file.csv")

def menu():
    df = None
    while True:
        print("\nMenu:")
        print("1. Genera dati")
        print("2. Visualizza prime e ultime 5 righe")
        print("3. Visualizza tipo di dati")
        print("4. Visualizza statistiche età")
        print("5. Visualizza statistiche salario")
        print("6. Rimuovi duplicati")
        print("7. Sostituisci valori mancanti")
        print("8. Aggiungi categoria età")
        print("9. Salva DataFrame su file CSV")
        print("0. Esci")

        try:
            scelta = int(input("Scegli un'opzione: "))
            if scelta == 1:
                df = genera_dati()
            elif scelta == 2:
                if df is not None:
                    prime_ultime_5_righe(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 3:
                if df is not None:
                    tipo_dati(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 4:
                if df is not None:
                    statistiche_età(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 5:
                if df is not None:
                    statistiche_salario(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 6:
                if df is not None:
                    df = rimuovi_duplicati(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 7:
                if df is not None:
                    df = sostituisci_mancanti(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 8:
                if df is not None:
                    df = aggiungi_categoria_età(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 9:
                if df is not None:
                    salva_df(df)
                else:
                    print("Prima genera i dati.")
            elif scelta == 0:
                print("Arrivederci")
                break
            else:
                print("Scelta non valida, riprova.")
        except ValueError: #entra se il valore inserito risulta una stringa
            print("Inserisci un numero valido.")

menu()