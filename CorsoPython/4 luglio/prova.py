def __init__(self):
        self.__veicoli = []
    
    def registra_veicolo(self, veicolo):
        self.__veicoli.append(veicolo)
        
    def lista_veicoli(self):
        for veicolo in self.__veicoli:
            print(f"Marca: {veicolo.get_marca()}, Modello: {veicolo.get_modello()}, Anno: {veicolo.get_anno()}, Accensione: {veicolo.is_accensione()}")