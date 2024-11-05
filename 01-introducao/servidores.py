from abc import ABC, abstractmethod


class Servidor(ABC):
    def __init__(self, nome, matricula, email, salario):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.salario = salario

    @abstractmethod
    def get_cargo(self):
        pass

class Professor(Servidor):
    def __init__(self, nome, matricula, email, salario, lattes):
        super().__init__(nome, matricula, email, salario)
        self.lattes = lattes
    
    def get_cargo(self):
        return "Professor"
    
class Tecnico(Servidor):
    def __init__(self, nome, matricula, email, salario, ch):
        super().__init__(nome, matricula, email, salario)
        self.ch = ch
    
    def get_cargo(self):
        return "Técnico Administrativo"

class Terceirizado(Tecnico):
     def __init__(self, nome, matricula, email, salario, ch, empresa):
        super().__init__(nome, matricula, email, salario, ch)
        self.empresa = empresa

     def get_cargo(self):
         return "Terceirizado"

if __name__ == '__main__':

    prof = Professor("Diego", "312123123", "diego@ifpb", 232223, 'lattes.com/diego')
    tecnico = Tecnico("Maria", "3222322", "email2@email.com", 3208322, 30)
    terceirizado = Terceirizado("José", "13232", "email@email.com", 323232, 30, 'Empresa')

    funcionarios = [prof, tecnico, terceirizado]

    soma = 0
    for funcionario in funcionarios:
        print(funcionario.nome)
        soma += funcionario.salario

    print("Total gasto com salários =", soma)