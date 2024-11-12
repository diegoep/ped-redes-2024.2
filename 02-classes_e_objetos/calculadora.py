class Calculadora:
    def __init__(self, registrador: float = 0.0):
        self.nome = "Calculadora"
        self.registrador = registrador
        self.anterior = registrador

    def __del__(self):
        print(f'Objeto com endereço de memória {hex(id(self))} deletado.')
    
    def __str__(self):
        return f"Total: {self.registrador}"

    def adicionar(self, valor: float):
        self.__guardar_anterior()
        self.registrador += valor

    def subtrair(self, valor: float):
        self.__guardar_anterior()
        self.registrador -= valor

    def dividir(self, valor: float):
        self.__guardar_anterior()
        try:
          self.registrador /= valor
        except ZeroDivisionError:
          self.registrador = 0.0
        except Exception:
          print("Erro desconhecido")
            

    def multiplicar(self, valor: float):
        self.__guardar_anterior()
        self.registrador *= valor

    def exibir(self):
        print(self.registrador)

    def resetar(self):
        self.__guardar_anterior()
        self.registrador = 0.0

    def desfazer(self):
        self.registrador, self.anterior = self.anterior, self.registrador

    def __guardar_anterior(self):
        self.anterior = self.registrador


if __name__ == '__main__':
    calculadora = Calculadora()
    operacao = None
    while True:
        print("+--------------+",
                f"|{calculadora.registrador: >13} |",
                "+--------------+",
                "(+) somar",
                "(-) subtrair",
                "(/) dividir",
                "(*) multiplicar",
                "(r) resetar",
                "(d) desfazer",
                "(exit) sair",
                "---------------",
                sep='\n')

        operacao = input("Operação: ")

        if operacao == '+':
            valor = float(input("Valor: "))
            calculadora.adicionar(valor)
            continue

        elif operacao == '-':
            valor = float(input("Valor: "))
            calculadora.subtrair(valor)
            continue

        elif operacao == '/':
            valor = float(input("Valor: "))
            calculadora.dividir(valor)
            continue

        elif operacao == '*':
            valor = float(input("Valor: "))
            calculadora.multiplicar(valor)
            continue

        elif operacao == 'r':
            calculadora.resetar()
            continue

        elif operacao == 'd':
            calculadora.desfazer()
            continue

        elif operacao == 'exit':
            break

        else:
            print('Operação inválida. Veja as opções disponíveis no menu.')

    print(calculadora.__dict__)
    print(Calculadora.__name__)
    print(Calculadora.__module__)
    print(hasattr(calculadora, 'registrador'))
    print(hasattr(calculadora, 'aaaaa'))