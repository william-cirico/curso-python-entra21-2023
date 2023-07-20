"""
Métodos mágicos

Também conhecidos como métodos especiais ou dunder methods (nome derivado do fato 
de começarem e terminarem com duplo sublinhado). Esses métodos são chamados automaticamente
pelo interpretador Python em determinadas situações.
"""
from __future__ import annotations

class Point2D:
    """Point2D representa um ponto 2D."""
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def __add__(self, other) -> Point2D:
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("operação não suportada.")
    
    def __iadd__(self, other):
        if isinstance(other, Point2D):
            self.x += other.x
            self.y += other.y
        else:
            raise TypeError("operação não suportada.")


class SumCalculator:
    """SumCalculator representa uma calculadora para soma de números."""
    def __call__(self, *args: float):
        return sum(args)
    

if __name__ == "__main__":
    calculator = SumCalculator()
    result = calculator(10, 9, 8)
    print(result)

    point1 = Point2D(2, 3)
    point2 = Point2D(4, 5)
    point3 = point1 + point2

    print(point1, point2, point3, sep="\n")

    point1 += point2

    print(point1)
