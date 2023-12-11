import pytest

from university import University

@pytest.fixture(autouse=True)
def reset_university_class():
    University.total_professors = 0
    University.total_students = 0

def test_enroll_student():
    University.enroll_student()
    assert University.total_students == 1
    
def test_hire_professor():
    University.hire_professor()
    assert University.total_professors == 1
    
def test_get_total_people():
    University.hire_professor()
    University.enroll_student()
    
    assert University.get_total_people() == 2