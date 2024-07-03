class MembroSquadra:
    def __init__(self,nome,età):
        self.nome=nome
        self.età=età
    
    def descrivi(self):
        print(f"Il membro della squadra {self.nome} ha {self.età} anni")

class Giocatore(MembroSquadra):
    def __init__(self, nome, età,ruolo,n_maglia):
        super().__init__(nome, età)
        self.ruolo=ruolo
        self.n_maglia=n_maglia
    def gioca_partita(self):
        print(f"Il giocatore {self.nome} ha {self.età} anni di età, è {self.ruolo} ed ha il numero di maglia {self.n_maglia} ")

class Allenatore(MembroSquadra):
    def __init__(self, nome, età,anni_di_esperienza):
        super().__init__(nome, età)
        self.anni_di_esperienza = anni_di_esperienza

    def dirige_allenamento(self):
        print(f"L'allenatore {self.nome} ha {self.età} anni di età, ha {self.anni_di_esperienza} anni di esperienza e conduce gli allenamenti in maniera intensiva")

class Assistente(MembroSquadra):
    def __init__(self, nome, età,specializzazione):
        super().__init__(nome, età)
        self.specializzazione=specializzazione
    def supporta_team(self):
        print(f"L'assistente {self.nome} ha {self.età} anni di età, ed è specializzato in {self.specializzazione}")

# Funzione per creare il giocatore
def crea_giocatore():
    nome = input("Inserisci il nome del giocatore: ")
    età = int(input("Inserisci l'età del giocatore: "))
    ruolo = input("Inserisci il ruolo del giocatore: ")
    n_maglia = int(input("Inserisci il numero di maglia del giocatore: "))
    
    return Giocatore(nome, età, ruolo, n_maglia)

def crea_allenatore():
    nome = input("Inserisci il nome dell'allenatore: ")
    età = int(input("Inserisci l'età dell'allenatore: "))
    anni_esperienza = int(input("Inserisci gli anni di esperienza: "))

    return Allenatore(nome, età, anni_esperienza)
def crea_assistente():
    nome = input("Inserisci il nome dell'assistente: ")
    età = int(input("Inserisci l'età dell'assistente: "))
    specializzazione = input("Inserisci la specializzazione dell'assistente: ")

    return Assistente(nome,età,specializzazione)

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserisci un giocatore")
        print("2. Inserisci un allenatore")
        print("3. Inserisci un assistente")
        print("4. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            giocatore = crea_giocatore()
            giocatore.gioca_partita()
        elif scelta == "2":
            allenatore = crea_allenatore()
            allenatore.dirige_allenamento()
        elif scelta == "3":
            assistente = crea_assistente()
            assistente.supporta_team()
        elif scelta == "4":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Per favore scegli un'opzione valida.")


menu()


"""# Creazione delle istanze delle classi
zanetti=Giocatore("Javier Zanetti", 50,"centrocampista",4)
zanetti.gioca_partita()

inzaghi=Allenatore("Simone Inzaghi", 48,5)
inzaghi.dirige_allenamento()

cannavacciuolo=Assistente("Antonino Cannavacciuolo", 49,"fisioterapia")
cannavacciuolo.supporta_team()"""