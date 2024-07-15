# Write a function to calculate the power of a number x^n using recursion


def power(num, exp) -> int:
    if exp == 0:
        return 1
    else:
        return num * power(num, exp - 1)
print(power(3, 3))


# Write a function to find the GCD of two numbers using recursion.
def greatest_common_divisor(n1, n2):
    if n2 == 0:
        return n1  # the GCD of any number and 0 is the number itself.
    else:
        return greatest_common_divisor(n2, n1 % n2)
print(greatest_common_divisor(48, 18))
