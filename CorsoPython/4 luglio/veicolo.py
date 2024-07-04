class Veicolo:
    def __init__(self,marca,modello,anno,accensione):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione=accensione

    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno(self):
        return self.__anno

    def is_accensione(self):
        return self.__accensione
    
    def accendi(self):
        self.__accensione=True
    def spegni(self):
        self.__accensione=False

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, accensione, numero_porte):
        super().__init__(marca, modello, anno, accensione)
        self.__numero_porte = numero_porte
    
    def suona_clacson(self):
        print(f"Suona clacson: {self.marca} - {self.modello}")

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, accensione, capacita_carico, capacita_scarico):
        super().__init__(marca, modello, anno, accensione)
        self.__capacita_carico = capacita_carico
        self.__capacita_scarico = capacita_scarico

    def carica(self):
        print(f"Puo caricare: {self.__capacità_carico}")
    
    def scarica(self):
        print(f"Puo scaricare: {self.__capacità_scarico}")

class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, accensione, tipo):
        super().__init__(marca, modello, anno, accensione)
        self.__tipo = tipo
    
    def esegui_wheelie(self):
        if self.__tipo=="sportivo":
            print("Hai eseguito un wheeliee")
        else:
            print("Non hai eseguito un wheelie")

class GestoreParcoVeicoli(Auto,Furgone,Motocicletta):
    def __init__(self):
        self.__veicoli = []
    
    def set_marca(self, marca):
        self.__marca = marca

    def set_modello(self, modello):
        self.__modello = modello

    def set_anno(self, anno):
        self.__anno = anno

    def set_accensione(self, accensione):
        self.__accensione = accensione
    
    def aggiungi_veicolo(self, veicolo):
        self.__veicoli.append(veicolo)
        
    def lista_veicoli(self):
        for veicolo in self.__veicoli:
            print(f"Marca: {veicolo.get_marca()}, Modello: {veicolo.get_modello()}, Anno: {veicolo.get_anno()}, Accensione: {veicolo.is_accensione()}")
    
    def rimuovi_veicolo(self, marca, modello):
        for veicolo in self.__veicoli:
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello:
                self.__veicoli.remove(veicolo)
                print(f"Rimosso: {marca} {modello}")
            else:
                print(f"Veicolo non trovato: {marca} {modello}")

#Prove
veicolo = GestoreParcoVeicoli()

auto = Auto("Fiat", "Panda", 1990, False, 4)
veicolo.aggiungi_veicolo(auto)

furgone = Furgone("Fiat", "Fiorino", 2021, False, 1000, 800)
furgone1 = Furgone("Fiat", "Furgone", 2021, True, 1000, 800)
veicolo.aggiungi_veicolo(furgone)

moto = Motocicletta("Ducati", "9", 2024, False, "sportivo")
moto1 = Motocicletta("Piaggio", "Prova", 2024, True, "non sportiva")
veicolo.aggiungi_veicolo(moto)

# Rimuovi un veicolo
veicolo.rimuovi_veicolo("Fiat", "Fiorino")

veicolo.lista_veicoli()