"""
I - Interface Segregation Principle

Classes não devem ser forçadas a depender de interfaces que elas não utilizam.
Um exemplo prático de aplicação do ISP em Python seria dividir uma interface 
grande em interfaces menores e mais específicas. Em vez de ter uma única classe 
com uma interface abrangente, você poderia criar várias interfaces mais focadas e 
fazer com que as classes implementem apenas as interfaces relevantes para o seu 
contexto específico.
"""

from abc import ABC, abstractmethod

class IAnimal(ABC):
    """Interface de Animal."""
    @abstractmethod
    def mover(self) -> None:
        """Executa a ação de mover do animal."""

    # Violação do ISP
    @abstractmethod
    def voar(self) -> None:
        """Executa a ação de voar do animal."""


class Peixe(IAnimal):
    """Classe concreta de peixe."""
    def mover(self) -> None:
        print("O peixe nada.")
    
    def voar(self) -> None:
        print("O peixe voa.")
