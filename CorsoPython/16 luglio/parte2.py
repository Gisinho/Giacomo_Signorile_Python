"""Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere 
di creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle 
elemento per elemento e stampare il risultato.
Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media 
di tutti gli elementi della matrice."""

import numpy as np
def menu():
    matrice = []
    
    while True:
        print("\nMenu:")
        print("1. Creare una nuova matrice 2D di dimensioni specificate con numeri casuali")
        print("2. Estrarre e stampare la sotto-matrice centrale")
        print("3. Trasporre la matrice e stamparla")
        print("4. Calcolare e stampare la somma di tutti gli elementi della matrice")
        print("5. Crea seconda matrice e calcola il prodotto")
        print("6. Calcolo media degli elementi")
        print("7. Calcolare e stampare il determinante della matrice")
        print("0. Esci")

        scelta = input("Scegli l'opzione: ")

        if scelta == '1':
            matrice,n_righe,n_colonne = crea_matrice()
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
        elif scelta == '5':
            try:
                seconda_matrice = crea_seconda_matrice(n_righe,n_colonne)
                moltiplica_matrici(matrice,seconda_matrice)
            except:
                print("Dati inseriti non corretti")
        elif scelta == '6':
            try:
                media_matrice(matrice)
            except:
                print("Per favore, crea prima una matrice.")
        elif scelta == '7':
            try:
                calcola_determinante(matrice)
            except:
                print("La matrice non è quadrata, impossibile calcolare il determinante.")
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
    return matrice,n_righe,n_colonne

def crea_seconda_matrice(n_righe,n_colonne):
    seconda_matrice = np.random.randint(1,100, size=(int(n_righe),int(n_colonne)))
    print("Seconda matrice creata:")
    print(seconda_matrice)
    return seconda_matrice
def moltiplica_matrici(matrice,seconda_matrice):
    matrice_prodotto = matrice*seconda_matrice
    print("La matrice prodotto:")
    print(matrice_prodotto)

def media_matrice(matrice):
    media = np.mean(matrice)
    print("La media è:")
    print(f"{media:.2f}")

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

def calcola_determinante(matrice):
    if matrice.shape[0] != matrice.shape[1]:
        print("La matrice non è quadrata")
    else:
        determinante = np.linalg.det(matrice)
        print(f"Il determinante della matrice è: {determinante:.2f}")

menu()