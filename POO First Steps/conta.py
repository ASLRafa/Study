class Conta:

    def __init__(self, codigo, titular, limite=1000):

      self.__codigo = codigo
      self.__saldo = 0
      self.__titular = titular
      self.__limite = limite
      self.__codigo_banco = '001'
      
    @property
    def saldo(self):
      return self.__saldo
      
    @property
    def titular(self):
      return self.__titular
      
    @property
    def limite(self):
      return self.__limite
      
    @limite.setter
    def limite(self,novo_limite):
      self.__limite = novo_limite
  
    def extrato(self):
      print("\n-----------EXTRATO-----------\n")
      print("codigo de conta: {}\ntitular: {}\nsaldo total: {}\n".format(
          self.__codigo, self.__titular, self.__saldo))
      print("-"*30)

    def deposita(self, valor):
      self.__saldo += valor

    def saca(self, valor):
      if self.__pode_sacar(valor):
        self.__saldo -= valor
      else:
        print("Saldo Insuficiente")

    def __pode_sacar(self,valor_a_sacar):
      uso_limite = 1
      valor_com_limite = (self.__saldo + self.__limite)
      if valor_a_sacar > self.__saldo:
        print("Deseja utilizar o limite?\nDigite 1 para SIM e 2 para NÃO.")
        uso_limite = input("")
      if uso_limite == "1" and valor_a_sacar <= valor_com_limite:
        return True
      else:
        return False
  
    def transfere(self,valor,contaDestino):
      if valor >= self.__saldo:
        self.saca(valor)
        contaDestino.deposita(valor)
      else:
        print('saldo insuficiente')
        
    @staticmethod
    def codigo_banco() -> str:
      return "001"

    @staticmethod
    def codigos_bancos() -> dict:
      return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
      