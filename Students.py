class Student:
    student_id = ()
    student_name = ()
    email = ()
    grades = {}
    courses = []

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades
        self.courses = courses
        pass
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
        pass

    class StudentRecords:
        def __init__(self, student_id, student_name, email, grades=None, courses=None):
            self.student_id = student_id
            self.student_name = student_name
            self.email = email
            self.grades = grades
            self.courses = courses
            self.records = []

        @classmethod
        def add_student(cls, student_id, student_name, email):

        @classmethod
        def update_student(cls, student_id, student_name=None, email=None):

        @classmethod
        def delete_student(cls, student_id):

        @classmethod
        def enrollcourse(cls, student_id, course):

        @classmethod
        def searchstudent(cls, student_id):
        
