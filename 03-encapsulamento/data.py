class Data:
    __DATA_COUNTER = 0
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        Data.__DATA_COUNTER += 1

    @classmethod
    def get_data_counter(cls):
        return cls.__DATA_COUNTER
    
    @staticmethod
    def valida_dia(dia):
        return type(dia) == int and 0 < dia <= 31

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        assert Data.valida_dia(dia), "O dia deve ser um valor inteiro entre 1 e 31"
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        assert type(mes) == int and 0 < mes <= 12, "O mês deve ser um valor inteiro entre 1 e 12"
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        assert type(ano) == int and 1900 < ano <= 2100, "O mês deve ser um valor inteiro entre 1900 e 2100"
        self.__ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

d1 = Data(1, 8, 1990)
d2 = Data(12, 7, 1990)
d3 = Data(1, 12, 1990)
print(d3.get_data_counter())

print(Data.valida_dia())
