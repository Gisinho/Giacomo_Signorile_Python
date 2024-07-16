"""Esercizio 1: Somma e Media di Elementi
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array."""

import numpy as np

arr = np.random.randint(1,101, 15)
print(arr)

sum_arr = sum(arr)
print(f"La somma di tutti gli elementi è: {sum_arr}")

mean_arr = np.mean(arr)
print(f"La media di tutti gli elementi è: {mean_arr:.2f}")
