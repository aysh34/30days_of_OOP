# Write a program that reads a list of numbers (as strings) from the user, converts each to an integer, and calculates the sum. Handle any conversion errors that occur.
list1 = []
for i in range(5):
    try:
        user = int(input("Enter any number: "))
        list1.append(user)

    except ValueError:
        print("Error: Invalid number. Please enter a valid integer.")
    except Exception as e:
        print(e)
print("Sum of the numbers is: ", sum(list1))
