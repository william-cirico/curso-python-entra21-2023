from geometric_form import GeometricForm

class Rectangle(GeometricForm): 
    def __init__(self, side_a: float, side_b: float):
        self.side_a = side_a
        self.side_b = side_b
        
    def get_area(self) -> float:
        """Calcula a área do retângulo."""
        return self.side_a * self.side_b
    
    def get_perimeter(self) -> float:
        return 2 * (self.side_a + self.side_b)