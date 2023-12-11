from __future__ import annotations

class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @staticmethod
    def has_common_axis(pointA: Point2D, pointB: Point2D) -> bool:
        """Verifica se dois pontos possuem eixos em comum.
        
        Args:
            pointA (Point2D): Ponto A.
            pointB (Point2D): Ponto B.
            
        Returns:
            True caso possua um eixo em comum, False caso contrário.
        """
        return pointA.x == pointB.x or pointA.y == pointB.y    
    