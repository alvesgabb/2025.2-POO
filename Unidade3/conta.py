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
       obj_str+=f"Data da abertura:{self.data_abertura.strftime("%d/%m/%Y")}\n"
       obj_str+=f"Saldo da conta:{self.saldo}\n"
       obj_str+=f"Nome do usuario:{self.usuario.get_nome()}\n"
       obj_str+=f"RG:{self.usuario.get_rg()}\n"
       obj_str+=f"CPF: {self.usuario.get_cpf()}\n"
       obj_str+=f"Data de nascimento: {self.usuario.get_data_nascimento().strftime("%d/%m/%Y")}\n"
       return obj_str
        
        
usuario1=Usuario()

nome_usuario1= input("Digite seu nome: ")
cpf_usuario1= int (input("Digite seu CPF: "))
rg_usuario1= int (input("Digite seu RG: "))
dia_nascimento= int (input("Digite o dia do seu nascimento: "))
mes_nacimento= int (input("Digite o mês do seu nascimento: "))
ano_nascimento= int (input("Digite o ano do seu nascimento:"))


usuario1.set_nome(nome_usuario1)
usuario1.set_cpf(cpf_usuario1)
usuario1.set_rg(rg_usuario1)
usuario1.set_data_nascimento(ano_nascimento,mes_nacimento,dia_nascimento)


conta_usuario1 = Conta(usuario1)
print(conta_usuario1)

