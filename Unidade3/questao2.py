""" 1.	Crie uma classe chamada Restaurante. O construtor deve prever a passagem de valores para os atributos: nomeRestaurante e tipoCozinha. Crie um método chamado descreverRestaurante, que mostra ambas as informações, e um método abrirRestaurante, que exibe mensagem de restaurante aberto;
2.	Crie 3 (três) objetos Restaurante e execute o método descreverRestaurante para cada uma delas;
3.	Adicione o método __str__ à classe Restaurante, utilize-o ao invés de descreverRestaurante para exibir as informações da classe. """
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