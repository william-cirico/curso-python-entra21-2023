import pytest

from person import Person, InvalidPhoneNumberError, InvalidNameError

def test_person_creation():
    person = Person("William Círico", "+55 47 8408-8520")
    
    assert person.name == "William Círico"
    assert person.phone == "+55 47 8408-8520"
    

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        Person("William", "+55 47 8408-8520")
    

def test_invalid_phone():
    with pytest.raises(InvalidPhoneNumberError):
        Person("William Círico", "47 8408-8520")
        
        
def test_valid_updates():
    person = Person("William Círico", "+55 47 8408-8520")
    person.name = "William Teste"
    person.phone = "+55 47 9 8408-8520"
    
    assert person.name == "William Teste"
    assert person.phone == "+55 47 9 8408-8520"
    
    
def test_str_method():
    person = Person("William Círico", "+55 47 8408-8520")
    
    assert person.__str__() == "Nome: William Círico | Telefone: +55 47 8408-8520"