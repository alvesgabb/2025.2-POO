from datetime import datetime

class Usuario:
    def __init__(self, rg=0, cpf=0, nome="", dataNascimento=None):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento if dataNascimento else datetime.now()