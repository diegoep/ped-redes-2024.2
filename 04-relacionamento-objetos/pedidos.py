class Pedido:
    def __init__(self, itens=[]):
        self.__itens = itens

    @property
    def itens(self):
        return self.__itens
    
    def adicionar_item(self, item):
        assert type(item) == ItemPedido, "Item deve ser do tipo ItemPedido"
        self.__itens.append(item)

    def remover_item(self, item):
        assert type(item) == ItemPedido, "Item deve ser do tipo ItemPedido"
        self.__itens.remove(item)
    
    def obter_total(self):
        total = 0
        for item in self.__itens:
            total += item.qtd * item.produto.valor
        return total


class ItemPedido:
    def __init__(self, qtd, produto):
        self.qtd = qtd
        self.produto = produto

    @property
    def qtd(self):
        return self.__qtd
    
    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto):
        assert type(produto) == Produto, "Produto deve ser instância da classe Produto"
        self.__produto = produto

class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        assert type(valor) == float or type(valor) == int, "Valor deve ser numérico"
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

if __name__ == '__main__':
    produto = Produto(1, 10.0, "Produto 1")
    produto2 = Produto(2, 20.0, "Produto 2")
    produto3 = Produto(3, 30.0, "Produto 3")
    item = ItemPedido(2, produto)
    item2 = ItemPedido(3, produto2)
    item3 = ItemPedido(4, produto3)
    pedido = Pedido()
    pedido.adicionar_item(item)
    pedido.adicionar_item(item2)
    pedido.adicionar_item(item3)
    print("Total do Pedido =", pedido.obter_total())