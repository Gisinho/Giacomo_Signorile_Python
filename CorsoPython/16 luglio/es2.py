import numpy as np

def crea_array():
    arr = np.linspace(0, 1, 12)
    print("12 numeri equidistanti:")
    print(arr)
    return arr

def cambia_forma(arr):
    matrice = arr.reshape(3, 4)
    print("Matrice 3X4:")
    print(matrice)
    return matrice

def genera_matrice_casuale():
    matrice_casuale = np.random.rand(3, 4)
    print("Matrice 3X4 di numeri casuali:")
    print(matrice_casuale)
    return matrice_casuale

def calcola_somma(matrice, matrice_casuale):
    somma = np.sum(matrice + matrice_casuale)
    print("Somma delle matrici:")
    print(somma)

def menu():
    array = []
    matrice = [[]]
    matrice_casuale = [[]]
    
    while True:
        print("\nMenu:")
        print("1. Crea un array di 12 numeri equidistanti tra 0 e 1")
        print("2. Cambia la forma dell'array a una matrice 3x4")
        print("3. Genera una matrice 3x4 di numeri casuali tra 0 e 1")
        print("4. Calcola e stampa la somma degli elementi di entrambe le matrici")
        print("0. Esci")
        
        scelta = input("Scegli l'opzione: ")
        
        if scelta == '1':
            array = crea_array()
        elif scelta == '2':
            if array is not None:
                matrice = cambia_forma(array)
            else:
                print("Per favore, crea prima un array (opzione 1).")
        elif scelta == '3':
            matrice_casuale = genera_matrice_casuale()
        elif scelta == '4':
            if matrice is not None and matrice_casuale is not None:
                calcola_somma(matrice, matrice_casuale)
            else:
                print("Per favore, assicurati di aver creato entrambe le matrici (opzioni 2 e 3).")
        elif scelta == '0':
            print("Arrivederci.")
            break
        else:
            print("Opzione non valida.")

menu()
