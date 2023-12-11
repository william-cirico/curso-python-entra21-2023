import pytest

from car import Car

def test_car_speed_up():
    car = Car("Toyota", "Corolla", 2021)
    
    car.speed_up()
    
    assert car.speed == 10
    
    
def test_car_break():
    car = Car("Toyota", "Corolla", 2021)
    
    car.speed_up()
    car.brake()
    
    assert car.speed == 5
    
def test_car_break_when_stopped():
    car = Car("Toyota", "Corolla", 2021)
    
    car.brake()
    
    assert car.speed == 0