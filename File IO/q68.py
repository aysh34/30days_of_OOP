# Write a program that creates a CSV file called students.csv with columns "Name", "Grade", and "ID", and write data for at least five students

with open("students.csv", "w") as f:
    f.write("Name  Grade  ID\n")
    f.writelines("A     A+    1001\n")
    f.writelines("K     C     1002\n")
    f.writelines("Z     F     1003\n")
    f.writelines("Y     E     1004\n")
    f.writelines("X     B     1005\n")
