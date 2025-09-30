from cartaoweb import CartaoWeb

class DiaDosNamorados(CartaoWeb):
   def __init__(self, destinatario):
      super().__init__(destinatario)
    
   def showMessage(self):
       print(f"Feliz dia dos Namorados, {self.destinatario}! Que o amor esteja sempre em seu coração.")
       print("-"*35)