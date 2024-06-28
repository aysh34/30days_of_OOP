import math


class MathOperations:
    @staticmethod
    def isPrime(num):
        if num <= 1:
            return False
        elif num == 2 or num == 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(num)) + 1, 6):
            if num % i == 0 or num % (i + 2):
                return False
        return True

    def calculateFactorial(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.calculateFactorial(n - 1)


number = 19
if MathOperations.isPrime(number):  # call a static method without any object
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

obj = MathOperations()
factorial = 5
result = obj.calculateFactorial(factorial)  # call a class method through its object
print(f"The factorial of {factorial} is {result}")
