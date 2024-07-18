"""Esempio Pratico finale: Unione e Risistemazione
Supponiamo di avere due dataset: uno con le vendite
giornaliere di prodotti in varie città e l'altro con le
informazioni sul costo dei prodotti. Utilizzeremo pandas
per unire questi dataset e creare una tabella pivot per
analizzare le vendite totali per prodotto e città.
Dataset di esempio:
Vendite: Prodotto, Quantità, Città, Data
Costi: Prodotto, Costo per unità
Operazioni:
Unire i due dataset su "Prodotto".
Creare una tabella pivot con le vendite totali per
prodotto per città."""
import pandas as pd

# Dataset Vendite
vendite_data = {
    'Prodotto': ['Mela', 'Pera', 'Banana', 'Mela', 'Pera', 'Banana'],
    'Quantità': [10, 20, 15, 10, 30, 25],
    'Città': ['Bari', 'Roma', 'Roma', 'Milano', 'Bari', 'Milano'],
    'Data': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02']
}

vendite_df = pd.DataFrame(vendite_data)

# Dataset Costi
costi = {
    'Prodotto': ['Mela', 'Pera', 'Banana'],
    'Costo per unità': [1.5, 2.0, 1.0]
}

costi_df = pd.DataFrame(costi)

unito_df = pd.merge(vendite_df, costi_df, on='Prodotto')
print("Dataset unito:\n", unito_df)

# Aggiunge una colonna per il valore totale delle vendite(unendo i dataframe)
unito_df['Valore Totale Vendite'] = unito_df['Quantità'] * unito_df['Costo per unità']

# Creo la tabella pivot
pivot_df = unito_df.pivot_table(values='Valore Totale Vendite', index='Prodotto', columns='Città', aggfunc='sum')
print("\nTabella pivot delle vendite totali per prodotto e città:\n", pivot_df)
