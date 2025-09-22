""" 1.	Declare uma classe Usuario que contenha os atributos RG (int), CPF (int), nome (string) e dataNascimento (datetime). Deve ser implementado método construtor que possibilita a passagem de parâmetros ou, na sua ausência, valores padrão;
2.	Declare uma classe Conta com os atributos agencia (int), usuario (Usuario), dataAbertura (datetime) e saldo (float).
3.	Implemente um programa que deve:
a.	Instanciar um objeto do tipo Usuario apenas com os valores padrão),
b.	Solicitar a digitação dos dados do usuário (rg, cpf, nome e data de nascimento),
c.	Atribuir os valores dos atributos através dos métodos modificadores.
d.	Em seguida, o programa deve instanciar um objeto do tipo Conta. Porém, para isso, deve passar valores para todos os atributos (leitura prévia) no momento da instanciação.
i.	Observação: o código da agência deve ser um valor gerado aleatoriamente entre 0 e 999.
e.	Ao final, os dados da conta, incluindo os do usuário, devem ser exibidos. Para isso, devem ser utilizados os métodos de acesso.
Observação: ambas as classes devem prever mecanismo de auto referência para atribuição dos valores dos parâmetros dos métodos aos atributos da classe.
 """

from datetime import datetime
import random
from usuario import Usuario
from conta import Conta

# a) Instanciar Usuario com valores padrão
usuario = Usuario()

# b) Solicitar dados do usuário
usuario.rg = int(input("Digite o RG: "))
usuario.cpf = int(input("Digite o CPF: "))
usuario.nome = input("Digite o nome: ")
data_str = input("Digite a data de nascimento (dd/mm/aaaa): ")
usuario.dataNascimento = datetime.strptime(data_str, "%d/%m/%Y")

# d) Criar Conta com todos os atributos
agencia = random.randint(0, 999)
dataAbertura = datetime.now()
saldo = float(input("Digite o saldo inicial: "))
conta = Conta(agencia, usuario, dataAbertura, saldo)

# e) Exibir dados da conta e do usuário
print("\n===== DADOS DA CONTA =====")
print(conta)
