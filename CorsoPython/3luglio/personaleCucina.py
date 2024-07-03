class PersonaleCucina:
    
    def __init__(self,nome,età):
        self.nome=nome
        self.età=età

    def lavora(self):
        print(f"{self.nome} sta svolgendo il suo lavoro.")

class Chef(PersonaleCucina):
    def __init__(self, nome, età, specialità):
        super().__init__(nome, età)
        self.specialità = specialità
        self.piatti = []
    
    def lavora(self):
        print(f"Lo chef {self.nome}, specializzato in {self.specialità}, sta preparando nuovi piatti.")
    
    def prepara_menu(self):
        print(f"{self.nome} sta creando un nuovo menu con specialità {self.specialità}.")
    
    def aggiungi_piatto(self, piatto):
        self.piatti.append(piatto)
        print(f"Piatto {piatto} aggiunto da {self.nome}.")    
    
    def mostra_piatti(self):
        print(f"I piatti preparati da {self.nome} sono:")
        for piatto in self.piatti:
            print(f"{piatto}")
    

class SousChef(PersonaleCucina):
    def gestisci_inventario(self):
        print(f"{self.nome} sta gestendo l'inventario della cucina.")

class CuocoLinea(PersonaleCucina):
    def cucina_piatto(self, nome_piatto):
        print(f"{self.nome} prepara il piatto {nome_piatto}.")

# Prove
mario = Chef("Mario", 35, "Italiana")
mario.lavora()
mario.prepara_menu()
mario.aggiungi_piatto("Risotto ai funghi")
mario.aggiungi_piatto("Lasagne")
mario.mostra_piatti()

giacomo = SousChef("Giacomo", 28)
giacomo.gestisci_inventario()

luca = CuocoLinea("Luca", 22)
luca.cucina_piatto("Pasta al pesto")