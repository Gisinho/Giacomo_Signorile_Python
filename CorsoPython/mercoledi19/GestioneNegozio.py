# Imposta la variabile di controllo per il ciclo principale
controllo = True

# Chiede all'utente se vuole iniziare
selezione = input("Vuoi iniziare (si/no): ").lower()

# Lista dei prodotti disponibili in inventario
lista_prodotti = [
    ["pera", 1.50, 10],
    ["mela", 1.20, 15],
    ["banana", 1.80, 12],
    ["ciliegia", 2.00, 20],
    ["arancia", 1.00, 25],
    ["uva", 2.50, 8],
    ["limone", 1.10, 18],
    ["pesca", 2.20, 10],
    ["albicocca", 2.30, 5],
    ["fragola", 3.00, 6]
]

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
                print(prodotto[0])

        # Chiede all'utente se vuole acquistare prodotti
        selezione3 = input("Vuoi acquistare i prodotti (si/no): ").lower()
        if selezione3 == "si":
            # Chiede quale prodotto l'utente vuole acquistare
            prodotto_da_acquistare = input("Che prodotto vuoi acquistare? ")
            if prodotto_da_acquistare in lista_prodotti[0]:
                # Aggiunge il prodotto alla lista degli acquisti del cliente
                acquisti_cliente.append(prodotto_da_acquistare)
                print("Hai acquistato: " + prodotto_da_acquistare)
            else:
                # Messaggio di errore se il prodotto non è disponibile
                print("Prodotto non disponibile")

        # Chiede all'utente se vuole continuare
        continuare = input("Vuoi continuare (si/no): ").lower()
        if continuare != "si":
            # Esce dal ciclo se l'utente non vuole continuare
            controllo = False

    # Mostra gli acquisti del cliente
    print("I tuoi acquisti:")
    for acquisto in acquisti_cliente:
        print(acquisto)

else:
    # Messaggio di saluto se l'utente non vuole iniziare
    print("Arrivederci")
