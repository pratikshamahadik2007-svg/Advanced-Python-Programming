# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'"{self.title}" has been borrowed.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not borrowed.')


# Patron Class
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'{self.name} cannot borrow "{book.title}".')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'{self.name} did not borrow "{book.title}".')


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to library.')

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron "{patron.name}" registered.')

    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            patron.borrow_book(book)
        else:
            print("Patron or Book not found.")

    def return_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            patron.return_book(book)
        else:
            print("Patron or Book not found.")


# ---------------- Main Program ----------------

# Create Library Instance
library = Library()

# Add Books
book1 = Book("Python Basics", "John Smith", "101")
book2 = Book("Data Structures", "Alice Brown", "102")

library.add_book(book1)
library.add_book(book2)

print()

# Register Patrons
patron1 = Patron("Rahul", "P001")
patron2 = Patron("Sneha", "P002")

library.register_patron(patron1)
library.register_patron(patron2)

print()

# Borrow Books
library.borrow_book("P001", "101")
library.borrow_book("P002", "102")

print()

# Return Books
library.return_book("P001", "101")

print()

# Display Relevant Information
print("Library Books:")
for book in library.books:
    status = "Borrowed" if book.is_borrowed else "Available"
    print(f"{book.title} - {status}")

print("\nPatron Details:")
for patron in library.patrons:
    print(f"\nName: {patron.name}")
    print(f"ID: {patron.patron_id}")
    print("Borrowed Books:")
    if patron.borrowed_books:
        for book in patron.borrowed_books:
            print("-", book.title)
    else:
        print("None")