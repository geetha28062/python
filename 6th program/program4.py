class Book:
    def __init__(self, name):
        self.name = name
        self.available = False

    def return_book(self):
        self.available = True
        print(self.name, "is returned")


book = Book("Python")
book.return_book()
