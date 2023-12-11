class Triangle:
    def __init__(self, a: float, b: float, c: float):
        if not self.__is_triangle(a, b, c):
            raise ValueError("Os valores fornecidos não forma um triângulo")
        
        self.__a = a
        self.__b = b
        self.__c = c
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
        
    def __is_triangle(self, a: float, b: float, c: float) -> bool:
        return (a + b > c) and (a + c > b) and (b + c > a)
        
    def get_type(self) -> str:
        if self.__b == self.__a == self.__c:
            return "Equilátero"
        
        if self.__b != self.__a != self.__c:
            return "Escaleno"

        return "Isósceles"