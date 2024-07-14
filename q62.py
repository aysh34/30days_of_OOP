# f-strings
name = "A"
age = 20
print(f"{name} is {age} years old.")

# format method
product = "laptop"
price = 234
print("The price of {} is {}$".format(product, price))

# using %
favorite_language = "python"
print("My favorite language is %s" % favorite_language)  # %d for integer

# format_map()
data = {"name": "A", "age": 20}
student = "Name of student is '{name}' and she is {age} years old.".format_map(data)
print(student)
