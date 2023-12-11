import pytest

from point2d import Point2D

def test_has_common_axis():
    pointA = Point2D(1, 1)
    pointB = Point2D(1, 2)
    
    assert Point2D.has_common_axis(pointA, pointB) == True
    
def test_doesnt_have_common_axis():
    pointA = Point2D(1, 1)
    pointB = Point2D(3, 2)
    
    assert Point2D.has_common_axis(pointA, pointB) == False