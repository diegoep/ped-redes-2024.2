class Carro:
    def __init__(self, cor, marca='Mobi'):
        self.cor = cor
        self.marca = marca

    def __str__(self):
        return f"Carro da marca {self.marca} e da cor {self.cor}"

car1 = Carro('Branca')
car2 = Carro('Preta', 'Corolla')

print(car1)
print(car2)