# Describe a scenario where implementing the __call__ method would be useful for a class Multiplier that multiplies a given number by a predefined factor.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        self.number = number
        self.result = self.number * self.factor
        return self.result

    def __str__(self) -> str:
        return f"The result after multiplying number with predefined factor is {self.result}"


m = Multiplier(4)
m(2)  # it'll call __call__ method
print(str(m))  # it'll call __str__ method
