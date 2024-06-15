class Temperature:
    def __init__(self, celsius=0.0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = value - 273.15


temp = Temperature(25)  # Initialize with 25°C
print(f"Celsius: {temp.celsius}°C")  # Celsius: 25.0°C
print(f"Fahrenheit: {temp.fahrenheit}°F")  # Fahrenheit: 77.0°F
print(f"Kelvin: {temp.kelvin}K")  #  Kelvin: 298.15K

# Update the temperature in Fahrenheit
temp.fahrenheit = 98.6
print(
    f"Celsius after setting Fahrenheit: {temp.celsius}°C"
)  # Celsius after setting Fahrenheit: 37.0°C
print(
    f"Kelvin after setting Fahrenheit: {temp.kelvin}K"
)  # Kelvin after setting Fahrenheit: 310.15K

# Update the temperature in Kelvin
temp.kelvin = 273
print(
    f"Celsius after setting Kelvin: {temp.celsius}°C"
)  # Celsius after setting Kelvin: 26.85°C
print(
    f"Fahrenheit after setting Kelvin: {temp.fahrenheit}°F"
)  # Fahrenheit after setting Kelvin: 80.33°F
