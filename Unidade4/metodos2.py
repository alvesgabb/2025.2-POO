class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos=15

    def descreverRestaurante(self):
        print(f"Restaurante: {self.nomeRestaurante}")
        print(f"Tipo de Cozinha: {self.tipoCozinha}\n")

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está ABERTO!\n")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo de Cozinha: {self.tipoCozinha}"
    
    def getNumeroServidos(self):
        return self.numeroServidos
    def setNumeroServidos(self,novo_numeroservidos):
        self.numeroServidos=novo_numeroservidos

    def incrementarNumeroServidos(self,quantidade):
        numero_atual = self.getNumeroServidos()
        novo_numero = numero_atual+quantidade
        self.setNumeroServidos(novo_numero)


        
    
    

    
    