class Lampada:
    def __init__(self, cor, potencia, ligada=False):
        self.ligada = ligada
        self.cor = cor
        self.potencia = potencia
    
    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def alternar_ligado(self):
        self.ligada = not self.ligada

    