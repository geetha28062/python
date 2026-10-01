class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(self.name, "issued")
        else:
            print("Book not available")

b = Book("Python")
b.issue()
