class ContoBancario:
    
    def __init__(self):
        self.__titolare = "Alfredo Alcaldo"
        self.__saldo = 1200.30
    
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self):
        return self.__titolare
    
    def get_saldo(self):
        return self.__saldo
    
    def deposita(self,importo): #Aggiunge un importo al saldo del conto se l'importo è positivo
        if importo > 0:
            self.__saldo += importo
        else:
            print("L'importo deve essere un numero positivo.")

    def preleva(self,importo): #Sottrae un importo dal saldo del conto se l'importo è positivo
        if importo>0 and self.__saldo >= importo:
            self.__saldo -= importo
        else:
            print("L'importo deve essere positivo e/o fondi insufficienti per prelevare.")
    
    def visualizza_saldo(self):
        return self.__saldo

#Prove
conto = ContoBancario()

print("Titolare:", conto.get_titolare())
print("Saldo iniziale:", conto.visualizza_saldo())

#Dopo depositivo
conto.deposita(50.0)
print("Saldo dopo deposito:", conto.visualizza_saldo())

#Dopo prelievo
conto.preleva(300.0)
print("Saldo dopo prelievo:", conto.visualizza_saldo())


#Cambia il titolare del conto
c = ContoBancario
c.set_titolare("Bevilacqua")
print(c.get_titolare())