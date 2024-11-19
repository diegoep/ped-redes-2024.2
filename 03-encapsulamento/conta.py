from random import random

class ContaCorrente:
    def __init__(self, numero, saldo, titular):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular

    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    def depositar(self, valor):
        assert (type(valor) == int or type(valor) == float) and valor >= 5, "valor a depositar deve ser um número a partir de cinco reais"
        self.__saldo += valor
    
    def sacar(self, valor):
        assert (type(valor) == int or type(valor) == float) and valor > 0, "valor a depositar deve ser um número maior que zero"
        if self.saldo >= valor:
            self.__saldo -= valor
            return True
        return False
    
    def __str__(self):
        return f"Numero da conta: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}"
    
if __name__ == '__main__':
    contas = dict()
    for i in range(1, 10):
        conta = ContaCorrente(i, 0, 'Diego')
        valor_deposito = random()*1000
        print("Depositando",valor_deposito)
        conta.depositar(valor_deposito)
        valor_saque = random()*1000
        if conta.sacar(valor_saque):
            print('Conseguiu sacar',valor_saque)
        else:
            print('Não conseguiu sacar', valor_saque)
        print(conta)
        contas[conta.numero] = conta

    while True:
        print("Bem-vindo ao Banco IFPB")
        numero_conta = int(input("Digite o número da conta que deseja acessar: "))
        conta = contas[numero_conta]
        if not conta:
            print("Conta inválida. Tente novamente")
        else: 
            break

    while True:
        try:
            print("1- Depositar")
            print("2- Sacar")
            print("3- Exibir Saldo")
            print("4- Sair")
            operacao = input("Digite a operação a ser feita nessa conta: ")
            if operacao == '1':
                valor = float(input('Digite o valor a ser depositado'))
                conta.depositar(valor)
                print("Novo saldo =", conta.saldo)
            elif operacao == '2':
                valor = float(input('Digite o valor a ser sacado'))
                if conta.sacar(valor):
                    print("Saque realizado com sucesso!")
                    print("Novo saldo =", conta.saldo)
                else:
                    print("Saldo insuficiente")
            elif operacao == '3':
                print("saldo =", conta.saldo)
            elif operacao == '4':
                break
            else:
                print("Operação inválida")
        except Exception as e:
            print(e)