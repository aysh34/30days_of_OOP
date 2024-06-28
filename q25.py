class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        string = string.split("-")  # split() returns a list
        return cls(string[0], string[1], string[2])
        # string[0]== self.name, string[1]==self.position, string[2]== self.salary

    def employee_details(self):
        print(
            f"Employee name: {self.name}\nEmployee position: {self.position}\nEmployee salary: {self.salary}\n"
        )


emp1 = Employee("ABC", "CEO", 220000)
emp1.employee_details()

emp2 = Employee.from_string("XYZ-Manager-100000")
emp2.employee_details()
