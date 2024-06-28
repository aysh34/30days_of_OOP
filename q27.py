# How would you implement the __len__ method for a class Library that contains a books of Book objects, to return the number of books in the library?


class Library:
    def __init__(self, books) -> None:
        self.books = books

    def __len__(self):
        return len(self.books)

    def __str__(self) -> str:
        return f"The number of books in the library are {len(self.books)}"


obj = Library(["A", "B", "C", "D"])
print(len(obj))  # call __len__ method
print(str(obj))  # call __str__ method
