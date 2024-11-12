from random import shuffle

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
    
    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    PONTUACAO = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11
    }

    def __init__(self, cartas=[]):
        self.cartas = cartas

    def embaralhar(self):
        shuffle(self.cartas)

    def retirar(self):
        return self.cartas.pop()
    
    def imprimir_cartas(self):
        print("Cartas do Baralho: ")
        if self.cartas:
            print([str(carta) for carta in self.cartas])

class Jogador:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.cartas = []

    def add_carta(self, carta):
        self.cartas.append(carta)

    def calc_pontuacao(self):
        pontos = 0
        for carta in self.cartas:
            if type(carta.valor) == str:
                pontos += Baralho.PONTUACAO[carta.valor]
            else:
                pontos += carta.valor
        return pontos

class Partida:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.iniciar()
    
    def iniciar(self):
        valores = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        naipes = ['ouro', 'paus', 'espadas', 'copa']
        cartas = []
        for naipe in naipes:
            for valor in valores:
                carta = Carta(naipe, valor)
                cartas.append(carta)
        self.baralho = Baralho(cartas)
        self.baralho.embaralhar()
        self.distribuir_cartas()

    def distribuir_cartas(self):
        while self.baralho.cartas:
            for jogador in self.jogadores:
                if self.baralho.cartas:
                    jogador.add_carta(self.baralho.retirar())


    def exibir_resultado(self):
        resultados = dict()
        for jogador in self.jogadores:
            resultados[jogador.id] = jogador.calc_pontuacao()
        print(resultados)

    def exibir_ranking(self):
        resultados = dict()
        for jogador in self.jogadores:
            if jogador.calc_pontuacao() not in resultados:
                resultados[jogador.calc_pontuacao()] = [jogador.id]
            else:
                resultados[jogador.calc_pontuacao()].append(jogador.id)
        resultados = dict(sorted(resultados.items(), reverse=True))
        print(resultados)

if __name__ == '__main__':
  jogador1 = Jogador(1, 'Diego')
  jogador2 = Jogador(2, 'Gabriel')
  jogador3 = Jogador(3, 'José')
  jogador4 = Jogador(4, 'Maria')
  jogadores = [jogador1, jogador2, jogador3, jogador4]
  partida = Partida(jogadores)
  print("Resultado por jogador: ")
  partida.exibir_resultado()
  print("Ranking: ")
  partida.exibir_ranking()

