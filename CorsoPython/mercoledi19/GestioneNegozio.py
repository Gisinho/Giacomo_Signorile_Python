# Dati degli utenti
utenti = {
    "pippo franco": {"password": "cliente", "tipo_utente": "Cliente"},
    "gino paoli": {"password": "amministrazione", "tipo_utente": "Amministrazione"},
    "solo frutta": {"password": "admin", "tipo_utente": "Admin"}
}

# Lista dei prodotti disponibili in inventario
lista_prodotti = {
    "pera": {"prezzo":1.0, "quantità": 25},
    "mela": {"prezzo":2.5, "quantità": 15},
    "banana": {"prezzo":1.5, "quantità": 10},
    "ciliegia": {"prezzo":1.8, "quantità": 5},
    "arancia": {"prezzo":2.2, "quantità": 80},
    "uva": {"prezzo":3.5, "quantità": 20},
    "limone": {"prezzo":2.0, "quantità": 36},
    "pesca": {"prezzo":3.2, "quantità": 13},
    "albicocca": {"prezzo":4.0, "quantità": 11},
    "fragola":{"prezzo":6.0, "quantità": 8}
}

# Richiesta delle credenziali all'utente
username = input("Inserisci il tuo username: ")
password = input("Inserisci la tua password: ")

# Verifica se lo username esiste e la password è corretta
if username in utenti and utenti[username]["password"] == password:
    tipo_utente = utenti[username]["tipo_utente"]
    if tipo_utente == "Admin":
        print("Benvenuto Admin! Hai pieno accesso.")
    elif tipo_utente == "Amministrazione":
        print("Benvenuto Amministrazione! Puoi modificare i contenuti.")
    elif tipo_utente == "Cliente":
        print("Benvenuto Cliente! Puoi visualizzare i contenuti.")
        # Imposta la variabile di controllo per il ciclo principale
        controllo = True
        # Chiede all'utente se vuole iniziare
        selezione = input("Vuoi iniziare (si/no): ").lower()
        # Lista per tenere traccia degli acquisti del cliente
        acquisti_cliente = []

        # Verifica se l'utente vuole iniziare
        if selezione == "si":
        # Inizia il ciclo principale per l'interazione con l'utente
            while controllo:
            # Chiede all'utente se vuole vedere i prodotti
                selezione2 = input("Vuoi vedere i prodotti (si/no): ").lower()
                if selezione2 == "si":
                    # Mostra i prodotti disponibili
                    print("Prodotti disponibili in inventario:")
                    for prodotto in lista_prodotti:
                        print(prodotto)

                    # Chiede all'utente se vuole acquistare prodotti
                selezione3 = input("Vuoi acquistare i prodotti (si/no): ").lower()
                if selezione3 == "si":
                # Chiede quale prodotto l'utente vuole acquistare
                    prodotto_da_acquistare = input("Che prodotto vuoi acquistare? ")
                    if prodotto_da_acquistare in lista_prodotti:
                    # Aggiunge il prodotto alla lista degli acquisti del cliente
                        acquisti_cliente.append(prodotto_da_acquistare)
                
                    # converte la lista in una stringa separata da virgole
                    acquisti_stringa = ", ".join(acquisti_cliente)  
                    print("Hai acquistato: " + acquisti_stringa)
                else:
                # Messaggio di errore se il prodotto non è disponibile
                    print("Prodotto non disponibile")

                # Chiede all'utente se vuole continuare
                continuare = input("Vuoi continuare (si/no): ").lower()
                if continuare != "si":
                # Esce dal ciclo se l'utente non vuole continuare
                    controllo = False
                print("Buona giornata")
else:
    print("Username o password non validi.")

        

