"""No programa principal:
Solicite ao usuário o valor da compra e o método de pagamento desejado.
Crie a instância da classe correspondente com base na escolha do usuário.
Use uma mesma referência do tipo MetodoPagamento para armazenar o objeto instanciado e chamar o método pagar().
Questão: (responda via comentário no próprio código no arquivo main)
Como o uso de polimorfismo facilitou a implementação do sistema de pagamento? Quais seriam as vantagens de usar uma interface abstrata nesse contexto realista?"""

from cartaocredito import CartaoCredito
from boletobancario import BoletoBancario
from pix import Pix
from metodopagamento import MetodoPagamento




        
valor = float(input("Digite o valor da compra: R$"))

print("Escolha o método de pagamento:")
print("1 - Cartão de Crédito")
print("2 - Boleto Bancário")
print("3 - Pix")
opcao = input("Digite o número da opção desejada: ")

        
        
pagamento: MetodoPagamento

        
if opcao == "1":
    pagamento = CartaoCredito(valor)
elif opcao == "2":
    pagamento = BoletoBancario(valor)
elif opcao == "3":
    pagamento = Pix(valor)
else:
    print("Opção inválida.")

        
pagamento.pagar()

    
"""porque permitiu utilizar uma única variável de referência (do tipo MetodoPagamento) para lidar com diferentes tipos de pagamento (Cartão, Boleto, Pix).Isso torna o código mais flexível, limpo e fácil de manter, pois não é necessário criar estruturas separadas para cada tipo de pagamento."""
