class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Books:", self.books)

l = Library()
l.add_book("Python")
l.add_book("Java")
l.show_books()

