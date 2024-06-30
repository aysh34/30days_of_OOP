# Create a class Student with attributes name, age, and grades. Implement __eq__ to compare students based on their average grades.
# Write a scenario where you compare instances of Student objects and demonstrate the use of == for custom equality checks.


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __eq__(self, other):
        self.avg_grades = sum(self.grades) / len(self.grades)
        other.avg_grades = sum(other.grades) / len(other.grades)
        return (
            self.avg_grades == other.avg_grades
        )  # whether the average grades of two Student objects are equal or not


s1 = Student("X", 20, [30, 40, 60])
s2 = Student("Y", 20, [20, 30, 50])
s3 = Student("Z", 19, [50, 30, 20])
print(f"{s1.name} and {s2.name} have equal average grades: {s1==s2}")
print(f"{s1.name} and {s3.name} have equal average grades: {s1==s3}")
print(f"{s2.name} and {s3.name} have equal average grades: {s2==s3}")
