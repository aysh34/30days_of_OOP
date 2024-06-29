# Write a Python class Vector that overloads the + operator to perform vector addition.
# Implement the __str__ method in the Vector class to provide a string representation of vector objects.


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):  # self refers to vec1, other refers to vec2
        return Vector(
            self.x + other.x, self.y + other.y, self.z + other.z
        )  # returned vector object will store in resultant_vec

    def __str__(self):  # for string representation of object
        return f"{self.x}x + {self.y}y + {self.z}z"


vec1 = Vector(2, 4, 5)
vec2 = Vector(1, 3, 6)
resultant_vec = vec1 + vec2
print(vec1)
print(vec2)
print("The resultant vector is ", resultant_vec)
