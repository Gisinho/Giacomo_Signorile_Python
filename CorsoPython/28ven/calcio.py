"""Create un gestionale per la vostra squadra di calcio, siete gli allenatori quindi potete aggiungere massimo 25 calciatori:
3 portieri;
8 difensori;
8 centrocampisti;
6 attaccanti;
per ogni calciatore nome e ruolo.
Nel menù potete aggiungerli, eliminarli o visualizzarli, tutto verrà salvato in un database .txt
file.csv"""

squadra = {"portiere" : 3, "difensore" : 8, "centrocampista" : 8, "attaccante" : 6}

def visualizza_squadra():
    with open("calciatori.csv", "r") as file:
        calciatori = file.read()
    return calciatori

def menu():
    
    while True:
        print('1. Aggiungi giocatore')
        print('2. Elimina giocatore')
        print('3. Visualizza squadra')
        print('4. Esci')
        scelta = input('Seleziona un\'opzione: ')
        if scelta == '1':
            nome = input('Inserisci il nome del giocatore: ')
            ruolo = input('Inserisci il ruolo del giocatore (portiere, difensore, centrocampiste, attaccante): ').lower()
            #aggiungi_giocatore(nome, ruolo)
        elif scelta == '2':
            nome = input('Inserisci il nome del giocatore: ')
            ruolo = input('Inserisci il ruolo del giocatore (portiere, difensore, centrocampiste, attaccante): ').lower()
            #elimina_giocatore(nome, ruolo)
        elif scelta == '3':
            visualizza_squadra()
        elif scelta == '4':
            exit()
        else:
            print('Opzione non valida.')

menu()