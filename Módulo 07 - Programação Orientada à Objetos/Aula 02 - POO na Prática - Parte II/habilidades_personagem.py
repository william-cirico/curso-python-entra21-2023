"""Implementação da interface HabilidadesPersonagem"""
from abc import ABC, abstractmethod

class IHabilidadesPersonagem(ABC):
    """
    HabilidadesPersonagem é uma interface que define habilidades que todo
    personagem deve ter.
    """

    @abstractmethod
    def atacar(self) -> None:
        """Realiza a ação de ataque do personagem."""

    @abstractmethod
    def defender(self) -> None:
        """Realiza a ação de defesa do personagem."""

    @abstractmethod
    def morrer(self) -> None:
        """Realiza a ação de morrer do personagem."""

    @abstractmethod
    def usar_habilidade_especial(self) -> None:
        """Utiliza a habilidade especial do personagem."""
