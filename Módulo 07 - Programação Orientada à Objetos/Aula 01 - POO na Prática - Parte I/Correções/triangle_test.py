import pytest

from triangle import Triangle

def test_triangle_creation():
    triangle = Triangle(10, 9, 8)
    
    assert triangle.a == 10
    assert triangle.b == 9
    assert triangle.c == 8

def test_invalid_triangle_creation():
    with pytest.raises(ValueError):
        triangle = Triangle(5, 10, 4)

def test_get_type_equilateral():
    triangle = Triangle(10, 10, 10)
    
    assert triangle.get_type() == "Equilátero"
    
def test_get_type_scalene():
    triangle = Triangle(10, 9, 8)
    
    assert triangle.get_type() == "Escaleno"
    
def test_get_type_isosceles():
    triangle = Triangle(10, 10, 8)
    
    assert triangle.get_type() == "Isósceles"