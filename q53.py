# Define a lambda function that checks if a number is even.

is_even = lambda x:x%2==0
print(is_even(4))
print(is_even(5))


# Sort based on the second element of each tuple
points = [(1, 2), (4, 1), (3, 3), (5, -1)]
print("Before sorting:", points)
sorted_points = sorted(points, key=lambda x: x[1])
print("After sorting:", sorted_points)

# sorting a dictionary by values
student_grades = {'Alice': 90, 'Bob': 85, 'Charlie': 95}
print(student_grades.items())
sorted_grades = sorted(student_grades.items(), key=lambda x: x[1])
print(sorted_grades)

