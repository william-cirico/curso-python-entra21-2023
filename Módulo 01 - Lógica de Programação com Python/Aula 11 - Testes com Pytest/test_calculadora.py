from calculadora import somar, dividir, multiplicar, subtrair
import pytest


def test_somar():
    assert somar(1, 3) == 4


def test_dividir():
    # Arrange
    a = 4
    b = 2

    # Act
    resultado = dividir(a, b)

    # Assert
    assert resultado == 2


def test_dividir_por_zero_gera_erro():
    # Arrange
    a = 4
    b = 0

    # Act e Assert
    with pytest.raises(ZeroDivisionError):
        dividir(a, b)


def test_multiplicar():
    assert multiplicar(10, 2) == 20



def test_subtrair():
    assert subtrair(10, 2) == 8