""" Crie uma classe abstrata chamada MetodoPagamento com:
Um atributo: valor (float);
Um método abstrato chamado pagar() que deverá ser implementado pelas subclasses.
Implemente três classes concretas que herdem de MetodoPagamento:
CartaoCredito: Simule pagamento com uma taxa de 5% sobre o valor;
BoletoBancario: Simule pagamento com desconto de 2% no valor;
Pix: Sem acréscimos ou descontos.
Cada classe deve implementar o método pagar() de forma diferente:
O método deve exibir o tipo de pagamento, o valor original e o valor final (após desconto ou acréscimo, se houver). """

from abc import ABC,abstractmethod

#Classe forma de pagamento
class MetodoPagamento(ABC):
    def __init__(self,valor=float):
        self.valor = valor
    
    @abstractmethod
    def pagar(self):
        pass




        
