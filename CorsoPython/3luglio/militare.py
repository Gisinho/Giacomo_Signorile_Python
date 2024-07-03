class UnitaMilitare:
    tipo = "UnitaMilitare"
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome} si sta muovendo.")

    def attacca(self):
        print(f"{self.nome} sta attaccando.")

    def ritira(self):
        print(f"{self.nome} si sta ritirando.")

class Fanteria(UnitaMilitare): 
    tipo="Fanteria"
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.difesa = 0
    
    def costruisci_trincea(self):
        self.difesa += 1
        print(f"{self.nome} sta costruendo difese temporanee. Livello difesa: {self.difesa}")

class Artiglieria(UnitaMilitare):
    tipo = "Artiglieria"
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    def calibra_artiglieria(self):
        print(f"{self.nome} sta calibrando i pezzi di artiglieria per la precisione.")


class Cavalleria(UnitaMilitare):
    tipo = "Cavalleria"
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    
    def esplora_terreno(self):
        km = int(input("Inserisci quanto terreno vuoi esplorare in km?: "))
        print(f"{self.nome} sta esplorando l'area di {km} km per raccogliere informazioni sul nemico")

class SupportoLogistico(UnitaMilitare):
    tipo = "SupportoLogistico"
    rifornimento = {}
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def rifornisci_unita(self):
        tipo_rifornimento = input("Tipo di rifornimento: ")
        quantità = input("Inserire la quantità: ")

        if tipo_rifornimento in self.rifornimento:
            self.rifornimento[tipo_rifornimento] += quantità
        else:
            self.rifornimento[tipo_rifornimento] = quantità 
        print(f"{self.nome} sta gestendo il rifornimento di un'altra unità.")

class Ricognizione(UnitaMilitare):
    tipo = "Ricognizione"
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def conduci_ricognizione(self):
        print(f"{self.nome} sta conducendo missioni di sorveglianza.")

class ControlloMilitare():
    def __init__(self):
        self.unita_registrate = []
        self.tipologia = {}
    
    def registra_unita(self, unità):
        self.unita_registrate.append(unità)
        t_unità = [Ricognizione.tipo,Artiglieria.tipo,Fanteria.tipo,SupportoLogistico.tipo,Cavalleria.tipo]
        for i in t_unità:
            i+=1 # incrementa il conto del tipo sul dizionario

        print(f"Unità {unità} registrata.")
    # metodo per mostrare numero di unità registrate per tipo
    def mostra_unita(self):
        for unità, numero in self.tipologia.items():
            print(f"Unità {unità}:{numero}")
    
    def dettagli_unita(self, nome): # metodo per mostrare le unità registrate
        
        for unità in self.tipologia:
            if unità.nome == nome:
                print(f"Dettagli dell'unità {nome}:")
                print(f"Nome: {unità.nome}")
                print(f"Numero di soldati: {unità.numero_soldati}")
                print(f"Tipo: {unità.tipo}")
                return
        print(f"Unità con nome {nome} non trovata.")


controllo = ControlloMilitare()

fanteria1 = Fanteria("Fanteria Alpha", 100)
fanteria2 = Fanteria("Fanteria Bravo", 150)
artiglieria1 = Artiglieria("Artiglieria1", 50)
cavalleria1 = Cavalleria("Cavalleria1", 75)
supporto_logistico1 = SupportoLogistico("Supporto Prova", 30)
ricognizione1 = Ricognizione("Ricognizione Prova", 20)
    

controllo.registra_unita(fanteria1)
controllo.registra_unita(artiglieria1)

controllo.mostra_unita()