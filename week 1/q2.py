class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."


# Create an instance of the Calculator class
calc = Calculator()

print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))

