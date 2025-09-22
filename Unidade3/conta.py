from datetime import datetime

class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self.agencia = agencia
        self.usuario = usuario  # associação com objeto Usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def __str__(self):
        return (f"Agência: {self.agencia}\n"
                f"Data de Abertura: {self.dataAbertura.strftime('%d/%m/%Y %H:%M')}\n"
                f"Saldo: R${self.saldo:.2f}\n"
                f"--- Dados do Usuário ---\n"
                f"Nome: {self.usuario.nome}\n"
                f"RG: {self.usuario.rg}\n"
                f"CPF: {self.usuario.cpf}\n"
                f"Data de Nascimento: {self.usuario.dataNascimento.strftime('%d/%m/%Y')}")