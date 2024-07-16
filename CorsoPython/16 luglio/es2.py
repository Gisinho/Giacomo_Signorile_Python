import numpy as np

"""Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace."""
arr = np.linspace(0, 1, 12)
print(f"12 numeri equidistanti: {arr}")

"""Cambia la forma dell'array a una matrice 3x4."""
matrice = arr.reshape(3,4)
print("Matrice 3X4:")
print(matrice)

"""Genera una matrice 3x4 di numeri casuali tra 0 e 1."""
matrice_casuale = np.random.rand(3,4)
print("Matrice 3X4 di numeri casuali:")
print(matrice_casuale)

"""Calcola e stampa la somma degli elementi di entrambe le matrici."""
somma = np.sum(matrice+matrice_casuale)
print("Somma delle matrici:")
print(somma)