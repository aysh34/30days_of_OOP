# Write a program that reads an integer from the user and then accesses an index in a list of five numbers. Handle the exceptions for invalid input and index out of range.

num = [2, 5, 78, 55, 4]
user = int(input("Enter a number: "))
try:
    print(f"Number at index {user} is {num[user]}")
except Exception as e:
    print(e)

print("Successful")