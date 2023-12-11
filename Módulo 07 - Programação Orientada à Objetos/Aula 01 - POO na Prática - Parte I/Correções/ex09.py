class Person:
    __total_people = 0
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
        Person.__total_people += 1
        
    @classmethod
    def get_total_people(cls):
        return cls.__total_people
    