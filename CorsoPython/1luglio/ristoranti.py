class Ristorante:
    # attributi di classe
    aperto = False #stato iniziale risto
    menu = {}
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        

    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} ha una cucina {self.tipo_cucina}.")

    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è aperto.")
        else:
            print(f"Il ristorante {self.nome} è chiuso.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è ora aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è ora chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        piatto = input("Inserisci il nome: ")
        prezzo = float(input("Inserisci il prezzo: "))
        self.menu[piatto] = prezzo
        print(f"{piatto} è stato aggiunto al menu.")
    
    def togli_dal_menu(self, piatto):
        prezzo = self.menu.pop(piatto)
        if prezzo:
            print(f"{piatto} è stato rimosso dal menu.")
        else:
            print(f"{piatto} non è presente nel menu.")
    
    def stampa_menu(self):
        print("Menu del ristorante:")
        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: €{prezzo}")

# Test della classe
ristorante = Ristorante("shaolin", "cinese")

# Test dei metodi
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.stato_apertura()
ristorante.aggiungi_al_menu("ravioli", 12)
ristorante.aggiungi_al_menu("nuvola di drago", 8)
ristorante.stampa_menu()
ristorante.togli_dal_menu("ravioli")
ristorante.stampa_menu()
ristorante.chiudi_ristorante()
ristorante.stato_apertura()