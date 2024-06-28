class Student:
    def __init__(self, name, roll_no, grades):
        self.name = name
        self.roll_no = roll_no
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

stud = Student("Samaira", 6, [33, 43, 56, 78])
res = stud.calculate_average()
print(f"{stud.name} has average grade of {res}")
