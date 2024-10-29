class Televisao:
    def __init__(self, canal, volume, ligada=False):
        self.canal = canal
        self.volume = volume
        self.ligada = ligada

    def sintonizar_canal(self, canal_a_sintonizar):
        self.canal = canal_a_sintonizar

    def aumentar_volume(self, nivel=1):
        self.volume += nivel

    def diminuir_volume(self, nivel=1):
        self.volume -= nivel

    def alternar_ligado(self):
        self.ligada = not self.ligada

tv1 = Televisao(5, 0)
tv1.sintonizar_canal(7)
tv1.aumentar_volume(10)
tv1.diminuir_volume()
tv1.diminuir_volume(5)
tv1.aumentar_volume()
print(tv1.volume)
