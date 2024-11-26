class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        assert type(nome) == str, 'Nome precisa ser uma string'
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        assert type(salario) == float or type(salario) == int, 'Salário precisa ser um número'
        assert salario >= 0, 'Salário precisa ser maior ou igual a zero'
        self.__salario = salario

    def adiciona_aumento(self, valor):
        self.salario += valor

    def exibe_dados(self):
        print(f'Nome: {self.nome} - Salário: {self.salario}')

    def ganho_anual(self):
        return self.salario * 12
    
    def __str__(self):
        return f'Nome: {self.nome} - Salário: {self.salario}'
    

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula

    def exibe_dados(self):
        super().exibe_dados()
        print(f'Matrícula: {self.matricula}')

    def __str__(self):
        return f'{super().__str__()} - Matrícula: {self.matricula}'

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        assert type(matricula) == int, 'Matrícula precisa ser um número inteiro'
        self.__matricula = matricula


class AssistenteTecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.bonus = bonus

    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonus):
        assert type(bonus) == float or type(bonus) == int, 'Bônus precisa ser um número'
        assert bonus >= 0, 'Bônus precisa ser maior ou igual a zero'
        self.__bonus = bonus

    def exibe_dados(self):
        super().exibe_dados()
        print(f'Bônus: {self.bonus}')

    def ganho_anual(self):
        return super().ganho_anual() + (self.bonus * 12)
    
class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno=0):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, turno):
        assert type(turno) == str, 'Turno precisa ser uma string'
        assert turno in ['diurno', 'noturno'], 'Turno precisa ser diurno ou noturno'
        self.__turno = turno

    @property
    def adicional_noturno(self):
        return self.__adicional_noturno
    
    @adicional_noturno.setter
    def adicional_noturno(self, adicional_noturno):
        assert type(adicional_noturno) == float or type(adicional_noturno) == int, 'Adicional noturno precisa ser um número'
        assert adicional_noturno >= 0, 'Adicional noturno precisa ser maior ou igual a zero'
        self.__adicional_noturno = adicional_noturno

    def exibe_dados(self):
        super().exibe_dados()
        print(f'Turno: {self.turno} - Adicional noturno: {self.adicional_noturno}')

    def ganho_anual(self):
        return super().ganho_anual() + (self.adicional_noturno * 12)

a = AssistenteTecnico('José', 3432, 1234, 100)
print(a.ganho_anual())
a.exibe_dados()

b = AssistenteAdministrativo('Maria', 3432, 1234, 'noturno', 500)
print("Ganho anual = ", b.ganho_anual())
b.exibe_dados()
