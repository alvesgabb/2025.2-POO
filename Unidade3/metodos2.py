class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        print(f"Restaurante: {self.nomeRestaurante}")
        print(f"Tipo de Cozinha: {self.tipoCozinha}\n")

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está ABERTO!\n")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo de Cozinha: {self.tipoCozinha}"