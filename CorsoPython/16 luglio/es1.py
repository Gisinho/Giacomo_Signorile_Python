"""Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100."""

import numpy as np

matrice = np.random.randint(1,100, size=(6,6))
print(matrice)

"""Estrai la sotto-matrice centrale 4x4 dalla matrice originale."""
matr_centrale = matrice[1:-1, 1:-1] #seleziono righe e colonne centrali
print(f"Estrazione matrice centrale: {matr_centrale}")

"""Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, 
la seconda diventa la penultima, e così via)."""
matr_inverti = np.flipud(matr_centrale)
print(f"Matrice centrale invertita: {matr_inverti}")

"""Estrai la diagonale principale della matrice invertita 
e crea un array 1D contenente questi elementi"""
diagonale = np.diagonal(matr_inverti)
print(f"Diagonale principale della matrice invertita: {diagonale}")

"""Sostituisci tutti gli elementi della 
matrice invertita che sono multipli di 3 con il valore -1."""
matr_inverti[matr_inverti % 3 == 0]=-1
print(f"Sostituzione degli elementi con -1: {matr_inverti}")
