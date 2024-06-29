#  Implement a class ComplexNumber that supports addition (+), subtraction (-) operators for complex numbers


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # c1+c2 = (a+c)+(b+d)i
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        # c1−c2 = (a−c)+(b−d)i
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = ComplexNumber(4, 8)
c2 = ComplexNumber(6, 5)
c3 = c1 + c2  # c1.__add__(c2) , The returned object from __add__() is assigned to c3
c4 = c1 - c2  # The returned object from __sub__() is assigned to c4
print(c1)
print(c2)
print("The addition of complex numbers is ", c3)
print("The subtraction of complex numbers is ", c4)
