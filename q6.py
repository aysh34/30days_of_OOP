class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def give_raise(self, percent):
        self.salary += self.salary * (percent / 100)
        return self.salary

    def employee_details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"The salary has been increased to {raised_salary}")


emp = Employee("David", 1001, 12000)
raised_salary = emp.give_raise(5)  # 5% increase
emp.employee_details()
