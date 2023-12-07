from person import Person

class PhoneBook:
    """Representa uma agenda.
    
    Attributes:
        name (str): Nome da agenda.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.__people = []
        
    @property
    def people(self):
        """List[People]: Pessoas da agenda."""
        return self.__people
        
    def add_person(self, person: Person):
        """Adiciona uma pessoa na agenda.
        
        Args:
            person (Person): Pessoa que será adicionada na agenda.
        """
        if len(self.__people) < 10:
            self.__people.append(person)
        else:
            print("Agenda lotada.")
            
    def remove_person(self, name: str):
        """Remove uma pessoa da agenda pelo nome.
        
        Args:
            name (str): Nome da pessoa.
        """
        for pessoa in self.__people:
            if pessoa.name == name:
                self.__people.remove(pessoa)
                return
            
        print("Pessoa não foi encontrada.")
        
    def search_person(self, name: str):
        """Mostra as informações de uma pessoa se ela estiver na agenda.
        
        Args:
            name (str): Nome da pessoa.
        """
        for person in self.__people:
            if person.name == name:
                print(person)
                return
        
        print("Pessoa não encontrada.")
        
    def list_people(self):
        """Lista as pessoas da agenda."""
        for person in self.__people:
            print(person)
        
    
    