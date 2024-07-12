# Given a list of integers, use the reduce function to find the sum of all the elements in the list.
from functools import reduce

nums = [4, 5, 6, 2, 1, 9, 7]
sumNum = reduce(lambda x, y: x + y, nums)
print(sumNum)

# Given a list of integers, use the reduce function to find the maximum value in the list.
nums = [4, 5, 6, 2, 1, 9, 7]


def maxNum(x: int, y: int):
    if x > y:
        return x
    else:
        return y

# Use reduce to find the maximum value in the list
res = reduce(maxNum, nums)
print(res)
