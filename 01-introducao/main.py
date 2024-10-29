from lampada import Lampada

lamp = Lampada(4000, 50)
print(lamp.cor)
print(lamp.potencia)
print(lamp.ligada)
lamp.ligada = True
lamp.potencia = 100

lamp2 = Lampada(6000, 30)
print(lamp2.cor)
print(lamp2.potencia)
print(lamp2.ligada)