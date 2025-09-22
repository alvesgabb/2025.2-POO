class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos = 0  # valor padrão

    # Método get
    def getNumeroServidos(self):
        return self.numeroServidos

    # Método set
    def setNumeroServidos(self, valor):
        if valor >= 0:
            self.numeroServidos = valor
        else:
            print("Valor inválido para número de clientes.")

    # Método para incrementar o número de clientes atendidos
    def incrementeNumeroServidos(self, incremento):
        if incremento > 0:
            novo_valor = self.getNumeroServidos() + incremento
            self.setNumeroServidos(novo_valor)
        else:
            print("O incremento deve ser positivo.")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo: {self.tipoCozinha} | Clientes Servidos: {self.numeroServidos}"