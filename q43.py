# Create a program that continuously takes integer inputs from the user and stops when the user inputs zero. Print the sum of all entered numbers. Use the walrus operator to streamline your code.
sum1 = 0
while (n := int(input("Enter a number "))) != 0:
    sum1 += n

print("The sum of all entered numbers is:", sum1)
