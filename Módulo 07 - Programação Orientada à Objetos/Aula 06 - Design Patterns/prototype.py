"""
Prototype - Padrão Criacional

Permite a criação de objetos duplicados (protótipos) através da clonagem de um objeto existente. 
O padrão Prototype é útil quando a criação de um objeto é complexa e custosa em termos de recursos. 
Em vez de repetir o processo de criação do objeto toda vez que for necessário, podemos criar um protótipo 
inicial e cloná-lo sempre que for necessário um objeto similar.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import copy

class Protoype(ABC):
    """Interface que define um prototype."""
    @abstractmethod
    def clone(self):
        """Método responsável por clonar o objeto."""

class Inimigo(Protoype):
    """Classe do inimigo"""
    def __init__(self, nome, vida, pontos_ataque) -> None:
        self.nome = nome
        self.vida = vida
        self.pontos_ataque = pontos_ataque

    def clone(self) -> Inimigo:
        return copy.deepcopy(self)
    
    def mostrar_info(self):
        """Mostra as informações do inimigo."""
        print(f"Nome: {self.nome}\nVida: {self.vida}\nPontos de ataque: {self.pontos_ataque}\n{'-'*20}")

if __name__ == "__main__":
    goblin_prototype = Inimigo("Goblin", 100, 10)
    orc_prototype = Inimigo("Orc", 150, 15)

    goblin1 = goblin_prototype.clone()
    goblin2 = goblin_prototype.clone()
    orc1 = orc_prototype.clone()

    goblin1.vida = 80
    orc1.pontos_ataque = 20

    goblin1.mostrar_info()
    goblin2.mostrar_info()
    orc1.mostrar_info()