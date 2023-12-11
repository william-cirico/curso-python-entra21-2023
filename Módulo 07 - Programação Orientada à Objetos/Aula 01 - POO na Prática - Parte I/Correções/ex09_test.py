import pytest

from ex09 import Person

def test_get_total_people():
    person1 = Person("Person 1", 22)
    person2 = Person("Person 2", 23)
    
    assert Person.get_total_people() == 2