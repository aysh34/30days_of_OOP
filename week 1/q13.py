class Product:
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def displayProductDetails(self):
        print(f"Product: {self.product}\nPrice: {self.price}")


class Electronics(Product):
    def __init__(self, product, price, warranty, brand):
        super().__init__(product, price)  # accessing super class' constructor
        self.warranty = warranty
        self.brand = brand

    def displayProductDetails(self):  # method overriding
        super().displayProductDetails()
        print(f"Warranty Period: {self.warranty}\nBrand: {self.brand}")


class SmartPhone(Electronics):
    def __init__(self, product, price, warranty, brand, system, camera):
        super().__init__(product, price, warranty, brand)
        self.system = system
        self.camera = camera

    def displayProductDetails(self):
        super().displayProductDetails()
        print(f"OS: {self.system}\nCamera quality: {self.camera}")


phone = SmartPhone("iPhone 14 Pro Max", "$1731", "2 years", "Apple", "iOS 16", "48 MP")
phone.displayProductDetails()
