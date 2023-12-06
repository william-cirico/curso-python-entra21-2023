"""
L - Liskov Substitution Principle (LSP)

O Princípio de Substituição de Liskov estabelece que, em um programa, objetos de 
uma classe derivada devem ser substituíveis por objetos de sua classe base sem 
afetar a corretude do programa. Em outras palavras, uma classe derivada deve poder
ser usada no lugar de sua classe base sem causar comportamentos indesejados ou 
resultados incorretos.
"""

from abc import ABC, abstractmethod

class IForma(ABC):
    """Implementa uma interface para forma."""
    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula a área da fomra"""


class Retangulo(IForma):
    """Implementa uma classe para retângulos."""

    def __init__(self, largura: float, altura: float) -> None:
        """
        Inicialia um objeto Retângulo.

        Args:
            largura (float): A largura do retângulo.
            altura (float): A altura do retângulo.
        """
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula a área do retângulo."""
        return self.largura * self.altura


class Quadrado(IForma):
    """Implementa uma classe para quadrado."""
    
    def __init__(self, lado: float) -> None:
        """
        Inicializa um objeto Quadrado.

        Args:
            lado (float): Medida do lado do quadrado.
        """
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2
    

def exibir_area(forma: IForma):
    """Exibe a área da forma."""
    area = forma.calcular_area()
    print(f"A área da forma é {area:.2f}")

if __name__ == '__main__':
    retangulo = Retangulo(2, 2)
    quadrado = Quadrado(8)

    exibir_area(retangulo)
    exibir_area(quadrado)
