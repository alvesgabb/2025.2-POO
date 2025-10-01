""" Crie uma classe chamada Veiculo que represente um veículo da locadora. Ela deverá conter:
Atributos:
__placa → (privado, string) – placa do veículo.
modelo → (público, string) – modelo do veículo.
diaria → (público, float) – valor da diária para aluguel.
__alugado → (privado, boolean) – indica se o veículo está alugado ou não.
total_veiculos → (atributo de classe, int) – conta quantos veículos foram criados no sistema.
Métodos de instância:
__init__(self, placa, modelo, diaria) → Construtor para inicializar os atributos.
alugar(self) → Marca o veículo como alugado (caso esteja disponível).
devolver(self) → Marca o veículo como disponível (caso esteja alugado).
status(self) → Exibe o status atual do veículo (alugado ou disponível).
encapsulamento com @property:
Crie uma propriedade chamada placa que permita apenas leitura da placa.
Implemente um setter para placa que não permita alteração e exiba uma mensagem dizendo que a placa não pode ser modificada.
Método de classe:
mostrar_total_veiculos(cls) → Deve exibir o número total de veículos cadastrados.
Use o decorador @classmethod.
Método estático:
calcular_preco_aluguel(dias, diaria) → Recebe dois argumentos e retorna o valor total do aluguel.
Use o decorador @staticmethod."""

class Veiculo:
    total_veiculos = 0  

    def __init__(self, placa, modelo, diaria, alugado=False):
        self.__placa = placa           
        self.modelo = modelo           
        self.diaria = diaria           
        self.__alugado = alugado       
        Veiculo.total_veiculos += 1  

    def alugar(self):
      if not self.__alugado:
        self.__alugado = True
        print(f"Status do veículo: {self.modelo} alugado com sucesso.")
      else:
        print(f"Status do veículo: {self.modelo}, palca:{self.placa} já está alugado.")

    def devolver(self):
      if self.__alugado:
        self.__alugado = False
        print(f"Veículo {self.modelo} devolvido com sucesso.")
      else:
        print(f"Este {self.modelo}  já está disponível.")

    def status(self):
      if self.__alugado:
        print(f"Esse {self.modelo} não está disponível.")
      else:
        print(f"Esse {self.modelo} está disponível para ser alugado.")

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, novo_valor):
        print("A placa não pode ser modificada.")

    @classmethod
    def mostrar_total_veiculos(cls):
       print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
       return dias*diaria
    




