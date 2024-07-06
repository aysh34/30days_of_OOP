# Write a Python script to filter out and print all even numbers from a given list of numbers using the walrus operator.

nums = [2, 3, 5, 8, 10, 13]
for num in nums:
    if is_even := num % 2 == 0:
        print(num)
# the walrus operator := is used to both check if num is even and assign the result to is_even