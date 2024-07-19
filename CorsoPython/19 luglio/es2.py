"""Testo dell'esercizio:
Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 
Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.
Fornisci un codice che:
Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
Applichi la normalizzazione min-max alle colonne altezza e peso.
Stampa sia il DataFrame originale sia quello modificato per compararli"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'altezza': [160, 175, 168, 180, 155],
    'peso': [60, 70, 65, 80, 55],
    'età': [25, 30, 22, 35, 28]
}
#dataframe
df = pd.DataFrame(data)


print("DataFrame1:")
print(df)


# Grafico del DataFrame1
#plt.subplot(1, 2, 1)
sns.histplot(data=df, x='altezza', y='peso', hue='età',kde=True)
plt.title('DataFrame1')
plt.xlabel('Altezza')
plt.ylabel('Peso')

plt.show()