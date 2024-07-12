# Given a list of strings, use the filter function to keep only the strings that start with the letter 'a'.
l = ["abc", "avx", "xyz", "wxyz", "atr"]

def is_start(s: str):
    return s.startswith("a")

new_list = filter(is_start, l)
print(list(new_list))

# Given a list of dictionaries representing students with keys "name" and "grade", use the filter function to keep only the students with grades above 75.
students = [
    {"name": "A", "grade": 88},
    {"name": "B", "grade": 72},
    {"name": "C", "grade": 90},
    {"name": "D", "grade": 65},
    {"name": "E", "grade": 78},
    {"name": "F", "grade": 55},
    {"name": "G", "grade": 82},
]
def grade(grades:dict):
    return grades["grade"]>=75


# Use filter to apply the function to the list of students.
new_students=filter(grade,students)
print(list(new_students))
