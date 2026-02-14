# library.py

from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = {}  # ISBN as key
        self.users = {}  # user_id as key

    def add_book(self, book):
        if book.isbn in self.books:
            print("Book with this ISBN already exists.")
            return False
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added successfully.")
        return True

    def remove_book(self, isbn):
        if isbn in self.books:
            removed = self.books.pop(isbn)
            print(f"Book '{removed.title}' removed successfully.")
            return True
        print("Invalid ISBN. No book removed.")
        return False

    def list_available_books(self):
        available_books = [book for book in self.books.values() if not book.is_borrowed]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(book)
                print("-" * 30)

    def borrow_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = self.books.get(isbn)
        if not user:
            print("Invalid user ID.")
            return False
        if not book:
            print("Invalid ISBN.")
            return False
        if user.borrow_book(book):
            print(f"{user.name} successfully borrowed '{book.title}'.")
            return True
        print(f"Book '{book.title}' is already borrowed.")
        return False

    def return_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = self.books.get(isbn)
        if not user or not book:
            print("Invalid user ID or ISBN.")
            return False
        if user.return_book(book):
            print(f"{user.name} successfully returned '{book.title}'.")
            return True
        print(f"Book '{book.title}' was not borrowed by {user.name}.")
        return False

    def add_user(self, user):
        if user.user_id in self.users:
            print("User already exists.")
            return False
        self.users[user.user_id] = user
        print(f"User '{user.name}' added successfully with ID {user.user_id}.")
        return True

    def list_users(self):
        if not self.users:
            print("No users registered.")
        else:
            for user in self.users.values():
                print(user)
                print("-" * 30)
