class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"You have borrowed '{book.title}'.")
                return
        print(f"Sorry, '{title}' is not available in the library.")

    def return_book(self, book):
        self.books.append(book)
        print(f"Thank you for returning '{book.title}'.")

    def show_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are currently available.")


class User:
    def __init__(self, name):
        self.name = name

    def interact(self, library):
        while True:
            print("\nWelcome to the Library!")
            print("1. Add Book")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Show Available Books")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                library.add_book(Book(title, author))

            elif choice == "2":
                title = input("Enter the title of the book you want to borrow: ")
                library.borrow_book(title)

            elif choice == "3":
                title = input("Enter the title of the book you are returning: ")
                author = input("Enter the author of the book: ")
                library.return_book(Book(title, author))

            elif choice == "4":
                library.show_books()

            elif choice == "5":
                print("Thank you for using the Library Management System!")
                break

            else:
                print("Invalid choice. Please try again.")


# Main program
library = Library()
user = User("User")
user.interact(library)
