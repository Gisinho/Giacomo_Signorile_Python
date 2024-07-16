"""Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
Il programma deve presentare un menu interattivo che consente all'utente di eseguire 
varie operazioni sulla matrice. Le operazioni disponibili includono:
Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma."""


import numpy as np
def menu():
    matrice = []
    
    while True:
        print("\nMenu:")
        print("1. Creare una nuova matrice 2D di dimensioni specificate con numeri casuali")
        print("2. Estrarre e stampare la sotto-matrice centrale")
        print("3. Trasporre la matrice e stamparla")
        print("4. Calcolare e stampare la somma di tutti gli elementi della matrice")
        print("0. Esci")

        scelta = input("Scegli l'opzione: ")

        if scelta == '1':
            matrice = crea_matrice()
        elif scelta == '2':
            try:
                matrice_centrale(matrice)
            except:
                print("Per favore, crea prima una matrice.")
        elif scelta == '3':
            try:
                matrice_trasposta(matrice)
            except:
                print("Per favore, crea prima una matrice.")
        elif scelta == '4':
            try:
                somma_elementi(matrice)
            except:
                print("Per favore, crea prima una matrice.")
        elif scelta == '0':
            print("Arrivederci.")
            break
        else:
            print("Opzione non valida.")

def crea_matrice():
    n_righe= input("Inserisci numero di righe: ")
    n_colonne= input("Inserisci numero di colonne: ")
    matrice = np.random.randint(1,100, size=(int(n_righe),int(n_colonne)))
    print("Matrice creata:")
    print(matrice)
    return matrice

def matrice_centrale(matrice):
    matrice_centrale = matrice[1:-1,1:-1]
    print("\nMatrice centrale:")
    print(matrice_centrale)

def matrice_trasposta(matrice):
    matr_trasposta = np.transpose(matrice)
    print("\nLa matrice trasposta è:")
    print(matr_trasposta)

def somma_elementi(matrice):
    somma = np.sum(matrice)
    print("\nLa somma è:")
    print(somma)

menu()

