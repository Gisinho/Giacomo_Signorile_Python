class Studenti:
    corpo_studentesco=0
    ore_settimanali = 36
    def __init__(self,nome,cognome,voti):
        self.nome=nome
        self.cognome=cognome
        self.voti=voti
        Studenti.corpo_studentesco+=1

    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Voti: {self.voti}, Ore settimanali: {self.ore_settimanali}"

    def visualizza_nome(self):
        print(self.nome) #Metodo getter
    
    def inserisci_nome(self):
        self.nome = input("Inserisci il nome: ")


Giovanni = Studenti("Giovanni","filippo",[4,5])
Tommaso = Studenti("tommaso","muraca",[7,8])
Andrea = Studenti("andrea","piccolo",[4,8])

Giovanni.inserisci_nome()
print(Giovanni)

Andrea.ore_settimanali+=4

print(Andrea)
print(Studenti.corpo_studentesco)
