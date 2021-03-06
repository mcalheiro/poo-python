

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f'Saldo: R$ {self.__saldo:.2f}')
    
    def deposita(self, valor):
        self.__saldo += valor
        print(f'Depositou: R$ {valor:.2f} na conta de {self.__titular}. \nNovo saldo: R${self.__saldo:.2f}')
        
    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'Sacou: R$ {valor:.2f} da conta de {self.__titular}. \nNovo saldo: R${self.__saldo:.2f}')
        else:
            print(f'Valor R$ {valor:.2f} ultrapassa o limite de R$ {self.__limite + self.__saldo:.2f}')
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        
        print(f'R$ {valor:.2f} transferido de {self.__titular} para {destino.__titular}')

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel
        
#    # getters & setters
    
#     def get_saldo(self):
#         return self.__saldo
    
#     def get_titular(self):
#         return self.__titular
    
#     def get_limite(self):
#         return self.__limite
    
#     def set_limite(self, limite):
#         self.__limite = limite
        
    # properties > getters & setters
    
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
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
        
    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
        
