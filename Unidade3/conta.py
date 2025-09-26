from datetime import datetime as dt
from random import randint
from usuario import Usuario

class Conta:
    def __init__(self,usuario:Usuario):
        self.agencia = randint(0,999)
        self.usuario = usuario
        self.saldo = 0
        self.data_abertura = dt.now()


    def __str__(self):
       obj_str="\n---Dados da conta---:\n"
       obj_str+=f"Agência:{self.agencia}\n"
       obj_str+=f"Data da abertura:{self.data_abertura}\n"
       obj_str+=f"Saldo da conta:{self.saldo}\n"
       obj_str+=f"Nome do usuario:{self.usuario.get_nome()}\n"
       return obj_str
        
        
usuario1=Usuario()

nome_usuario1= input("Digite seu nome: ")
cpf_usuario1= int (input("Digite seu CPF: "))
rg_usuario1= int (input("Digite seu RG: "))
dia_nascimento= int (input("Digite o dia do seu nascimento: "))
mes_nacimento= int (input("Digite o mês do seu nascimento: "))
ano_nascimento= int (input("Digite o ano do seu nascimento: "))


usuario1.set_nome(nome_usuario1)
usuario1.set_cpf(cpf_usuario1)
usuario1.set_rg(rg_usuario1)
usuario1.set_data_nascimento(ano_nascimento,mes_nacimento,dia_nascimento)


conta_usuario1 = Conta(usuario1)
print(conta_usuario1)
                f"Data de Nascimento: {self.usuario.dataNascimento.strftime('%d/%m/%Y')}")
