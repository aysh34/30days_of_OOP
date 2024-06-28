class Temprature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    def temp_in_celsius(self):
        print(f"Temprature in celcius is {self.celsius:.2f}")


t1 = Temprature(40)
t1.temp_in_celsius()
t2 = Temprature.from_fahrenheit(104)
t2.temp_in_celsius()
