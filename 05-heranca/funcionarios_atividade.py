from abc import ABC, abstractmethod
from enum import Enum

class FuncionarioException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class GrauInstrucao(Enum):
    GRADUADO = 'GRADUADO'
    ESPECIALISTA = 'ESPECIALISTA'
    MESTRE = 'MESTRE'
    DOUTOR = 'DOUTOR'

class Funcionario(ABC):
    def __init__(self, nome, salario, grau_instrucao=GrauInstrucao.GRADUADO):
        self.nome = nome
        self.salario = salario
        self.grau_instrucao = grau_instrucao

    def contracheque(self):
        return self.salario + self.add_bonificacao()
    
    @abstractmethod
    def add_bonificacao(self):
        pass

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        assert isinstance(nome, str), "Nome deve ser uma string"
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        assert isinstance(salario, (int, float)), "Salário deve ser um número"
        if salario < 0:
            raise FuncionarioException("Salário não pode ser negativo")
        self.__salario = salario

    @property
    def grau_instrucao(self):
        return self.__grau_instrucao
    
    @grau_instrucao.setter
    def grau_instrucao(self, grau_instrucao):
        assert isinstance(grau_instrucao, GrauInstrucao), "Grau de instrução deve ser um GrauInstrucao"
        self.__grau_instrucao = grau_instrucao

    def __str__(self):
        return f"{self.nome} - {self.salario} - {self.grau_instrucao}"

class Gerente(Funcionario):
    def add_bonificacao(self):
        if self.grau_instrucao == GrauInstrucao.ESPECIALISTA:
            return self.salario * 0.15
        elif self.grau_instrucao == GrauInstrucao.MESTRE:
            return self.salario * 0.25
        elif self.grau_instrucao == GrauInstrucao.DOUTOR:
            return self.salario * 0.50

class Diretor(Gerente):
    def add_bonificacao(self):
        return super().add_bonificacao() + (self.salario * 0.30)

class Presidente(Funcionario):
    def add_bonificacao(self):
        if self.grau_instrucao == GrauInstrucao.DOUTOR:
            return self.salario * 4
        else:
            return self.salario * 2


try:
    g = Gerente('João', 5000, GrauInstrucao.MESTRE)
    d = Diretor('Maria', 10000, GrauInstrucao.DOUTOR)
    p = Presidente('José', 20000, GrauInstrucao.DOUTOR)

    funcionarios = [g, d, p]
    for f in funcionarios:
        print(f)
        print(f.contracheque())
        print()
except AssertionError as e:
    print(e)
except FuncionarioException as e:
    print(e)
except Exception as e:
    print(f"Erro desconhecido: {e}")
finally:
    print("Fim do programa")