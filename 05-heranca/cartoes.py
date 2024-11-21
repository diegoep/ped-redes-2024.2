from abc import ABC, abstractmethod


class CartaoMensagem(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def enviar_mensagem(self, remetente):
        pass

    @property
    def destinatario(self):
        return self.__destinatario
    
    @destinatario.setter
    def destinatario(self, destinatario):
        self.__destinatario = destinatario

class MensagemDiaDosNamorados(CartaoMensagem):
    def enviar_mensagem(self, remetente):
        return f"Querido(a) {self.destinatario}, feliz dia dos namorados! De {remetente}"
    
class MensagemNatal(CartaoMensagem):
    def enviar_mensagem(self, remetente):
        return f"Querido(a) {self.destinatario}, feliz natal! De {remetente}"
    
class MensagemAniversario(CartaoMensagem):
    def enviar_mensagem(self, remetente):
        return f"Querido(a) {self.destinatario}, feliz aniversário! De {remetente}"
    
class MensagemInformativa(CartaoMensagem):
    pass
    
if __name__ == '__main__':
    mensagem_namorados = MensagemDiaDosNamorados("João")
    mensagem_natal = MensagemNatal("João")
    mensagem_aniversario = MensagemAniversario("João")

    mensagens = [mensagem_namorados, mensagem_natal, mensagem_aniversario]
    for mensagem in mensagens:
        print(mensagem.enviar_mensagem("Maria"))

    cartao = CartaoMensagem("João")
