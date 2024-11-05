class Lampada:

    MAX_POTENCIA = 100
    LAMPADAS_CRIADAS = 0

    def __init__(self, cor, potencia, ligada=False):
        Lampada.incrementar_lampadas_criadas()
        self.ligada = ligada
        self.cor = cor
        if potencia < Lampada.MAX_POTENCIA:
            self.potencia = potencia
        else:
            self.potencia = 0
            print("Potência informada maior que a máxima permitida")

    @classmethod
    def incrementar_lampadas_criadas(cls):    
        cls.LAMPADAS_CRIADAS += 1

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def alternar_ligado(self):
        self.ligada = not self.ligada

    