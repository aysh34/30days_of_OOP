# Problem: Write a recursive function to perform binary search on a sorted array.
def search(arr, target, s, e) -> int:
    if s > e:
        return -1  # Base case: target not found
    m = (s + e) // 2
    if arr[m] == target:
        return m
    elif arr[m] > target:
        return search(arr, target, s, m - 1)
    else:
        return search(arr, target, m + 1, e)


arr = [1, 2, 3, 4, 5, 6]
print(search(arr, 15, 0, len(arr) - 1))
print(search(arr, 5, 0, len(arr) - 1))
