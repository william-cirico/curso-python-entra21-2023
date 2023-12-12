import pytest

from rectangle import Rectangle

def test_rectangle_creation():
    rectangle = Rectangle(5, 10)
    
    assert rectangle.side_a == 5
    assert rectangle.side_b == 10
    
def test_get_area():
    rectangle = Rectangle(5, 10)
    
    assert rectangle.get_area() == 50
    
def test_get_perimeter():
    rectangle = Rectangle(5, 10)
    
    assert rectangle.get_perimeter() == 30