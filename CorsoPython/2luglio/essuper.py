class Animale:
    def __init__(self,nome,età):
        self.nome = nome
        self.età=età
    def fai_suono(self):
        print("Suono generico dell'animale.")

class Leone(Animale):
    def fai_suono(self):
        print(f"Suono del leone. '{self.nome}'")
    
    def caccia(self):
        print("I leoni cacciano le gazzelle")

class Giraffa(Animale):
    def fai_suono(self):
        print(f"Suono della giraffa. '{self.nome}'")

class Pinguino(Animale):
    def fai_suono(self):
        print(f"suono del pinguino. '{self.nome}'")
    def cammina(self):
        print("Il pinguino cammina lentamente")

# Creazione delle istanze delle classi
leone = Leone("Prova Leone", 2)
giraffa = Giraffa("Prova Giraffa", 1)
pinguino = Pinguino("Pingu", 5)

# Utilizzo dei metodi delle classi
leone.fai_suono()
leone.caccia()
giraffa.fai_suono()
pinguino.fai_suono() 
pinguino.cammina()