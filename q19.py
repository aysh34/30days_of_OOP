class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(
            f"{self.name} is {self.age} years old studing in school '{self.school_name}'"
        )


stu1 = Student("A", 20)
stu1.get_details()
stu1.school_name = "XYZ School"  # creating instance variable
stu1.get_details()  # instance variable takes preference over class variable of same name
stu2 = Student("B", 20)
stu2.get_details()
Student.school_name = "WXY School"  # modifying class variable
stu2.get_details()
