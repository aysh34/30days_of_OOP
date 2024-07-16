# Given a large text file data.txt, write a program that reads the file in chunks of 1024 bytes and prints each chunk

with open("data.txt") as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        print(chunk)
