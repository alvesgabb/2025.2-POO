"""O programa principal (main) deverá:
Criar pelo menos dois veículos diferentes, com placas, modelos e valores de diárias distintos.
Alugar um veículo e exibir seu status.
Devolver o veículo e exibir novamente o status.
Exibir a placa do veículo e tentar modificá-la para verificar o encapsulamento.
Exibir o total de veículos cadastrados usando o método de classe.
Calcular e exibir o valor do aluguel de um dos veículos para um número de dias usando o método estático.
"""
from veiculo import Veiculo

#Criação de veículos
carro1=Veiculo("123456","Fiat",250)
carro2=Veiculo("654321","Honda",350)

#Alugando véiculo e exibindo status.
print("\nAlugando veículo e exibindo status:")
carro1.alugar()
carro1.status()
print("-"*30)

#Devolvendo véiculo e exibir status.
print("\nDevolvendo veículo:")
carro1.devolver()
carro1.status()
print("-"*30)

#Exibindo a placa do veículo e tentando modificá-la para verificar o encapsulamento.
print("\nExibindo placa do veículo e tentando modificá-la:")
print(f"Placa do {carro1.modelo}: {carro1.placa}")
carro1.placa=20
print("-"*30)


#Exibindo o total de veículos cadastrados usando o método de classe.
print("\nExibindo total de veículos cadastrados:")
Veiculo.mostrar_total_veiculos()
print("-"*30)


#Calculando e exibindo o valor do aluguel de um dos veículos para um número de dias usando o método estático.
valor = carro1.calcular_preco_aluguel(2, 250)
print("\nValor do aluguel do veículo:")
print(f"R${valor:.2f}")
