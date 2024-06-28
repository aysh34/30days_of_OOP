class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Car Information\nBrand: {self.brand}, Model: {self.model}, Year: {self.year}"


# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())
