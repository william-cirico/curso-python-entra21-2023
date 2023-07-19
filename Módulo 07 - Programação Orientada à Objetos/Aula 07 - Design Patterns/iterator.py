"""
Iterator - Padrão Comportamental

O padrão Iterator é útil quando você precisa percorrer uma coleção de elementos 
sem se preocupar com a estrutura subjacente da coleção.
"""
from collections.abc import Iterator, Iterable
from typing import List

class NumerosIterator(Iterator):
    """Iterator da classe Numeros."""
    def __init__(self, numeros: List[float]) -> None:
        self.numeros = numeros
        self.indice = 0

    def __next__(self) -> float:
        if self.indice < len(self.numeros):
            numero = self.numeros[self.indice]
            self.indice += 1
            return numero
        else:
            raise StopIteration

class Numeros(Iterable):
    """Iterable Números."""
    def __init__(self, *args) -> None:
        self.numeros = list(args)

    def __iter__(self):
        return NumerosIterator(self.numeros)


if __name__ == "__main__":
    lista_numeros = Numeros(1, 2, 3, 4, 5)
    for n in lista_numeros:
        print(n)
