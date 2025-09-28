""" 1.	A partir da atividade 2 da unidade 3, acrescente o atributo numeroServidos, cujo valor padrão é 0 (zero). Crie uma instância chamada restaurante, apresente o número de clientes atendidos e, em seguida, mude o valor e exiba-o novamente;
2.	Adicione os métodos getNumeroServidos e setNumeroServidos, para alterar o valor de clientes atendidos. Execute-o com um novo valor de clientes atendidos e, em seguida, apresente o valor novamente;
3.	Acrescente o método incrementeNumeroServidos que permita incrementar o número de clientes servidos, através de um parâmetro passado. Em sua implementação, invoque os métodos getNumeroServidos e setNumeroServidos para incrementar o número de clientes atendidos """
from metodos2 import Restaurante

# Criar 3 objetos Restaurante
r1 = Restaurante("Sabor Nordestino", "Comida regional")
r2 = Restaurante("Pizza Space", "Pizzaria")
r3 = Restaurante("Samurai Sushi", "Comida japonesa")

# Usando descreverRestaurante
print("=== Usando descreverRestaurante ===")
r1.descreverRestaurante()
r2.descreverRestaurante()
r3.descreverRestaurante()

# Usando __str__
print("=== Usando __str__ ===")
print(r1)
print(r2)
print(r3)

# Teste de abrirRestaurante
print("\n=== Teste de abertura ===")
r2.abrirRestaurante()

#Mostrando o número de clientes atendidos
print("Clientes atendidos")
print("Número de clientes atendidos inicialmente:",r1.numeroServidos)

#Novo número de clientes atendidos
print("Novo número de clientes atendidos:",r1.numeroServidos)

#Novos valores de clientes atendidos usando getters e setters
print("\nUsando getters e setters")
print("Número de clientes atendidos inicialmente:",r1.getNumeroServidos())

#Usando set para modificar
r1.setNumeroServidos(40)

#Exibindo valor alterado
print("Novo número de clientes atendidos:",r1.getNumeroServidos())

#invocando os métodos getNumeroServidos e setNumeroServidos para incrementar o número de clientes atendidos 
print("\nIncrementando")
print("Número de clientes atendidos:",r1.getNumeroServidos())

r1.incrementarNumeroServidos(10)
print("Número de clientes atendidos:",r1.getNumeroServidos())






