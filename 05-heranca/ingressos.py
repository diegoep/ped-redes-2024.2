class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def calcula_valor(self):
        return self.__valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        assert type(valor) == float or type(valor) == int, "Valor deve ser numérico"
        self.__valor = valor

class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def calcula_valor(self):
        return self.valor + self.adicional

    @property
    def adicional(self):
        return self.__adicional
    
    @adicional.setter
    def adicional(self, adicional):
        assert type(adicional) == float or type(adicional) == int, "Adicional deve ser numérico"
        self.__adicional = adicional

if __name__ == '__main__':
    ingresso = Ingresso(100)
    print(f"Valor do ingresso: {ingresso.calcula_valor()}")

    ingresso_vip = IngressoVIP(100, 50)
    print(f"Valor do ingresso VIP: {ingresso_vip.calcula_valor()}")