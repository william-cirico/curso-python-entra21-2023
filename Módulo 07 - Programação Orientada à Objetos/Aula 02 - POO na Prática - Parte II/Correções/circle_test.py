import pytest

from circle import Circle

def test_circle_creation():
    circle = Circle(20)
    
    assert circle.radius == 20
    
def test_get_area():
    circle = Circle(20)
    
    assert circle.get_area() == pytest.approx(1256.64, 0.1)
    
def test_get_perimeter():
    circle = Circle(20)
    
    assert circle.get_perimeter() == pytest.approx(125.6, 0.1)