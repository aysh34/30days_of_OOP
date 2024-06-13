class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def cal_area(self):
        return self.length * self.width

    @staticmethod
    def compare_area(rect1, rect2):
        area1 = rec1.cal_area()
        area2 = rec2.cal_area()
        if area1 > area2:
            return f"Larger area: {area1}"
        elif area2 > area1:
            return f"Larger area: {area2}"
        else:
            return "Both have same area"

rec1 = Rectangle(6, 3)
rec2 = Rectangle(4, 7)
result = Rectangle.compare_area(rec1, rec2)
print(result)