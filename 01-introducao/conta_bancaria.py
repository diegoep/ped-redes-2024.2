class ContaBancaria:
    def __init__(self, agencia, conta, saldo_inicial=0):
        self.__saldo = saldo_inicial
        self.agencia = agencia
        self.conta = conta
    
    def depositar(self, valor):
        if (type(valor) == int or type(valor) == float) and valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido informado para depósito")

    def sacar(self, valor):
        if (type(valor) == int or type(valor) == float) and valor > 0:
            self.__saldo -= valor
        else:
            print("Valor inválido informado para saque")

    def exibir_saldo(self):
        return f"R$ {self.__saldo:.2f}"

c1 = ContaBancaria('1234-5', '54321-0')
print(c1.agencia)
print(c1.conta)
c1.depositar(100)
print(c1.exibir_saldo())