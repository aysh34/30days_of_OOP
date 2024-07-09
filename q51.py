# Write a function print_index_value_pairs that takes a list of strings as input and prints each string along with its index in the format "Index: Value".


def print_index_value_pairs(s: list):
    for index, item in enumerate(s):
        print(f"{index}:{item}")


print_index_value_pairs(["A", "B", "C", "D"])

# Write a function find_indices that takes a list of integers and a target integer as input. Return a list of indices where the target integer appears in the list. Use enumerate for indexing.


def find_indices(s: list, target: int) -> list[int]:
    list_indices = []
    for index, item in enumerate(s):
        if item == target:
            list_indices.append(index)
    return list_indices


result = find_indices([2, 55, 4, 1, 2, 77, 2, 9], 2)
print(result)
