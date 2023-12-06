"""Implementação da classe Personagem"""
from abc import ABC # Precisamos utilizar ABC para definir uma classe abstrata
from habilidades_personagem import IHabilidadesPersonagem

class Personagem(IHabilidadesPersonagem, ABC):
    """Personagem representa um personagem no jogo.
    
    Attributes:
        nome (str): Nome do personagem.
        nivel (int): Nível do personagem.
        vida (int): Vida do personagem.
    """

    def __init__(self, nome: str, nivel: int, vida: int) -> None:
        """
        Inicializa um objeto Personagem.
    
        Args:
            nome (str): O nome do personagem.
            nivel (int): O nível do personagem.
            vida (int): A quantidade de vida do personagem.
        """
        self.nome = nome
        self.nivel = nivel
        self.vida = vida

    def atacar(self) -> None:
        """Realiza a ação de ataque do personagem."""
        print(f"{self.nome} ataca!")

    def defender(self) -> None:
        """Realiza a ação de defesa do personagem."""
        print(f"{self.nome} defende!")

    def morrer(self) -> None:
        """Realiza a ação de morte do personagem."""
        print(f"{self.nome} foi derrotado!")

    