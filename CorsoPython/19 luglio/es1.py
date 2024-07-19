import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Genera un dataset di temperature giornaliere per un mese (30 giorni)
temperature_data = np.random.randint(15, 35, size=30)  # Temperature tra 15.0°C e 35.0°C

#Creo un DataFrame
df = pd.DataFrame(temperature_data, columns=['temperature'])

#calcolo min,max,media,mediana
temperature_max = df['temperature'].max()
temperature_min = df['temperature'].min()
temperature_media = df['temperature'].mean()
temperature_mediana = df['temperature'].median()

#stampo min,max,media,mediana
print(f"Temperatura massima: {temperature_max:.2f}°C")
print(f"Temperatura minima: {temperature_min:.2f}°C")
print(f"Temperatura media: {temperature_media:.2f}°C")
print(f"Mediana delle temperature: {temperature_mediana:.2f}°C")


# Prepara i dati per il grafico a barre
statistiche = ['Massima', 'Minima', 'Media', 'Mediana']
valori = [temperature_max, temperature_min, temperature_media, temperature_mediana]

# Crea il grafico a barre
plt.figure(figsize=(10, 6))
plt.bar(statistiche, valori, color='green')
plt.title('Statistiche delle Temperature')
plt.xlabel('Statistiche')
plt.ylabel('Temperatura')

plt.show()