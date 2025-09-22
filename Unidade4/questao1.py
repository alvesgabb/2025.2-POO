""" 1.	Com base na atividade 1 da unidade 3, adicione os métodos consultarSaldo, depositar, sacar e transferir na classe Conta;
2.	Adicione as classes ContaPoupanca (filha de Conta), ContaCorrente (filha de Conta) e ContaEspecial (filha de ContaCorrente). Você deve identificar e adicionar demais atributos e métodos relevantes ao problema. Exemplo: saldo;
3.	Sobrescreva os métodos consultarSaldo, sacar e transferir na classe ContaEspecial, para refletir a condição de que este tipo de classe possui um limite (cheque especial);
4.	Identifique outros métodos necessários (específicos) ao perfil de cada classe. Instancie objetos e execute os novos métodos adicionados às novas classes. Exiba suas informações atualizadas.

 """

from usuario import Usuario
from conta import Conta, ContaPoupanca, ContaCorrente, ContaEspecial
import random

# Criar usuários
u1 = Usuario(123456, 11122233344, "Gabrielly")
u2 = Usuario(654321, 55566677788, "Lucas")
u3 = Usuario(111222, 99988877766, "Marcos")

# Criar contas
poup = ContaPoupanca(random.randint(0,999), 1001, u1, 1000)
corr = ContaCorrente(random.randint(0,999), 1002, u2, 500)
esp = ContaEspecial(random.randint(0,999), 1003, u3, 200)

# Operações
print("\n=== Consulta de saldos iniciais ===")
poup.consultarSaldo()
corr.consultarSaldo()
esp.consultarSaldo()

print("\n=== Operações Conta Poupança ===")
poup.aplicarRendimento()
poup.consultarSaldo()

print("\n=== Operações Conta Corrente ===")
corr.depositar(200)
corr.cobrarTarifa()
corr.consultarSaldo()

print("\n=== Operações Conta Especial ===")
esp.sacar(600)          # usa limite
esp.transferir(50, corr)  # transfere usando limite
esp.consultarSaldo()

print("\n=== Saldos finais ===")
print(poup)
print(corr)
print(esp)
