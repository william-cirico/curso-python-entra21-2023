import pytest
from datetime import datetime

from vehicle import Vehicle

def test_calculate_tax():
    current_year = datetime.now().year
    vehicle = Vehicle("Toyota", 2018, 50000)
    
    expected_depreciation = (1 - 0.05) ** (current_year - 2018)
    expected_tax = 50000 * expected_depreciation * 0.02
    
    assert vehicle.calculate_tax() == pytest.approx(expected_tax)
    
def test_calculate_tax_new_vehicle():
    current_year = datetime.now().year
    vehicle = Vehicle("Tesla", current_year, 60000)
    
    expected_tax = 60000 * 0.02
    
    assert vehicle.calculate_tax() == pytest.approx(expected_tax)
    
def test_calculate_tax_old_vehicle():
    current_year = datetime.now().year
    vehicle = Vehicle("Ford", 2000, 30000)
    
    expected_depreciation = (1 - 0.05) ** (current_year - 2000)
    expected_tax = 30000 * expected_depreciation * 0.02
    
    assert vehicle.calculate_tax() == pytest.approx(expected_tax)