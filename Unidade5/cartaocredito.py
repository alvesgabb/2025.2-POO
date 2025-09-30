from metodopagamento import MetodoPagamento


#Forma de pagamento: Cartão de Crédito
class CartaoCredito(MetodoPagamento):
    def pagar(self):
        taxa = self.valor * 0.05
        valor_final = self.valor + taxa
        print(f"Pagamento via Cartão de Crédito")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Taxa de 5%: R${taxa:.2f}")
        print(f"Valor final: R${valor_final:.2f}")
        print("\n------------------\n")
