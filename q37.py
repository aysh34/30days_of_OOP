# Define an abstract class GeometricShape with the following abstract methods: area, perimeter. Create concrete classe RightTriangle,that inherit from GeometricShape and implement the abstract methods.

from abc import ABC, abstractmethod

import math


class GeometricShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class RightTriangle(GeometricShape):

    def __init__(self, height, base):
        self.height = height
        self.base = base
        self.hypotenuse = math.sqrt(self.height**2 + self.base**2)

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.height + self.hypotenuse


triangle = RightTriangle(4, 3)
output = triangle.area()
print("Area:", output)
output = triangle.perimeter()
print("Perimeter:", output)
