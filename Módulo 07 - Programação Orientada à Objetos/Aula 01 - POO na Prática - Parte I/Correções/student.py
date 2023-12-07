from typing import List
from random import randint

from person import InvalidNameError


class InvalidGradeError(Exception):
    """Exceção para nota inválida."""
    pass


class Student:
    """Student representa um aluno.

    Attributes:
        registration (str): Número da matrícula.
        name (str): Nome do aluno.
        grades (List[float]): Notas do aluno.
    """

    def __init__(self, name: str, grades: List[float]):
        self.__registration = randint(1, 100000)
        self.name = name
        self.grades = grades

    @property
    def registration(self):
        return self.__registration

    @property
    def name(self):
        """str: Nome do aluno."""
        return self.__name

    @name.setter
    def name(self, name: str):
        if not self.__is_name_valid(name):
            raise InvalidNameError()

        self.__name = name

    @property
    def grades(self):
        """List[float]: Notas do aluno."""
        return self.__grades

    @grades.setter
    def grades(self, grades: List[float]):
        if not self.__is_grades_valid(grades):
            raise InvalidGradeError()

        self.__grades = grades

    def __is_name_valid(self, nome: str) -> bool:
        """Verifica se um nome é válido.

        Args:
            name (str): Nome que será verificado.

        Returns:
            True caso o nome seja composto, False caso não seja.
        """
        return len(nome.strip().split()) > 1

    def __is_grades_valid(self, grades: List[float]) -> bool:
        """Verifica se todas as notas de uma lista são válidas.

        Args:
            grades (List[float]): Lista de notas.

        Returns: 
            Retorna True se todas as notas forem válidas, caso contrário False.
        """
        return not any(grade < 0 or grade > 10 for grade in grades)

    def get_average(self) -> float:
        """Calcula a média do aluno com base nas notas."""
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def get_situation(self) -> str:
        """Retorna a situação do aluno com base na média.

        Returns:
            A situação do aluno ('Reprovado', 'Recuperação', 'Aprovado').
        """
        media = self.get_average()

        if 0 <= media <= 4:
            return "Reprovado"

        if 5 <= media <= 6:
            return "Recuperação"

        return "Aprovado"
