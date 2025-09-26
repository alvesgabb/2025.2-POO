
from datetime import datetime as dt

class Usuario:
    def __init__(self,rg=None,cpf=None,nome=None,data_nascimento=dt(1900,9,1)):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    
    def get_rg(self):
        return self.rg
    def set_rg(self,novo_rg):
        self.rg = novo_rg

    def get_cpf(self):
        return self.cpf
    def set_cpf(self,novo_cpf):
        self.cpf = novo_cpf
    
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_data_nascimento(self):
        return self.data_nascimento
    def set_data_nascimento(self,ano,mes,dia):
        self.data_nascimento = dt(ano,mes,dia)



