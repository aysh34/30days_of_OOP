class Student:
    total_students = 0
    total_grades = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.update_statistics(grade)  # call a class method

    @classmethod
    def update_statistics(cls, new_grade):
        cls.total_students += 1
        cls.total_grades += new_grade
        print(f"Total students: {cls.total_students}\nTotal grades: {cls.total_grades}")


student1 = Student("A", 20)
student2 = Student("B", 30)
student3 = Student("C", 50)