"""Es riassuntivo
Hai 40 min per creare un esercizio che rappresenti tutto quello 
che hai imparato nella settimana precedente: """
#Funzione aggiungere film
def aggiungi_film():
    titolo = input("Inserisci il titolo del film: ")

#Funzione per visualizzare i film
def visualizza_film():
    print("Visualizza film")

#Funzione aggiungere la prenotazione
def aggiungi_prenotazione():
    print("aggiunta prenotazione")

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