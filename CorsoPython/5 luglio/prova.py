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
    def emetti_suono(self): 
        print("Suono generico")      

class Gatto(Animale):
    def emetti_suono(self): 
        print("miao")  
"in questo caso l'emetti suono della claase Gatto sovrascrive l'emetti suono della classe animale cambiandone il funzionamento."