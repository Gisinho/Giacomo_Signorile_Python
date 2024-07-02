"""Create una classe calciatore che ha come attributi:
-nome:
- ruolo:
- valore.
Create un metodo getter per avere solo i valori dei calciatori 
e un metodo setter per settare il ruolo del calciatore.
create almeno 3 calciatori e poi printate in ordine di valore 
i calciatori.
"""

class Calciatori:
    Calciatore = 0
    def __init__(self,nome,ruolo,valore):
        self.nome=nome
        self.ruolo=ruolo
        self.valore=valore
        Calciatori.Calciatore +=1
    def __str__(self):
        return f"Nome: {self.nome}, Ruolo: {self.ruolo}, Valore: {self.valore}"
    # Getter per ottenere il valore del calciatore
    def get_valore(self):
        return self.valore
    
    def set_ruolo(self):
        self.ruolo = input("Inserire nuovo ruolo: ")


    # Setter per impostare il ruolo del calciatore
    def set_ruolo(self, cambia_ruolo):
        self.ruolo = cambia_ruolo
    
    def visualizza_nome(self):
        print(self.nome,self.ruolo,self.valore)


Cr7 = Calciatori("Cristiano Ronaldo","attaccante",10)
Gagliardini = Calciatori("Roberto Gagliardini","centrocampista",2)
Thuram = Calciatori("Marcus Thuram","attaccante",7)

# Lista dei calciatori
calciatori_valore = [Cr7.get_valore(),Gagliardini.get_valore(),Thuram.get_valore()]


calciatori = [Cr7,Gagliardini,Thuram]

calciatori_valore.sort(reverse=True)
print(calciatori_valore)

