with open("sample.txt") as f:
    print(f.read(5)) # print first 5 characters of the file

with open("sample.txt") as f:
    print(f.readline()) # print the 1st line of the file
    print(f.readline())  # print the 2nd line of the file
