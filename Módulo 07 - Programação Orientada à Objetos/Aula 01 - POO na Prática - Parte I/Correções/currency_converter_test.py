import pytest

from currency_converter import CurrencyConverter

def test_convert_to_BRL():
    converted_value = CurrencyConverter.convert_to_BRL(10)
    
    assert converted_value == pytest.approx(49.28, 0.5)
    
def test_convert_from_BRL():
    converted_value = CurrencyConverter.convert_from_BRL(10)
    
    assert converted_value == pytest.approx(2.03, 0.5)