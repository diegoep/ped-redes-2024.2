from lampada import Lampada

print(Lampada.MAX_POTENCIA)

lamp = Lampada(4000, 120)
print(lamp.cor)
print(lamp.potencia)
print(lamp.ligada)
lamp.ligada = True
lamp.potencia = 100

lamp2 = Lampada(6000, 30)
print(lamp2.cor)
print(lamp2.potencia)
print(lamp2.ligada)

print("Total de lampadas criadas =", Lampada.LAMPADAS_CRIADAS)