# Given a list of words ['Hello', 'world', 'from', 'Python'], use the join method to concatenate these words into a single string separated by spaces.
myList = ["Hello", "world", "from", "Python"]
singleStr = " ".join(myList)
print(singleStr)

# Given a list of characters ['P', 'y', 't', 'h', 'o', 'n'], use the join method to concatenate these characters into a single string

characters = ["P", "y", "t", "h", "o", "n"]
newStr = "".join(characters)
print(newStr)

# A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
multiply = [7,14,21,28,35,42,49,56,63,70]
newStr="\n".join(map(str,multiply))
print(newStr)

# You have a list containing different data types [1, 'two', 3.0, 'four'] join them with a space separator.
myList = [1, "two", 3.0, "four"]
newStr = " ".join(map(str, myList))  # map ---> to convert all the elements to string.
print(newStr)
