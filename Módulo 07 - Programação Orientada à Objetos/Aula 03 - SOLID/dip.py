"""
D - Dependency Inversion Principle

O DIP estabelece que as classes de alto nível não devem depender das classes de 
baixo nível. Ambas devem depender de abstrações. Além disso, as abstrações não 
devem depender de detalhes, mas os detalhes devem depender de abstrações.
"""
from abc import ABC, abstractmethod

class INotificador(ABC):
    """Implementa a interface de Notificador"""
    @abstractmethod
    def enviar_notificacao(self, mensagem: str) -> None:
        """Envia uma notificação"""

class EmailNotificador(INotificador):
    """Implementa a classe concreta de EmailNotificador."""
    def enviar_notificacao(self, mensagem: str) -> None:
        print(f"Enviando a notificação '{mensagem}' via e-mail...")

class SMSNotificador(INotificador):
    """Implementa a classe concreta de SMSNotificador."""
    def enviar_notificacao(self, mensagem: str) -> None:
        print(f"Enviando a notificação '{mensagem}' via SMS...")

class WPPNotificador(INotificador):
    """Implementa a classe concreta de SMSNotificador."""
    def enviar_notificacao(self, mensagem: str) -> None:
        print(f"Enviando a notificação '{mensagem}' via WPP...")

class Aplicacao:
    """Implementa a classe de Aplicação."""
    def __init__(self, notificador: INotificador):
        self.notificador = notificador

    def enviar_mensagem(self, mensagem: str) -> None:
        """Envia uma mensagem utilizando o notificador."""
        self.notificador.enviar_notificacao(mensagem)
        
if __name__ == "__main__":
    wpp_notificador = WPPNotificador()
    aplicacao = Aplicacao(wpp_notificador)
