"""
As classes são modelos que definem um tipo de objeto específico. Uma classe
descreve as características (atributos) e os comportamentos (métodos) dos
objetos que serão criados (instânciados) através dessa classe terão.
"""

# Sintaxe de declaração de uma classe
class NomeClasse: # Utilizar CapWords: https://peps.python.org/pep-0008/#class-names
    """Docstring da classe"""

    # Construtor -> Método utilizado para inicializar o objeto
    def __init__(self, parametro1: int) -> None:
        # Self é utilizado para acessar os atributos e métodos do objeto instânciado
        self.atributo1 = parametro1
        self.__atributo_privado1 = 0 # Atributo privado

    def metodo1(self, valor1: int) -> None:
        """Docstring do método"""
        print(valor1)

    # Getter
    @property
    def atributo_privado(self) -> str:
        """Docstring do método"""
        return self.__atributo_privado1
    
    # Setter
    @atributo_privado.setter
    def atributo_privado(self, novo_valor) -> None:
        self.__atributo_privado1 = novo_valor
