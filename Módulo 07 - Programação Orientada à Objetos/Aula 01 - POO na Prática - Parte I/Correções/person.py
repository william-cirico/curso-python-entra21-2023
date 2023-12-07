import re

class InvalidPhoneNumberError(Exception):
    """Exceção para número de telefone inválido."""
    pass

class InvalidNameError(Exception):
    """Exceção para nome inválido."""
    pass


class Person:
    """Person representa uma pessoa.
    
    Attributes:
        name (str): Nome da pessoa.
        phone (str): Número de telefone da pessoa.
    """
    
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return f"Nome: {self.__name} | Telefone: {self.__phone}"
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if not self.__is_name_valid(name):
            raise InvalidNameError()
        
        self.__name = name
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str):
        if not self.__is_phone_valid(phone):
            raise InvalidPhoneNumberError()

        self.__phone = phone
        
    def __is_name_valid(self, nome: str):
        return len(nome.strip().split()) > 1
    
    def __is_phone_valid(self, phone: str):
        phone_regex = r"\+55\s?(?:\([1-9]{2}\)|[1-9]{2})\s?(?:9\s?\d{4}[-.\s]?\d{4}|\d{4}[-.\s]?\d{4})"
        return re.match(phone_regex, phone)
    