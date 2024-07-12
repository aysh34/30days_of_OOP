# Given a list of integers, first use map to square each number, then use filter to keep only the results that are greater than 5, and finally use reduce to find the sum of these filtered result.
from functools import reduce

nums = [22, 5, 6, 75]
squared_nums = map(lambda x: x**2, nums)

filtered_nums = filter(lambda x: x > 5, squared_nums)

summation = reduce(lambda x, y: x + y, filtered_nums,0) # an initial value of 0 to handle empty list case
print(summation)
