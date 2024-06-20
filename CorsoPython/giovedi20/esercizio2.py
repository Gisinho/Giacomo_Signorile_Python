#PUNTO 1
numero=int(input("Inserisci un numero: "))

if numero%2==0:
    print("PARI")
#else:
    print("DISPARI")

#PUNTO2
controllo_ciclo=True
while controllo_ciclo:
    numero=int(input("Inserisci un numero: "))
    for i in range(numero,-1, -1):
        print(i)


#PUNTO3
# Chiedo all'utente quanti numeri vuole inserire
conteggio = int(input("Quanti numeri vuoi inserire?: "))

# Inizializzo le liste vuote
numeri = []
quadrati = []

# Chiedo all'utente di inserire i numeri
for num in range(conteggio):
    numero = int(input("Inserisci un numero: "))
    
    if numero > 0:
        
        # Aggiungo il numero alla lista dei numeri
        numeri.append(numero)
    
        # Calcolo il quadrato del numero
        numero_al_quadrato = numero ** 2
    
        # Aggiungo il quadrato alla lista dei quadrati
        quadrati.append(numero_al_quadrato)
        # Trova il numero massimo nella lista
        numero_massimo = max(numeri)
        print("Numero massimo nella lista:", numero_massimo)
    elif numero ==0:
        print("Lista vuota")
    else:
        print("Numero inserito non valido")


# Stampo le liste finali
print("Numeri inseriti:", numeri)
print("Quadrati dei numeri:", quadrati)




