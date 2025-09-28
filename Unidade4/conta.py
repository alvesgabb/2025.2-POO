""" 1.	Com base na atividade 1 da unidade 3, adicione os métodos consultarSaldo, depositar, sacar e transferir na classe Conta;
2.	Adicione as classes ContaPoupanca (filha de Conta), ContaCorrente (filha de Conta) e ContaEspecial (filha de ContaCorrente). Você deve identificar e adicionar demais atributos e métodos relevantes ao problema. Exemplo: saldo;
3.	Sobrescreva os métodos consultarSaldo, sacar e transferir na classe ContaEspecial, para refletir a condição de que este tipo de classe possui um limite (cheque especial);
4.	Identifique outros métodos necessários (específicos) ao perfil de cada classe. Instancie objetos e execute os novos métodos adicionados às novas classes. Exiba suas informações atualizadas. """

from datetime import datetime as dt
from random import randint
from usuario import Usuario

class Conta:
    def __init__(self,usuario:Usuario):
        self.agencia = randint(0,999)
        self.usuario = usuario
        self.saldo = 0
        self.data_abertura = dt.now()

    def consultar_saldo(self):
        print(f"Saldo da conta: R${self.saldo}")

    def depositar(self,valor_deposito):
        self.saldo+=valor_deposito
        print(f"O depósito de R${self.saldo} foi realizado com sucesso!\n")
    
    def sacar(self,valor_saque):
        if valor_saque>self.saldo:
            print("Transação não realizada por saldo insuficiente")
        else:
         self.saldo-=valor_saque
         print(f"Saque de {valor_saque} realizado com sucesso!")

    def transferir(self,valor_trasferencia):
        if valor_trasferencia>self.saldo:
            print("Transfêrencia não realizada por saldo insuficiente.")
        else:
            self.saldo-=valor_trasferencia
            print(f"Transfêrencia de {valor_trasferencia} realizada com sucesso!")

    def __str__(self):
       obj_str="\n---Dados da conta---:\n"
       obj_str+=f"Agência:{self.agencia}\n"
       obj_str+=f"Data da abertura:{self.data_abertura.strftime("%d/%m/%Y")}\n"
       obj_str+=f"Saldo da conta:{self.saldo}\n"
       obj_str+=f"Nome do usuario:{self.usuario.get_nome()}\n"
       obj_str+=f"RG:{self.usuario.get_rg()}\n"
       obj_str+=f"CPF: {self.usuario.get_cpf()}\n"
       obj_str+=f"Data de nascimento: {self.usuario.get_data_nascimento().strftime("%d/%m/%Y")}\n"
       return obj_str
    
class ContaPoupanca(Conta):

    def __str__(self):
       obj_str="\n---Dados da conta poupança---:\n"
       obj_str+=f"Agência:{self.agencia}\n"
       obj_str+=f"Data da abertura:{self.data_abertura.strftime("%d/%m/%Y")}\n"
       obj_str+=f"Saldo da conta:{self.saldo}\n"
       obj_str+=f"Nome do usuario:{self.usuario.get_nome()}\n"
       obj_str+=f"RG:{self.usuario.get_rg()}\n"
       obj_str+=f"CPF: {self.usuario.get_cpf()}\n"
       obj_str+=f"Data de nascimento: {self.usuario.get_data_nascimento().strftime("%d/%m/%Y")}\n"
       return obj_str


class ContaCorrente(Conta):
    pass

        
class ContaEspecial(ContaCorrente):
    def __init__(self, usuario,saldo_especial=0):
        super().__init__(usuario)
        self.saldo_especial=saldo_especial

    def sacar(self,valor_saque):
        if valor_saque>self.saldo+self.saldo_especial:
            print("Transação não realizada por saldo insuficiente")
        else:
         self.saldo-=valor_saque
         print(f"Saque de {valor_saque} realizado com sucesso!")
    
        
usuario1=Usuario()

""" nome_usuario1= input("Digite seu nome: ")
cpf_usuario1= int (input("Digite seu CPF: "))
rg_usuario1= int (input("Digite seu RG: "))
dia_nascimento= int (input("Digite o dia do seu nascimento: "))
mes_nacimento= int (input("Digite o mês do seu nascimento: "))
ano_nascimento= int (input("Digite o ano do seu nascimento:")) """

usuario1.set_nome("Gabriele Alves")
usuario1.set_cpf("474656")
usuario1.set_rg("374857")
usuario1.set_data_nascimento(22,3,2007)

conta_usuario1 = Conta (usuario1)
print(conta_usuario1)
