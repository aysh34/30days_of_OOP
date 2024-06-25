
class Class:
    no_of_objects = 0   # class variable

    def __init__(self):
        Class.no_of_objects += 1  

    def show(self):
        print(f"you have created {self.no_of_objects} objects so far")


obj1 = Class()
obj1.show()
obj2 = Class()
obj2.show()
obj3 = Class()
obj3.show()
