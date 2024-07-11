# Given a list of integers, use the map function to create a new list where each integer is doubled.
myList = [3, 4, 5, 6]
new_list = map(lambda x: x * 2, myList)
print(list(new_list))

# Given two lists of numbers of the same length, use the map function to create a new list where each element is the sum of the corresponding elements from the two lists.

l1 = [3, 6, 7, 9, 1]
l2 = [13, 16, 17, 19, 1]
sumLists = map(lambda x, y: x + y, l1, l2)
print(list(sumLists))

# Given a list of tuples, where each tuple contains two numbers, use map to create a new list of the products of the numbers in each tuple. Describe how you would do this.
nums = [(1, 2), (3, 4), (5, 6), (7, 8)]


def product(pair):
    return pair[0] * pair[1]


product_list = map(product, nums)
print(list(product_list))

# Given a list of strings representing numbers with potential leading or trailing spaces use map to strip the spaces and convert them to integers.

stringsList = [" 1 ", " 2 ", " 3 "]
integersList = map(lambda x: int(x.strip()), stringsList)
print(list(integersList))
