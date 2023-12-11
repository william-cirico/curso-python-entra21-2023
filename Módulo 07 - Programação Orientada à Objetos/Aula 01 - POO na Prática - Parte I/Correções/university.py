class University:
    total_students = 0
    total_professors = 0
    
    @classmethod
    def enroll_student(cls):
        cls.total_students += 1
        
    @classmethod
    def hire_professor(cls):
        cls.total_professors += 1
        
    @classmethod
    def get_total_people(cls):
        return cls.total_professors + cls.total_students