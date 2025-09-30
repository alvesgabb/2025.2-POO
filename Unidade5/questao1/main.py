""" Questão 1
No programa principal:
Crie uma instância de cada uma das três subclasses (DiaDosNamorados, Natal, Aniversario);
Atribua cada uma delas, em momentos distintos, à mesma variável de referência;
Utilize essa referência para invocar o método showMessage.
Questão: (responda via comentário no próprio código no arquivo main)
Explique como ocorre o polimorfismo neste código. """

from cartaoweb import CartaoWeb
from diadosnamorados import DiaDosNamorados 
from natal import Natal
from aniversario import Aniversario
cartao:CartaoWeb

#Dia dos namorados
cartao=DiaDosNamorados("Gabriele")
print("\nData comemorativa: Dia dos namorados")
cartao.showMessage()

#Natal
cartao=Natal("Gabriele")
print("Data comemorativa: Natal")
cartao.showMessage()

#Aniversario
cartao=Aniversario("Gabriele")
print("Data comemorativa: Anivérsario")
cartao.showMessage()

#O polimorfimsmo aconteceu no momento em que você usei a mesma variável de referência (do tipo CartaoWeb) para chamar o método showMessage() em diferentes instâncias de subclasses.
