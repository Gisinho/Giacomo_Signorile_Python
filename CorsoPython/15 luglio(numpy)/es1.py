"""Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) 
e la forma (shape) dell'array.
Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array."""
import numpy as np

arr = []
arr_float = []

while True:
    print("\nMenu MIO PROGRAMMA:")
    print("1. Crea array di numeri interi da 10 a 49 e verifico il tipo di dato.")
    print("2. Cambia il tipo dell'array in float64.")
    print("3. Stampa la forma dell'array.")
    print("0. Esci.")

    scelta = input("Scegli un'opzione: ")

    if scelta == '1':
        arr = np.arange(10,50)
        print(f"L'array numeri interi da 10 a 49: {arr}")
        print(arr.dtype)
    elif scelta == '2':
        arrFloat = arr.astype(np.float64) 
        print(f"Cambio il tipo di dato dell'array in float64: {arrFloat}")
    elif scelta == '3':     
        # Stampo la forma dell'array
        print("La forma dell'array è:", arr.shape)
    elif scelta == '0':
        print("Arrivederci")
        break
    else:
        print("Opzione non valida.")