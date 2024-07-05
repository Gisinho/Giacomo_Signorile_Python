"""Create un gestionale bancario basato sulla programmazione a oggetti, 
la prima parte dell'esercizio riguarda solamente aggiunta e 
eliminazione cliente con il suo conto bancario e modifica cliente"""

class Cliente:
    def __init__ (self, nome, età,carta_credito,cvc):

        self.__nome=nome
        self.__età=età
        self.__carta_credito=carta_credito
        self.__cvc=cvc

    def get_nome(self): 
        return self.__nome
    
    def get_cvc(self):
        return self.__cvc
    
    def set_nome(self, nome):
        self.__nome = nome

class GestoreBanca(Cliente):
    def __init__(self):
        self.__clienti = []
    
    def aggiungi_cliente(self,cliente):
        self.__clienti.append(cliente)
    
    def rimuovi_cliente(self, nome, cvc):
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                self.__clienti.remove(cliente)
                print("Cliente rimosso.")
            else:
                print("Cliente non registrato")
    
    def modifica_nome(self,nome,cvc,nuovo_nome):
        trovato = False
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                cliente.set_nome(nuovo_nome)                
                trovato=True
        if trovato == True:
            print("Hai modificato il nome")
        else:
            print("Utente non trovato")
    
    def lista_clienti(self):
        for cliente in self.__clienti:
            print(f"Lista clienti: {cliente.get_nome()}")
        


def menu():
    print("""\n1. Apri conto
2. Chiudi conto
3. Modifica cliente
4. Lista clienti
0. Esci
""")
    

banca=GestoreBanca()

while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        while True:
            nome=input("Inserisci il nome del nuovo cliente: ")
            if nome.isalpha():
                break
            else:
                print("Inserisci solo lettere")
        while True:
            try:
                eta=int(input("Inserisci l'età del cliente: "))
                break
            except:
                print("ERRORE")
        while True:
            try:
                carta_credito=int(input("Inserisci il numero della carta di credito: "))
                break
            except:
                print("ERRORE")
        while True:
            cvc=input("Inserisci il cvc della carta: ")
            if len(cvc)!=3:
                print("cvc non conforme")
            else:
                break
        nuovo_cliente=Cliente(nome, eta,carta_credito,cvc)
        banca.aggiungi_cliente(nuovo_cliente)
        print("Cliente aggiunto con successo.")
    elif scelta=="2":       #RIMUOVI CLIENTE
        nome=input("Inserisci il nome del cliente: ")
        cvc=int(input("Inserisci il cvc della carta: "))
        banca.rimuovi_cliente(nome,cvc)
    elif scelta=="3":
        nome=input("Inserisci il vecchio nome del cliente")
        cvc=int(input("Inserisci il cvc della carta: "))
        nuovo_nome=input("Inserisci il nuovo nome del cliente: ")
        banca.modifica_nome(nome,cvc,nuovo_nome)
    elif scelta == "4":
        banca.lista_clienti()
        break
    elif scelta=="0":
        break


    
    

