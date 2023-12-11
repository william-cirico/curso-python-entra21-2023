import pytest

from person import Person, InvalidNameError, InvalidPhoneError

def test_person_creation():
    person = Person("William Círico", "+55 47 9 9999-9999")
    
    assert person.name == "William Círico"
    assert person.phone == "+55 47 9 9999-9999"
    
def test_invalid_name():
    with pytest.raises(InvalidNameError): 
        person = Person("William", "+55 47 9 9999-9999")
        
def test_invalid_phone():
    with pytest.raises(InvalidPhoneError): 
        person = Person("William Círico", "")