# If you have a class Book with attributes title and author, how would you implement the __str__ method to return a readable string representation of the book?


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"


book = Book("Atomic Habits", "James Clear")
print(book)  # print instance
