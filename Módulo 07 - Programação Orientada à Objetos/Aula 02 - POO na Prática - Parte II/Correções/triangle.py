from geometric_form import GeometricForm
from math import sqrt

class Triangle(GeometricForm):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if not self.__is_triangle(side_a, side_b, side_c):
            raise AttributeError("Triângulo não é válido.")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    def __is_triangle(self, side_a: float, side_b: float, side_c: float) -> bool:
        """Verifica se o triângulo é válido.
        
        Args:
            side_a (float): Lado A do triângulo.
            side_b (float): Lado B do triângulo.
            side_c (float): Lado C do triângulo.
        """
        return (side_a + side_b) > side_c and (side_a + side_c) >side_b and (side_b + side_c) > side_a
    
    def get_area(self) -> float:
        """Retorna a área do triângulo."""
        semiperimeter = (self.side_a + self.side_b + self.side_c) / 2
        
        return sqrt(semiperimeter * (semiperimeter - self.side_a) * (semiperimeter - self.side_b) * (semiperimeter - self.side_c))
    
    def get_perimeter(self) -> float:
        """Retorna o perímetro do triângulo"""
        return self.side_a + self.side_b + self.side_c