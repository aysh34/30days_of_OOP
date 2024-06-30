# Create a class Point with attributes x and y, and implement __eq__ to compare two Point objects based on their coordinates.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False


p1 = Point(2, 3)
p2 = Point(6, 1)
p3 = Point(2, 3)
print(p1 == p2)
print(p2 == p3)
print(p1 == p3)
