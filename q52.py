# Generate a list of all the numbers divisible by 3 from 1 to 30.

nums=[n for n in range(1,31) if n%3==0]
print("Q1: ",nums)

# Generate a list of all the vowels in a given string.
s="I am passionate"
vowels=[vowel for vowel in s if vowel.lower() in 'aeiou']
print("Q2: ",vowels)


# Generate a list of the palindromes from a given list of strings.
words = ["radar", "level", "world", "python", "civic", "deified", "noon", "hello"]

palindromes=[word for word in words if word==word[::-1]]
print("Q3: ",palindromes)

# Create a list of the element-wise sums of two lists of the same length
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
sumNum=[x+y for x,y in zip(l1,l2)] # zip to pair corresponding elements
print("Q4: ",sumNum)

# Write a list comprehension to print a list which contains the multiplication table of a user entered number.
num=int(input("Enter a number: "))
multiply=[num*i for i in range(1,11)]
print("Q5: ",multiply)

