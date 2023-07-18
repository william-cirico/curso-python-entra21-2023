"""
O - Open-Closed Principle

O Princípio Aberto-Fechado estabelece que as entidades de software (classes, módulos, funções etc.)
devem ser abertas para extensão, mas fechadas para modificação. Isso significa que você deve poder 
estender o comportamento de uma entidade sem precisar modificar seu código-fonte original.
"""
import math

class Calculadora:
    """Implementa uma calculadora básica"""

    @classmethod
    def calcular(cls, operando1, operador, operando2) -> float:
        """Realiza uma operação matemática básica.
        
        Args:
            operando1 (float): O primeiro operando.
            operador (str): O operador ("-", "-", "*", "/").
            operando2 (float): O segundo operando.

        Returns:
            float: O resultado da operação.

        Raises:
            ValueError: Se o operador for inválido.
        """
        match (operador):
            case "+":
                return operando1 + operando2
            case "-":
                return operando1 - operando2
            case "*":
                return operando1 * operando2
            case "/":
                return operando1 / operando2
            case _:
                raise ValueError("operador inválido")


class CalculadoraLogaritmo(Calculadora):
    """Implementa uma calculadora de logaritmo."""

    @classmethod
    def calcular(cls, operando1, operador, operando2) -> float:
        """
        Realiza uma operação matemática de logaritmo.

        Args:
            operando1 (float): O operando do logaritmo.
            operando2 (float): A base do logaritmo.
            operador (str): O operador ('log').

        Returns:
            float: O resultado do cálculo de logaritmo.

        Raises:
            ValueError: Se o operador for inválido.
        """
        if operador == "log":
            return math.log(operando1, operando2)
        else:
            return super().calcular(operando1, operador, operando2)


if __name__ == "__main__":
    print(Calculadora.calcular(10, "*", 5))
    print(CalculadoraLogaritmo.calcular(100, "log", 10))
