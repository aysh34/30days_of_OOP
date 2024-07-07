# Create a function process_data that takes a dictionary data where each key is a string and each value is a list of tuples. Each tuple consists of an integer and a string. The function should return a dictionary where each key is a string and each value is an integer representing the sum of integers from tuples associated with that key.

from typing import Dict, Tuple, List


def process_data(data: dict[str, list[tuple[int, str]]]) -> dict[str, int]:
    result = {}
    for key, tuple_list in data.items():
        total_sum = 0
        for pair in tuple_list:
            total_sum += pair[0]  # summing the integers in each tuple
        result[key] = total_sum  # assigning the total sum to result[key]
    return result


data = {"key1": [(2, "A"), (4, "B"), (6, "C")], "key2": [(1, "A"), (5, "B")]}
print(process_data(data))
