import pytest
from io import StringIO
import sys

from phone_book import PhoneBook
from person import Person

def test_add_person():
    person = Person("Ana Paula", "+55 (47) 9 9999-9999")
    
    phone_book = PhoneBook("Agenda de contatos")
    phone_book.add_person(person)
    
    assert person in phone_book.people
    assert len(phone_book.people) == 1
    
    
def test_add_person_failed(capfd):
    phone_book = PhoneBook("Agenda de contatos")
    
    for i in range(10):
        phone_book.add_person(Person(f"Pessoa {i}", f"+55 (47) 9 9999-999{i}"))
        
    extra_person = Person("Pessoa Extra", "+55 (47) 9 9999-9929")
    phone_book.add_person(extra_person)
    
    out, _ = capfd.readouterr()
    
    assert extra_person not in phone_book.people
    assert "Agenda lotada." in out

def test_remove_person():
    phone_book = PhoneBook("Agenda de Teste")
    person = Person("Ana Paula", "+55 (47) 9 9999-9929")
    phone_book.add_person(person)
    phone_book.remove_person("Ana Paula")
    
    assert person not in phone_book.people
    
def test_remove_person_failed(capfd):
    phone_book = PhoneBook("Agenda de Teste")
    
    phone_book.remove_person("Ana")
    
    out, _ = capfd.readouterr()
    assert "Pessoa não foi encontrada." in out
    
def test_search_person(capfd):
    phone_book = PhoneBook("Agenda de Teste")
    person = Person("Ana Paula", "+55 (47) 9 9999-9929")
    phone_book.add_person(person)
    
    phone_book.search_person("Ana Paula")
    
    out, _ = capfd.readouterr()
    
    assert out == "Nome: Ana Paula | Telefone: +55 (47) 9 9999-9929\n"

def test_search_person_failed(capfd):
    phone_book = PhoneBook("Agenda de Teste")
    person = Person("Ana Paula", "+55 (47) 9 9999-9929")
    
    phone_book.search_person("Ana Paula")
    
    out, _ = capfd.readouterr()
    assert "Pessoa não encontrada." in out

def test_list_people(capfd): 
    phone_book = PhoneBook("Agenda de contatos")
    phone_book.add_person(Person("Ana Paula", "+55 (47) 9 9999-9999"))
    phone_book.add_person(Person("João Pedro", "+55 (47) 9 9899-9999"))
    
    phone_book.list_people()
    
    out, _ = capfd.readouterr()
    
    expected_output = "Nome: Ana Paula | Telefone: +55 (47) 9 9999-9999\nNome: João Pedro | Telefone: +55 (47) 9 9899-9999\n"
    
    assert out == expected_output