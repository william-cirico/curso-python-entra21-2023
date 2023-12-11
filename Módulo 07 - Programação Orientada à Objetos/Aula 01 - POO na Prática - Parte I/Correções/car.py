class Car:
    """Car representa um carro."""
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.__speed = 0
    
    @property
    def speed(self):
        return self.__speed
    
    def speed_up(self):
        """Acelera o carro."""
        self.__speed += 10
        
    def brake(self):
        """Freia o carro."""
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
    
    