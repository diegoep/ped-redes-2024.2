from abc import ABC, abstractmethod


class Autenticavel(ABC):

    @abstractmethod
    def autentica(self, login, senha):
        pass


class Aluno:
    def __init__(self, nome, matricula, login, senha):
        self.nome = nome
        self.matricula = matricula
        self.login = login
        self.senha = senha

    def autentica(self, login, senha):
        return self.login == login and self.senha == senha
    

Autenticavel.register(Aluno)
print(isinstance(Aluno('João', 123, 'joao', '1234'), Autenticavel))  # True
print(issubclass(Aluno, Autenticavel))  # True