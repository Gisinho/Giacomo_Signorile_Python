"""
GRUPPO: GIACOMO SIGNORILE, VALENTINA TRULLI
Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
Il programma deve presentare un menu interattivo che consente all'utente di eseguire 
varie operazioni sulla matrice. Le operazioni disponibili includono:
Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma.
Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere 
di creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle 
elemento per elemento e stampare il risultato.
Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media 
di tutti gli elementi della matrice.
Parte 3: Ulteriore Estensione del Menu Interattivo
Estendere ulteriormente il programma precedente aggiungendo nuove opzioni al menu per permettere ulteriori operazioni sulla matrice. Le nuove operazioni includono:
Calcolare la matrice inversa (se la matrice è quadrata e invertibile).
Applicare una funzione matematica a tutti gli elementi della matrice (ad esempio, sin, cos, exp).
Filtrare e visualizzare solo gli elementi della matrice che soddisfano una determinata condizione (ad esempio, maggiori di un certo valore).
RENDERE OGNI PARTE RICHIAMABILE SINGOLARMENTE
Uscire dal programma.
Tutti i dati necessari al programma possono essere randomizzati o chiesti da inserire all’utente. 
"""

import numpy as np
def menu():
    matrice = None
    
    while True:
        print("\nMenu:")
        print("1. Creare una nuova matrice 2D di dimensioni specificate con numeri casuali")
        print("2. Estrarre e stampare la sotto-matrice centrale")
        print("3. Trasporre la matrice e stamparla")
        print("4. Calcolare e stampare la somma di tutti gli elementi della matrice")
        print("5. Crea seconda matrice e calcola il prodotto")
        print("6. Calcolo media degli elementi")
        print("7. Calcolare e stampare il determinante della matrice")
        print("8. Calcolare la matrice inversa")
        print("9. Applica funzione matematica coseno")
        print("10. Filtra e visualizza gli elementi > di un valore")
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
            if matrice is not None:
                matrice_trasposta(matrice)    
            else:
                print("Per favore, crea prima una matrice.")
        elif scelta == '4':
            if matrice is not None:
                somma_elementi(matrice)               
            else:
                print("Per favore, crea prima una matrice.")
        elif scelta == '5':
            try:
                seconda_matrice = crea_seconda_matrice(n_righe,n_colonne)
                moltiplica_matrici(matrice,seconda_matrice)
            except:
                print("Bisogna generare la prima matrice")
        elif scelta == '6':
            try:
                media_matrice(matrice)
            except:
                print("Per favore, crea prima una matrice.")
        elif scelta == '7':
            try:
                calcola_determinante(matrice)
            except:
                print("La matrice non presente o non quadrata, impossibile calcolare il determinante.")
        elif scelta == '8':
            try:
                matrice_inversa(matrice)
            except:
                print("La matrice non presente o non quadrata, impossibile calcolare la matrice inversa.")
        elif scelta == '9':
            try:
                coseno_matrice(matrice)
            except:
                print("Per favore, crea prima una matrice.")
        elif scelta == '10':
            try:
                filtra_elementi_maggiori(matrice)
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
    
def matrice_inversa(matrice):
    if matrice.shape[0] != matrice.shape[1]:
        print("La matrice non è quadrata")
    else:
        det = np.linalg.det(matrice)
        if det != 0:            
            matrice_inversa=np.linalg.inv(matrice)
            print(matrice_inversa)
        else:
            print("La matrice non è invertibile")

def coseno_matrice(matrice):
    # Calcolo del coseno di ciascun elemento della matrice
    coseno_matrice = np.cos(matrice)
    print("\nMatrice dei coseni:")
    print(coseno_matrice)
    return coseno_matrice

def filtra_elementi_maggiori(matrice):
    valore = int(input("Inserisci un valore: "))
    elementi_filtrati = matrice[matrice>valore]
    print(f"\nElementi della matrice maggiori di {valore}:")
    print(elementi_filtrati)
    return elementi_filtrati



menu()
