# Factorial of a number
def factorial(n) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))

# Write a function to find the n-th Fibonacci number.
# Fibonacci Sequence --> F(n)=F(n−1)+F(n−2) 0,1,1,2,3,5,8,13,21,34,55,…
def fibonacci(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
