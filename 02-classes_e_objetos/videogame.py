# marca, modelo, data de fabricação, capacidade do HD, 
# número de série, jogos instalados, anos de garantia

class Videogame:

    NUM_SERIE_ATUAL = 1

    def __init__(self, data=None, marca=None, modelo=None):
        if data is None:
            self.data = datetime.now()
        else:
            self.data = data
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 64
        self.anos_garantia = 5
        self.numero_serie = self.get_prox_num_serie()
        self.jogos_instalados = []

    def instalar_jogo(self, jogo):
        self.jogos_instalados.append(jogo)

    @classmethod
    def get_prox_num_serie(cls):
        num_serie = cls.NUM_SERIE_ATUAL
        cls.NUM_SERIE_ATUAL += 1
        return num_serie

    def __str__(self):
        return f"Data = {self.data}, Marca = {self.marca}, Modelo = {self.modelo}"


if __name__ == '__main__':

    from datetime import datetime

    v1 = Videogame()
    v1.marca = "Sony"
    v1.modelo = "Playstation 5"
    v1.data = datetime.now()
    print("V1=",v1)
    v2 = Videogame(datetime.now())
    print("V2=",v2)
    v3 = Videogame(datetime.now(), "Nintendo", "Switch")
    print("V3=",v3)

    v3.anos_garantia = 10
    v3.instalar_jogo("Counter Strike")
    print("Anos de garantia = ",v3.anos_garantia)
    print("Jogos instalados =", v3.jogos_instalados)
    print("Numero de serie de V3", v3.numero_serie)
    print(hasattr(v3, 'anos_garantia'))

    print(Videogame.__module__)


