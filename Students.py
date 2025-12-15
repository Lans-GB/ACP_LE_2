#LANCE ANDREY SILVA | BSIT 2107 | LAB 2 - STUDENT RECORDS MANAGEMENT SYSTEM

class Student:  # STUDENT CLASS TO HOLD STUDENT DETAILS
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name) #tu
        self.email = email
        self.grades = grades or {}
        self.courses = courses or set()

    def __str__(self): #FORMATTED STRING OUTPUT FOR STUDENT DETAILS
        return f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"

    def calc(self): # CALCULATES GPA FOR ALL STUDENTS
        if not self.grades:
            return 0.0
        transmuted = 0
        for score in self.grades.values(): #GRADE SYSTEM ACCORDING TO BATSTATEU STANDARDS
            if score >= 98:
                transmuted += 1.0
            elif score >= 90:
                transmuted += 1.5
            elif score >= 80:
                transmuted += 2.5
            elif score >= 75:
                transmuted += 3.0
            elif score >= 61:
                transmuted += 4.0
            elif score <= 60:
                transmuted += 5.0
            else:
                transmuted += 0.0
        return transmuted / len(self.grades)

class StudentRecords:
    students = []  # CLASS VARIABLE TO STORE STUDENTS

    @classmethod
    def add_student(cls, student_id, student_name, email, grades=None, courses=None):
        enroll = Student(student_id, student_name, email, grades, courses)
        cls.students.append(enroll)
        return "Student added successfully."
    pass

    @classmethod
    def update_student(cls, student_id, email=None, grades=None, courses=None):
        for student in cls.students:
            if student.id_name[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades.update(grades)
                if courses is not None:
                    student.courses.update(courses)
                return "Student updated successfully."
        return "Student not found."
    pass

    @classmethod
    def delete_student(cls, student_id):
        length = len(cls.students)
        cls.students = [student for student in cls.students if student.id_name[0] != student_id]
        if len(cls.students) < length:
            return "Student deleted successfully."
        return "Student not found."
    pass

    @classmethod
    def enroll_course(cls, student_id, course):
        for student in cls.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return "Course enrolled successfully."
        return "Student not found."
    pass

    @classmethod
    def search_student(cls, student_id):
        for student in cls.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"
    pass

    @classmethod
    def search_by_name(cls, name):
        r = []
        for student in cls.students:
            if name.lower() in student.id_name[1].lower():
                r.append(str(student))
        return r if r else ["No matches found."]
    pass

    @classmethod
    def get_all_students(cls): # GETS ALL STUDENTS FOR GPA CALCULATION
        return cls.students
    pass

# ---------------------------------------------------------------------------------------
# OUTPUT FOR ALL METHODS
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":

    # ADD STUDENTS TO THE LIST
    print("ADDING STUDENTS:") 
    print(StudentRecords.add_student(1, "Lance Andrey", "lance.andrey@gmail.com", grades={"CS111": 92, "CS211": 88}))
    print(StudentRecords.add_student(2, "Kendrell Jam", "kendrell@gmail.com", grades ={"MATH101": 85, "PHY101": 78}))
    print(StudentRecords.add_student(3, "John Del", "jandel.gag@gmail.com", grades ={"GAG101": 85, "RBX102": 78}))
    print(StudentRecords.add_student(4, "Sam Mhy", "sammy.sab@gmail.com", grades ={"SAB392": 85, "RBX102": 80}))
    print(StudentRecords.add_student(5, "Lance", "lancesdhusd@gmail.com", grades ={"GAG101": 90, "SAB201": 100}))

    # UPDATE STUDENT DETAILS
    print("\nUPDATING STUDENTS INFORMATION: ")
    print(StudentRecords.update_student(1, grades={"CS111": 100, "CS211": 85, "IT101": 89}, courses={"IT"}))
    print(StudentRecords.update_student(2, grades={"IT121": 78, "CS211": 90, "PHY101": 89}, courses={"IT"}))
    print(StudentRecords.update_student(4, email="invalid@gmail.com"))

    # ENROLL COURSES FOR STUDENTS
    print("\nENROLLING COURSES: ")
    print(StudentRecords.enroll_course(1, "Python"))
    print(StudentRecords.enroll_course(1, "Java"))
    print(StudentRecords.enroll_course(2, "Python"))

    # SEARCH STUDENTS
    print("\nSEARCH RESULTS:")
    print(StudentRecords.search_student(1)) #SEARCH STUDENT USING ID
    print(StudentRecords.search_by_name("lance")) #SEARCH STUDENT USING NAME
    print(StudentRecords.search_by_name("mamamo"))
    print(StudentRecords.search_by_name("john"))

    # GPA CALCULATION FOR ALL STUDENTS
    print("\nGPA OF ALL STUDENTS:")
    all_students = StudentRecords.get_all_students()
    for gpa in all_students:
        print(f"{gpa.id_name[1]} GPA: {gpa.calc():.2f}")

    # DELETE STUDENTS FROM THE LIST
    print("\nSTUDENT DELETION")
    print(StudentRecords.delete_student(2))  #DELETE STUDENT USING ID
    print(StudentRecords.search_student(2))  #VERIFY STUDENT INFO DELETION

    print("\nFINAL LIST OF STUDENTS:")
    for student in StudentRecords.get_all_students():
        print(student)

