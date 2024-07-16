"""Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice."""

import numpy as np

sequenza = np.arange(1,26)
matrice = sequenza.reshape(5,5)
print(matrice)

seconda_colonna = matrice[:,1]
print("Seconda colonna:")
print(seconda_colonna)

terza_riga = matrice[2,:]
print("terza riga:")
print(terza_riga)

diagonale = np.diagonal(matrice)
somma_diagonale = sum(diagonale)
print(f"La somma della diagonale è: {somma_diagonale}")

media_diagonale = np.mean(diagonale)
print(f"La media della diagonale è: {media_diagonale:.2f}")