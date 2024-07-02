# You are developing a Python class to manage employee details in a small company's HR system. Describe how you would use encapsulation principles to ensure the security and integrity of employee data


class Employee:
    def __init__(self, name, age, salary, employee_id, department):
        self._name = name  # protected attribute
        self.age = age  
        self._salary = salary
        self.__employee_id = employee_id  # private attribute
        self._department = department

    # Public method
    def set_salary(self, new_salary):
        self._salary = new_salary

    # Protected method
    def _calculate_bonus(self):
        return self._salary * 0.1

    # Private method
    def __encrypt_employee_id(self):
        return self.__employee_id

    # Public method
    def display_info(self):
        # Accessing protected and private attributes via public methods
        encrypted_id = self.__encrypt_employee_id()  # Accessing private method
        return f"Name: {self._name}, Salary: {self._salary}, Encrypted ID: ###{encrypted_id}###"


# Creating an instance of Employee
emp1 = Employee("ABD", 40, 50000, 12345, "IT")
emp1.set_salary(55000)
print(emp1.display_info())

# print(emp1._salary)       # valid but against encapsulation principles
# print(emp1._Employee__employee_id) # accessing through name mangling but discourged
