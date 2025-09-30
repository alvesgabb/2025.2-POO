from cartaoweb import CartaoWeb

class Aniversario(CartaoWeb):
    def __init__(self, destinatario):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Aniversário, {self.destinatario}! Que seu dia seja incrível.")


