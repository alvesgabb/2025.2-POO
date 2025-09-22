from datetime import datetime

class Conta:
    def __init__(self, agencia, numero, titular, saldo=0.0):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular  # objeto Usuario
        self.saldo = saldo
        self.dataAbertura = datetime.now()

    def consultarSaldo(self):
        print(f"Saldo da conta {self.numero}: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor:.2f} para conta {conta_destino.numero} realizada!")
        else:
            print("Saldo insuficiente para transferência.")

    def __str__(self):
        return (f"Agência: {self.agencia}\n"
                f"Conta: {self.numero}\n"
                f"Saldo: R${self.saldo:.2f}\n"
                f"Titular: {self.titular.nome}")

# ================= SUBCLASSES =================

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, titular, saldo=0.0, rendimento=0.02):
        super().__init__(agencia, numero, titular, saldo)
        self.rendimento = rendimento  # 2% padrão ao mês

    def aplicarRendimento(self):
        ganho = self.saldo * self.rendimento
        self.saldo += ganho
        print(f"Rendimento aplicado: +R${ganho:.2f}")

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, titular, saldo=0.0, tarifa=10.0):
        super().__init__(agencia, numero, titular, saldo)
        self.tarifa = tarifa

    def cobrarTarifa(self):
        self.saldo -= self.tarifa
        print(f"Tarifa mensal de R${self.tarifa:.2f} cobrada.")

class ContaEspecial(ContaCorrente):
    def __init__(self, agencia, numero, titular, saldo=0.0, limite=500.0):
        super().__init__(agencia, numero, titular, saldo)
        self.limite = limite

    # Sobrescrita de métodos para considerar limite
    def consultarSaldo(self):
        print(f"Saldo: R${self.saldo:.2f} | Limite: R${self.limite:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado (usando limite se necessário)!")
        else:
            print("Saldo + limite insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor:.2f} para conta {conta_destino.numero} realizada!")
        else:
            print("Saldo + limite insuficiente.")