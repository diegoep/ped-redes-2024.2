from datetime import datetime

class Professor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.__presencas = []
    
    def registrar_presenca(self, data, instituicao):
        presenca = Presenca(data, instituicao)
        self.presencas.append(presenca)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def presencas(self):
        return self.__presencas

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Presenças: {[str(p) for p in self.presencas]}"

class Presenca:
    def __init__(self, data, instituicao):
        self.data = data
        self.instituicao = instituicao

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        assert type(data) == datetime, "Data deve ser do tipo datetime"
        self.__data = data

    @property
    def instituicao(self):
        return self.__instituicao
    
    @instituicao.setter
    def instituicao(self, instituicao):
        assert type(instituicao) == Instituicao, "Instituição deve ser uma instância do tipo Instituicao"
        self.__instituicao = instituicao

    def __str__(self):
        return f"Data = {self.data}, Instituição = {self.instituicao}"

class Instituicao:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}"

p = Professor('Diego', '123123213')
ifpb = Instituicao('IFPB')
p.registrar_presenca(datetime.now(), ifpb)
p.registrar_presenca(datetime.now(), ifpb)
p.registrar_presenca(datetime.now(), ifpb)
p.registrar_presenca(datetime.now(), ifpb)
print(p)
