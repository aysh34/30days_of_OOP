# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder.

for i in range(2,21):
    with open(f"Table_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")
