booleano = input("Inserisci l'elemento booleano: ")
numero = input("Inserisci il numero intero: ")
stringa = input("Inserisci la stringa: ")

#Inserisco i valori nella lista
lista = [booleano, numero, stringa]

#Inserisco la lista nel dizionario
dizionario = {
    "tipididato":lista
}
print(dizionario)