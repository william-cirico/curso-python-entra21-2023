import pytest

from calculator import Calculator


def test_sum():
    assert Calculator.sum(1, 2, 3) == 6
    
def test_sub():
    assert Calculator.sub(1, 2, 3) == -4
    
def test_mul():
    assert Calculator.mul(1, 2, 3) == 6
    
def test_div():
    assert Calculator.div(6, 2, 3) == 1 
    
def test_div():
    with pytest.raises(ZeroDivisionError):
        assert Calculator.div(2, 0)