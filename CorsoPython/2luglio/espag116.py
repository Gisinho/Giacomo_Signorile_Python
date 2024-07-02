"""Esercizio: Analizzatore di Dati di Vendita
Sei stato incaricato di scrivere un programma Python che analizza un insieme di dati di vendita. I dati di vendita sono rappresentati come una lista di numeri, dove ciascun numero rappresenta l'importo totale delle vendite in un giorno specifico. Il tuo programma dovrebbe fare quanto segue:
Requisiti:
Inserimento dei Dati: Chiedi all'utente di inserire una serie di importi di vendita, separati da spazi. Converti questi importi in una lista di numeri interi.
Gestione delle Eccezioni: Durante la conversione degli importi in numeri interi, gestisci qualsiasi ValueError che possa sorgere a causa di un inserimento errato (ad esempio, l'utente inserisce una lettera invece di un numero), informando l'utente dell'errore e chiedendogli di reinserire i dati.
Calcolo del Totale e della Media: Calcola il totale e la media delle vendite. Stampa entrambi i valori con un messaggio appropriato. Se la lista è vuota (ad esempio, se l'utente non inserisce alcun dato), stampa un messaggio che indica che non sono presenti dati di vendita.
Vendite Sopra la Media: Trova e stampa una lista di tutti i giorni in cui le vendite hanno superato la media delle vendite di tutto il periodo. Assicurati di gestire correttamente il caso in cui non ci siano vendite sopra la media.
Visualizzazione dei Risultati: Per ogni punto sopra, stampa i risultati in modo chiaro e leggibile, con messaggi appropriati che spiegano cosa sta mostrando il programma."""


class DatiVendita:
    
    def __init__(self):
        self.importi_vendita = []

    def inserimento_dati(self):
        while True:
            importi = input("Inserisci una serie di importi di vendita separati da spazi: ")
            importi_vendita_temp = []
            err = False
            for importo in importi.split():
                try:
                    importi_vendita_temp.append(float(importo))
                except ValueError:
                    print(f"{importo} non valido")
                    err = True
            if not err:
                self.importi_vendita = importi_vendita_temp #Se non ci sono errori, asssegno l'attributo alla variabile temp
                break
            else:
                print("Riprova inserisci solo numeri")

    def calcolo_totale_e_media(self):
        if not self.importi_vendita:
            return 0
        totale = sum(self.importi_vendita)
        media = totale / len(self.importi_vendita)
        return totale, media
    def vendite_sopra_la_media(self, media):
    # Trova e restituisce le vendite sopra la media usando un ciclo for
        vendite_sopra_media = []
        for vendita in self.importi_vendita:
            if vendita > media:
                vendite_sopra_media.append(vendita)
        return vendite_sopra_media

# Creazione di un'istanza della classe 
dati_vendita = DatiVendita()

# Richiamo del metodo inserimento_dati
dati_vendita.inserimento_dati()

# Richiamo del metodo calcolo_totale_e_media
totale, media = dati_vendita.calcolo_totale_e_media()

# Stampa dei risultati
print(f"Totale delle vendite: {totale}")
print(f"Media delle vendite: {media}")
    
