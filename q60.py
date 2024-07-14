# Describe an algorithm to check if two strings s1 and s2 are anagrams of each other.

i = 0


def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


s1 = "bored"
s2 = "robed"
s3, s4 = "inch", "hin"
print(is_anagram(s1, s2))
print(is_anagram(s3, s4))
