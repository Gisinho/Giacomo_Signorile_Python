class MetodoPagamento:
    def effettua_pagamento(self):
        pass

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self):
        return "Pagamento tramite carta di credito."
    
class Paypal(MetodoPagamento):
    def effettua_pagamento(self):
        return "Pagamento tramite paypal"
    
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self):
        return "Pagamento tramite bonifico bancario"
    
class GestorePagamenti(CartaDiCredito,BonificoBancario,Paypal):
    def metodo_pagamento(self,importo):
        print(importo.effettua_pagamento())

#Prove
cartacredito = CartaDiCredito()
paypal = Paypal()
bonifico_bancario = BonificoBancario()
gestore_pagamento = GestorePagamenti()

gestore_pagamento.metodo_pagamento(cartacredito)
gestore_pagamento.metodo_pagamento(paypal)
gestore_pagamento.metodo_pagamento(bonifico_bancario)