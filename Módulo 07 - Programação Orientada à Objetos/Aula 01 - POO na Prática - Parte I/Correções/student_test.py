import pytest

from student import Student, InvalidGradeError, InvalidNameError

def test_create_student():
    student = Student("William Círico", [7, 8, 10])
    
    assert student.name == "William Círico"
    assert student.grades == [7, 8, 10]
    

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        Student("William", [7, 8, 10])
        

def test_invalid_grades():
    with pytest.raises(InvalidGradeError):
        Student("William Círico", [7, -1, 10])
        
def test_student_registration():
    student = Student("William Círico", [7, 8, 10])
    
    assert 1 <= student.registration <= 100000
    
def test_student_average():
    student = Student("William Círico", [10, 10, 10])
    
    assert student.get_average() == 10
    
    
def test_student_average_without_grades():
    student = Student("William Círico", [])
    
    assert student.get_average() == 0
    

def test_get_student_situation_approved():
    student = Student("William Círico", [10, 10, 10])
    
    assert student.get_situation() == "Aprovado"
    

def test_get_student_situation_recovery():
    student = Student("William Círico", [6, 6, 6])
    
    assert student.get_situation() == "Recuperação"
    

def test_get_student_situation_failed():
    student = Student("William Círico", [2, 2, 2])
    
    assert student.get_situation() == "Reprovado"

