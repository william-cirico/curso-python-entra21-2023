from geometric_form import GeometricForm
from math import pi

class Circle(GeometricForm):
    """Circle representa um círculo.
    
    Args:
        radius (float): Raio do círculo.
    """
    
    def __init__(self, radius: float):
        self.radius = radius
        
    def get_area(self) -> float:
        """Retorna a área do círculo."""
        return pi * self.radius ** 2
        
    def get_perimeter(self) -> float:
        """Retorna o perímetro do círculo."""
        return 2 * pi * self.radius