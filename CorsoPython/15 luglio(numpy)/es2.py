"""Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50."""
import numpy as np

arr_random = np.random.randint(10,50,20)
print(f"Genero 20 numberi casuali compresi tra 10 e 50: {arr_random}")

"""Utilizza lo slicing per estrarre i primi 10 elementi dell'array."""
slice=arr_random[:10]
print(f"Primi 10 elementi dell'array: {slice}")

"""Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array"""
slice=arr_random[-5:]
print(f"Ultimi 5 elementi dell'array: {slice}")

"""Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso)."""
slice=arr_random[5:15]
print(f"Elementi dall'indice 5 all'indice 15: {slice}")

"""Utilizza lo slicing per estrarre ogni terzo elemento dell'array."""
slice = arr_random [2::3]
print(f"Terzi elementi dell'array: {slice}")

"""Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99."""
slice=arr_random[5:10]=99
print(f"Assegno valore 99 agli elementi che vanno dall'indice 5 all'indice 10: {arr_random}")