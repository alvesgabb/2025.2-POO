from cartaoweb import CartaoWeb

class Natal(CartaoWeb):
   def __init__(self, destinatario):
      super().__init__(destinatario)
    
   def showMessage(self):
       print(f"Feliz Natal, {self.destinatario}! Que a mágia do Natal aqueça seu coração.")
       print("-"*35)

