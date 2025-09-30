from metodopagamento import MetodoPagamento

#Forma de pagamento: Boleto Bancário

class BoletoBancario(MetodoPagamento):
    def pagar(self):
        desconto = self.valor * 0.02
        valor_final = self.valor - desconto
        print(f"Pagamento via Boleto Bancário")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Desconto de 2%: R${desconto:.2f}")
        print(f"Valor final: R${valor_final:.2f}")
        print("\n------------------\n")
