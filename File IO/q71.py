# seek()
with open("sample.txt") as f:
    f.seek(12)  # move to the 12th byte in the file
    print(f.read(5))  # read 5 byte from current position

# tell()
with open("sample.txt") as f:
    f.seek(12)
    print(f.tell())  # returns the current position of the file pointer

# truncate()
with open("truncate.txt", "r+") as f:
    print("\nContent before truncation:", f.read())
    f.truncate(12)  # Truncate the file to 12 bytes
    f.seek(0)  # move to the beginning of the file
    print("\nContent after truncation:", f.read())
