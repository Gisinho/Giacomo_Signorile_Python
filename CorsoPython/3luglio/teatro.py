class Posto:
    
    def __init__(self,numero,fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False

    def get_numero(self):
        return self.__numero
    
    def get_fila(self):
        return self.__fila
    
    def is_occupato(self):
        return self.__occupato
    
    def prenota(self): #metodo per prenotare il posto se non è già occupato
        if not self.__occupato:
            self.__occupato=True
        else:
            print("Posto occupato")
    
    def libera(self, libera): #metodo per liberare il posto se occupato
        if self.__occupato:
            self.__occupato = False
        
class PostoVIP(Posto):
    def __init__(self,__numero,__fila,__occupato,__servizi_extra):
        super().__init__(self,__numero,__fila,__occupato)
        self.__servizi_extra = __servizi_extra

    def prenota(self):
        super().prenota()
        if self.is_occupato():        
            print(f"servizi extra prenotati, {self.__servizi_extra}")

class PostoStandard(Posto):
    def __init__(self,__numero,__fila,__occupato):
        super().__init__(self,__numero,__fila,__occupato)
        
    def prenota(self):
        super().prenota()
        if self.is_occupato():
            print("potrebbe avere un costo aggiuntivo  per la prenotazione online o altri servizi meno esclusivi.")


class Teatro(Posto,PostoVIP,PostoStandard):
    
    def __init__(self):
        self.__posti=[]

    def aggiungi_posto(self, posto):
        self.__posti.append(posto)
    
    def stampa_posti_occupati(self):
        for posto in self.__posti:
            if posto.is_occupato():
                print(posto)

# Esempio di utilizzo
t = Teatro()

# Aggiungere posti al teatro
t.aggiungi_posto(PostoStandard(1, "A"))
t.aggiungi_posto(PostoStandard(3, "B"))

t.aggiungi_posto(PostoVIP(2, "A", ["accesso alla piscina", "servizio in posto"]))
