# Inizializzazione della lista con 5 frutti
lista = ["Mela", "Banana", "Arancia", "Pera", "Ananas"]

# Visualizzazione del menu
print("\nMenu:")
print("1. Aggiungi")
print("2. Rimuovi")
print("3. Visualizza")
print("4. Esci")

# Lettura della scelta dell'utente
scelta = input("Seleziona un'opzione: ")

# Gestione delle scelte dell'utente
if scelta == "1":
    # Aggiungi un elemento alla lista
    elemento = input("Inserisci l'elemento da aggiungere: ")
    lista.append(elemento)
    print('Elemento "' + elemento + '" aggiunto con successo.')
    
elif scelta == "2":
    # Rimuovi un elemento dalla lista
    elemento = input("Inserisci l'elemento da rimuovere: ")
    # Se l'elemento è presente nella lista
    if elemento in lista:
        lista.remove(elemento)
        print('Elemento "' + elemento + '" rimosso con successo.')
    else:
        print('Elemento "' + elemento + '" non trovato nella lista.')
        
elif scelta == "3":
    # Visualizza la lista degli elementi
    if lista:
        print("Gli elementi nella lista sono:")
        # Visualizza ciascun elemento nella lista (senza usare cicli)
        if len(lista) > 0:
            print('1. ' + lista[0])
        if len(lista) > 1:
            print('2. ' + lista[1])
        if len(lista) > 2:
            print('3. ' + lista[2])
        if len(lista) > 3:
            print('4. ' + lista[3])
        if len(lista) > 4:
            print('5. ' + lista[4])
        # Aggiungi ulteriori condizioni se la lista può contenere più di 5 elementi
    else:
        print("La lista è vuota.")
        
elif scelta == "4":
    # Esci dal programma
    print("Uscita dal programma...")
    
else:
    # Scelta non valida
    print("Opzione non valida, riprova.")