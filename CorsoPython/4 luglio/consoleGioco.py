class Gioco: #Definizione classe base
    def __init__(self,nome): #Metodo costruttore
        self.__nome = nome
        
    def get_nome(self): 
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def inizia_gioco(self): #Metodo sovrascritto nelle classi figlie
        pass
class Sport(Gioco): #Classe figlia
    def __init__(self, nome,tipo_sport): #Metodo costruttore
        super().__init__(nome)
        self.__tipo_sport = tipo_sport

    def inizia_gioco(self): #Metodo ereditato dalla classe padre e sovrascritto 
        print(f"Stai iniziando una partita a {self.get_nome()} - {self.__tipo_sport}")
    
class Avventura(Gioco): #Classe figlia
    def __init__(self, nome, ambientazione): #Metodo costruttore
        super().__init__(nome)
        self.__ambientazione = ambientazione

    def inizia_gioco(self): #Metodo ereditato dalla classe padre e sovrascritto 
        print(f"Stai iniziando una partita a {self.get_nome()} in {self.__ambientazione}")
    
class Console(Sport,Avventura): #Gestore giochi
    def __init__(self): #Metodo costruttore
        self.__partite = []

    def aggiungi_partita(self, partita):
        self.__partite.append(partita)
    
    def visualizza_partite(self):
        print("Partite create: ")
        for partita in self.__partite:
            print(f"{partita.get_nome()}")

    
def menu():
    console = Console() #Creazione oggetto classe Console
    
    while True: #visualizza opzioni menu
        print("\nMenu:") 
        print("1. Inizia partita")
        print("2. Visualizza partite")
        print("3. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == "1":
            tipo_partita = input("Inserisci il tipo di partita (sport/avventura): ")
            nome = input("Inserisci il nome del gioco: ")
            
            if tipo_partita == "sport":
                tipo_sport = input("Inserisci il tipo di sport: ")
                partita = Sport(nome,tipo_sport) #crea oggetto chiamato partita di tipo Sport
                partita.inizia_gioco() #chiama metodo inizia gioco
            elif tipo_partita == "avventura":
                ambientazione = input("Inserisci ambientazione: ")
                partita = Avventura(nome,ambientazione) #crea oggetto chiamato partita di tipo Avventura
                partita.inizia_gioco() #chiama metodo inizia gioco
            else:
                print("Scelta non valida.")
                continue
            
            console.aggiungi_partita(partita)
        
        elif scelta == "2":
            console.visualizza_partite() 
        
        elif scelta == "3":
            print("Sei uscito.")
            break
        else:
            print("Sono baggato")

menu()
        
