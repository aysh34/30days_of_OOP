class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.pages = pages
        self.author = author

    @classmethod
    def from_dict(cls, dict):
        return cls(dict["title"], dict["author"], dict["pages"])

    def show(self):
        print(
            f"Book details are\nTitle: {self.title}, Author: {self.author}, Pages: {self.pages}"
        )


# use primary constructor
b1 = Book("Habits", "George Orwell", 457)
b1.show()

# use alternative constructor
book_info = {"title": "1984", "author": "George Orwell", "pages": 328}
b2 = Book.from_dict(book_info)
b2.show()
