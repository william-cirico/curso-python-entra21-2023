from abc import ABC, abstractmethod

class GeometricForm(ABC):
    @abstractmethod
    def get_area(self) -> float:
        """Calcula a área da forma geométrica."""
        
    @abstractmethod
    def get_perimeter(self) -> float:
        """Calcula o perímetro da forma geométrica."""