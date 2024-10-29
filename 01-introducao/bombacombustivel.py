from datetime import datetime


class BombaDeCombustivel:
    def __init__(self, numero):
        self.numero = numero
        self.abastecimentos = []
        self.combustiveis = []

    ## todo - como calcular a quantidade de litros por valor ou valor por litros automaticamente
    def registrar_abastecimento(self, abastecimento):
        self.abastecimentos.append(abastecimento)

    ## todo - como calcular o valor por período?
    def calcular_valor_acumulado(self):
        soma_total = 0
        for abastecimento in self.abastecimentos:
            soma_total += abastecimento.valor
        return soma_total

class Combustivel:
    def __init__(self, tipo, valor, litros_disponiveis):
        self.tipo = tipo
        self.valor = valor
        self.litros_disponiveis = litros_disponiveis

class Abastecimento:
    def __init__(self, datahora, litros, tipo, valor, cliente):
        self.datahora = datahora
        self.litros = litros
        self.tipo = tipo
        self.valor = valor
        self.cliente = cliente

bomba1 = BombaDeCombustivel(1)
gasolina_bomba1 = Combustivel('gasolina', 6.20, 500)
etanol_bomba1 = Combustivel('etanol', 4.80, 400)
bomba1.combustiveis.append(gasolina_bomba1)
bomba1.combustiveis.append(etanol_bomba1)

abastecimento1 = Abastecimento(datetime.now(), 30, 'gasolina', 200)
bomba1.registrar_abastecimento(abastecimento1)