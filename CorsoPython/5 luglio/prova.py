"Incapsulamento: si riferisce all’idea di nascondere i dettagli di implementazione di un oggetto e di esporre solo le sue funzionalità essenziali." 
#Esempio: 
def __init__(self, saldo_iniziale):  
    self.__saldo = saldo_iniziale 
"in questo caso l'attributo saldo diventa privato."  


"Ereditarietà: permette di creare nuove classi basate su classi esistenti, ereditandone proprietà e metodi consentendo  di riutilizzare il codice Esempio:" 
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def descrizione(self):
        return f"{self.marca} {self.modello}"

class Automobile(Veicolo):
    def __init__(self, marca, modello, tipo_carburante):
        super().__init__(marca, modello)
        self.tipo_carburante = tipo_carburante

    def descrizione(self):
        return f"{super().descrizione()}, {self.tipo_carburante}" 
"in questo caso la classe Automobile eredita tramite il costruttore le caratteristiche della classe base Veicolo. "  



"Polimorfismo: si riferisce alla capacità di un oggetto di assumere diverse forme. In Python, il polimorfismo si manifesta principalmente attraverso l'overriding dei metodi. Esempio "
class Animale:
    def parla(self):
        pass

class Cane(Animale):
    def parla(self):
        return "Bau"

class Gatto(Animale):
    def parla(self):
        return "Miao"

def fai_parlare(animale):
    print(animale.parla())

#PROVE
cane = Cane()
gatto = Gatto()

fai_parlare(cane) 
fai_parlare(gatto)
"in questo caso la funzione parla() della claase Gatto sovrascrive la funzione parla() della classe animale cambiandone il funzionamento."