"""Es riassuntivo
Hai 40 min per creare un esercizio che rappresenti tutto quello 
che hai imparato nella settimana precedente: """

#Funzione aggiungere film
def aggiungi_film():
    titolo = input("Inserisci il titolo del film: ")
    genere = input("Inserisci il genere: ")

    with open("film.csv", "a") as file:
        file.write(f"{titolo},{genere}")
        print("Film aggiunto con successo.")

#Funzione per visualizzare i film
def visualizza_film():
        # Apre il file film.csv in reading
        with open("film.csv", "r") as file:
            print("\nLista dei film:")
            #itera attraverso ciascuna linea del file
            for line in file:
                titolo, genere = line.strip().split(',')
                print(f"Titolo: {titolo}, Genere: {genere}")
        print()


#Funzione aggiungere la prenotazione
def aggiungi_prenotazione():
    # Richiede l'input dell'utente per il nome, il titolo del film e il numero di posti
    nome = input("Inserisci il tuo nome: ")
    titolo_film = input("Inserisci il titolo del film che vuoi prenotare: ")
    posti = input("Inserisci il numero di posti da prenotare: ")

    # Apre il file prenotazioni.txt in modalità append e scrive i dettagli della prenotazione
    with open("prenotazioni.csv", "a") as file:
        file.write(f"{nome},{titolo_film},{posti}\n")
        print(f"Prenotazione per '{titolo_film}' effettuata con successo")

#Funzione per visualizzare la prenotazione
def visualizza_prenotazioni():  
    print("visualizza prenota")

def menu():
    while True:
        print("Gestonale Cinema")
        print("1. Aggiungi film")
        print("2. Visualizza film")
        print("3. Aggiungi prenotazione")
        print("4. Visualizza prenotazioni")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            aggiungi_film()
        elif scelta == "2":
            visualizza_film()
        elif scelta == "3":
            aggiungi_prenotazione()
        elif scelta == "4":
            visualizza_prenotazioni()
        elif scelta == "5":
            break
        else:
            print("Opzione non valida.")
            break
            

menu()