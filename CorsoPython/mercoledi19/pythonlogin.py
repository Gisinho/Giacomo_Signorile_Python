utenti = {
    "nome":"admin",
    "pass":"12345",
    "nome":"giacomo",
    "pass":"prova",
}

nome_utente = input("Inserisci il nome utente: ")
password = input("Inserisci la password: ")

# Verifica credenziali inserite
if utenti["nome"] == nome_utente and utenti["pass"] == password:
    print("Ciao", nome_utente)
    print("1. Aggiungi citta")
    print("2. Aggiungi sesso")  
    print("3. Domanda segreta")  

    # Lettura della scelta dell'utente
    scelta = input("Seleziona un'opzione: ")
    if scelta == "1":
        cit=input("Inserisci la città: ")
        utenti["città"] = cit
    elif scelta == "2":
        ses=input("Inserisci la città: ")
        utenti["sesso"] = ses
    elif scelta == "3":
        segreta=input("Inserisci la risposta: ")
        utenti["domandasegreta"] = segreta
    else:
        print("Scelta non valida")
else:
    print("Le credenziali inserite sono errate")
