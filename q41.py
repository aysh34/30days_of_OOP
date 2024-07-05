# Create a function called safe_convert that attempts to convert a string to an integer. If the conversion fails, the function should return None and print an appropriate error message. Use this function to process a list of strings.


def safe_convert(nums):
    converted_list = []
    for num in nums:
        try:
            i = int(num)
            converted_list.append(i)
        except ValueError:
            print(f"Error: '{num}' cannot be converted to an integer.")
            converted_list.append(None)
    return converted_list


new_list = safe_convert(["12", "3t", "4", "9"])
print(new_list)
new_list = safe_convert(["12", "3", "4", "9"])
print(new_list)
