import numpy as np
import numpy as np

def crea_array():
    arr = np.linspace(0, 10, 50)
    print("50 numeri equidistanti:")
    print(arr)
    return arr

def genera_array_casuale():
    array_casuale = np.random.random(50)
    print("Array di numeri casuali:")
    print(array_casuale)
    return array_casuale

def somma_array(arr, array_casuale):
    sum_array = arr + array_casuale
    print("Somma elemento per elemento:")
    print(sum_array)
    return sum_array

def somma_totale(sum_array):
    somma_totale = np.sum(sum_array)
    print("Somma totale degli elementi del nuovo array:")
    print(somma_totale)
    return somma_totale

def somma_maggiori_5(sum_array):
    somma_maggiori_5 = np.sum(sum_array[sum_array > 5])
    print("Somma degli elementi del nuovo array maggiori di 5:")
    print(somma_maggiori_5)
    return somma_maggiori_5

def menu():
    arr = []
    array_casuale = []
    sum_array = []

    while True:
        print("\nMenu:")
        print("1. Crea array di 50 numeri equidistanti tra 0 e 10")
        print("2. Genera array di 50 numeri casuali tra 0 e 1")
        print("3. Somma i due array elemento per elemento")
        print("4. Calcola la somma totale degli elementi del nuovo array")
        print("5. Calcola la somma degli elementi del nuovo array maggiori di 5")
        print("0. Esci")
        
        scelta = input("Seleziona un'opzione da 1 a 6: ")

        if scelta == '1':
            arr = crea_array()
        elif scelta == '2':
            array_casuale = genera_array_casuale()
        elif scelta == '3':
            if len(arr) > 0 and len(array_casuale) > 0:
                sum_array = somma_array(arr, array_casuale)
            else:
                print("Somma non valida, crea prima i due array")
        elif scelta == '4':
            if len(sum_array) > 0:
                somma_totale(sum_array)
            else:
                print("Devi sommare prima i due array")
        elif scelta == '5':
            if len(sum_array) > 0:
                somma_maggiori_5(sum_array)
            else:
                print("Devi prima sommare i due array!")
        elif scelta == '0':
            print("Arrivederci")
            break
        else:
            print("Opzione non valida. Riprova.")

menu()
