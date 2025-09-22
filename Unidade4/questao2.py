""" 1.	A partir da atividade 2 da unidade 3, acrescente o atributo numeroServidos, cujo valor padrão é 0 (zero). Crie uma instância chamada restaurante, apresente o número de clientes atendidos e, em seguida, mude o valor e exiba-o novamente;
2.	Adicione os métodos getNumeroServidos e setNumeroServidos, para alterar o valor de clientes atendidos. Execute-o com um novo valor de clientes atendidos e, em seguida, apresente o valor novamente;
3.	Acrescente o método incrementeNumeroServidos que permita incrementar o número de clientes servidos, através de um parâmetro passado. Em sua implementação, invoque os métodos getNumeroServidos e setNumeroServidos para incrementar o número de clientes atendidos. """

from metodos2 import Restaurante

# Criar instância
restaurante = Restaurante("Sabores do Brasil", "Comida Regional")

# Mostrar número de clientes atendidos (padrão 0)
print("Clientes atendidos inicialmente:", restaurante.getNumeroServidos())

# Mudar o valor usando set
restaurante.setNumeroServidos(20)
print("Clientes atendidos após alteração:", restaurante.getNumeroServidos())

# Incrementar clientes atendidos
restaurante.incrementeNumeroServidos(15)
print("Clientes atendidos após incremento:", restaurante.getNumeroServidos())

# Exibir resumo final usando __str__
print("\nResumo final:")
print(restaurante)