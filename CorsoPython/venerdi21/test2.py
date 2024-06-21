#Chiedo all'utente di inserire una stringa.
stringa=input("Inserisci una stringa: ")

vocali = "aeiouAEIOU"
conta_vocali = 0

# Conta le vocali nella stringa
for carattere in stringa:
    if carattere in vocali:
        conta_vocali += 1

# Stampare il numero di vocali trovate
print("Numero di vocali nella stringa è:", conta_vocali)