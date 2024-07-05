# Write a program that asks the user for two inputs: a number and a string. The program should convert the number to an integer and attempt to access an index in the string corresponding to the number. Handle the exceptions for invalid number conversion and index out of range.

string = input("Enter any string: ")
try:
    num = int(input("Enter a number: "))
    print(f"Character '{string[num]}' is present at index {num}")
except IndexError:
    print("Index out of range")
except ValueError:
    print("Error: Invalid input. Please enter valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
