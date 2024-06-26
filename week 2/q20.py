class Employee:
    num_of_employees = 0

    @classmethod
    def increment_employee_count(cls):  # cls refers to class itself
        cls.num_of_employees += 1

    def display_employee_count(self):  # self refers to the instance
        print(f"The number of employees are {self.num_of_employees}")


e1 = Employee()
e1.increment_employee_count()
e1.display_employee_count()
e2 = Employee()
e2.increment_employee_count()
e2.display_employee_count()
