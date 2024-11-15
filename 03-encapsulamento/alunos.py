class Aluno:
    def __init__(self, matricula, nome, notas=[]):
        self.__matricula = matricula
        self.nome = nome
        self.__notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    @property
    def matricula(self):
        return f"mat:{self.__matricula}"
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def notas(self):
        return self.__notas
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
aluno = Aluno(123123, 'José', [10, 8, 7])
aluno.adicionar_nota(0)
print(aluno.media())
print(aluno.matricula)