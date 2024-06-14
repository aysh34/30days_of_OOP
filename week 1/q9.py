class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_availability(checkout_method):
        def wrapper(self):
            if self.available:
                checkout_method(self)
            else:
                print(
                    f"Sorry, the book '{self.title}' by {self.author} is currently not available for checkout."
                )

        return wrapper

    @check_availability
    def checkout(self):
        self.available = False
        print(f"Book '{self.title}' by {self.author} has been checked out.")


book1 = Book("Python", "Abc")
book1.checkout()
book1.checkout()