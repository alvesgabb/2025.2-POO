from metodopagamento import MetodoPagamento

#Forma de pagamento no Pix
class Pix(MetodoPagamento):
    def pagar(self):
        print(f"Pagamento via Pix")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Valor final: R${self.valor:.2f} (sem acréscimos ou descontos)")
        print("\n------------------\n")