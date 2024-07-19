import pandas as pd
import numpy as np

# Definiamo una data range per il nostro esempio
date_range = pd.date_range(start='2024-01-01', end='2024-01-10')

data = {
    'Data': np.random.choice(date_range, size=100),
    'Filiale': np.random.choice(['Bari', 'Milano', 'Verona', 'Torino', 'Benevento','Roma'], size=100),
    'Vendite': np.random.randint(100, 1000, size=100)
}

df = pd.DataFrame(data)

# Salviamo il DataFrame in un file CSV
df.to_csv('19 luglio_Signorile_test/vendite.csv', index=False)


# Carichiamo i dati dal file CSV
df = pd.read_csv('vendite.csv')

# Convertiamo la colonna 'Data' in formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Raggruppiamo i dati per 'Data' e 'Filiale' e calcoliamo la media delle vendite
vendite_medie = df.groupby(['Data', 'Filiale'])['Vendite'].mean().reset_index()

# Calcoliamo la media delle vendite giornaliere per ogni filiale
media_giornaliera_filiale = vendite_medie.groupby('Filiale')['Vendite'].mean().reset_index()

# Troviamo la filiale con le vendite medie più alte
filiale_max = media_giornaliera_filiale.loc[media_giornaliera_filiale['Vendite'].idxmax()]

# Salviamo i risultati in un nuovo file CSV
risultati = {
    'Vendite_Medie_Per_Data_Filiale': vendite_medie,
    'Media_Giornaliera_Per_Filiale': media_giornaliera_filiale,
    'Filiale_Più_Vendite': filiale_max
}

# Salviamo ciascun DataFrame in un file CSV separato
vendite_medie.to_csv('19 luglio_Signorile_test/vendite_medie_per_data_filiale.csv', index=False)
media_giornaliera_filiale.to_csv('19 luglio_Signorile_test/media_giornaliera_per_filiale.csv', index=False)
pd.DataFrame([filiale_max]).to_csv('19 luglio_Signorile_test/filiale_piu_vendite.csv', index=False)

print("risultati salvati.")

