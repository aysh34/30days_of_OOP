import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)  # create and return an object initilaized with radius

    def area(self):
        print(f"Area of the circle is {math.pi*(self.radius)**2:.2f}")

# use primary constructor
c = Circle(2)
c.area()
# use alternative constructor
c2 = Circle.from_diameter(4)
c2.area()
