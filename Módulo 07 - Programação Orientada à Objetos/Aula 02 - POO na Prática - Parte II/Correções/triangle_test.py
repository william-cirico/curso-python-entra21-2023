import pytest

from triangle import Triangle

def test_valid_triangle():
    triangle = Triangle(10, 5, 6)
    
    assert triangle.side_a == 10
    assert triangle.side_b == 5
    assert triangle.side_c == 6
    
def test_invalid_triangle():
    with pytest.raises(AttributeError):
        triangle = Triangle(10, 20, 30)
        
def test_get_area():
    isosceles_triangle = Triangle(10, 11, 11)
    scalene_triangle = Triangle(10, 5, 6)
    equilateral_triangle = Triangle(10, 10, 10)
    
    assert isosceles_triangle.get_area() == pytest.approx(48.98, 0.1)
    assert scalene_triangle.get_area() == pytest.approx(11.39, 0.1)
    assert equilateral_triangle.get_area() == pytest.approx(43.3, 0.1)
    
def test_get_perimeter():
    triangle = Triangle(10, 5, 6)
    
    assert triangle.get_perimeter() == 21
