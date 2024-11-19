class Pais:
    def __init__(self, nome, capital, dimensao):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.__paises_fronteira = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        assert type(nome) == str, "Nome do país deve ser uma string"
        self.__nome = nome
        
    @property
    def capital(self):
        return self.__capital
    
    @capital.setter
    def capital(self, capital):
        assert type(capital) == str, "Nome da capital deve ser uma string"
        self.__capital = capital

    @property
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao):
        assert type(dimensao) == float or type(dimensao) == int, "Dimensão deve ser int ou float"
        self.__dimensao = dimensao

    @property
    def paises_fronteira(self):
        return self.__paises_fronteira

    def adiciona_pais(self, pais):
        self.paises_fronteira.append(pais)

    def __str__(self):
        return f"Nome: {self.nome}, Capital: {self.capital}, Dimensão: {self.dimensao}, Fronteira com: {self.paises_fronteira}"

if __name__ == '__main__':
    p = Pais('Brasil', 'Brasilia', 2300203)
    p.adiciona_pais('Bolivia')
    p.adiciona_pais('Uruguai')
    p.adiciona_pais('Argentina')
    p.adiciona_pais('Colombia')
    p.adiciona_pais('Suriname')
    p.adiciona_pais('Peru')
    p.adiciona_pais('Paraguai')
    p.adiciona_pais('Guiana Francesa')
    print(p)
