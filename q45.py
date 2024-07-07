# Write a function is_palindrome that takes a string as input and returns a boolean indicating whether the string is a palindrome.


def is_palindrome(string: str) -> bool:
    string = string.lower().replace(" ", "")
    reverse_string = string[::-1]
    return reverse_string == string


result1: bool = is_palindrome("Ayesha")
result2 = is_palindrome("Madam")
result3 = is_palindrome("A man a plan a canal Panama")
print(result1)
print(result2)
print(result3)
