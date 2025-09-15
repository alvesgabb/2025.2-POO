""" 1) Crie uma classe chamada Carro. A classe deve ter um método construtor que inicializa os seguintes atributos:

marca: a marca do carro.
modelo: o modelo do carro.
ano: o ano de fabricação do carro.
cor: a cor do carro.
Crie dois objetos dessa classe, cada um com atributos diferentes, e imprima as informações dos carros. """


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print("-------------------------")

carro1 = Carro("Toyota", "Corolla", 2020, "Prata")
carro2 = Carro("Ford", "Mustang", 2023, "Vermelho")

carro1.mostrar_informacoes()
carro2.mostrar_informacoes()
