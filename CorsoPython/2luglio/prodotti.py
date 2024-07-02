class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita

    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario and self.inventario[prodotto.nome] >= quantita:
            self.inventario[prodotto.nome] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Profitto realizzato: {profitto}")

    def resi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita

# Creazione dei prodotti
tv = Elettronica("TV", 100, 150, 2)
camicia = Abbigliamento("Camicia", 20, 50, "Lino")

# Creazione della fabbrica
fabbrica = Fabbrica()

# Aggiunta prodotti all'inventario
fabbrica.aggiungi_prodotto(tv, 10)
fabbrica.aggiungi_prodotto(camicia, 20)

# Vendita 
fabbrica.vendi_prodotto(tv, 2)
fabbrica.vendi_prodotto(camicia, 5)

# Resi
fabbrica.resi_prodotto(tv, 1)
fabbrica.resi_prodotto(camicia, 2)