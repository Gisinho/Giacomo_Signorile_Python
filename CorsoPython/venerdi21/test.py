# Inizializzare i tentativi
tentativi = 0
numero = False

# Chiedo all'utente di inserire un numero intero
while tentativi < 3:
    n = int(input("Inserisci un numero intero: "))
    if n > 0:
        numero = n
        break
    else:
        print("Il numero non è positivo.")
        tentativi += 1

# Verifico se i tentativi sono stati esauriti
if numero is False:
    print("Hai finito i tentativi.")
else:
    somma_dispari = 0

    # Stampare i numeri pari e calcolare la somma dei numeri dispari
    for num in range(numero + 1):
        if num % 2 == 0:
            print(num, "PARI")
        else:
            somma_dispari += num

    print(f"La somma dei numeri dispari da 0 a {numero} è: {somma_dispari}")

    # Verifico se la somma dei numeri dispari supera 250
    if somma_dispari > 250:
        print("hai vinto")
