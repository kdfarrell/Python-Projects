import json
from book import Book
from user import User
from library import Library

def load_books_from_json(filepath, library):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            for item in data:
                library.add_book(Book(item["title"], item["author"], item["isbn"]))
    except FileNotFoundError:
        print(f"{filepath} not found. No books loaded.")
    except json.JSONDecodeError:
        print(f"Error reading {filepath}. Make sure it's valid JSON.")

def main():
    library = Library()
    
    # Load books from JSON
    load_books_from_json("books.json", library)

    # Add a sample user for testing
    user = User("Alice")
    library.add_user(user)

    while True:
        print("\n--- Library Menu ---")
        print("1. List available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add new book")
        print("5. Remove a book")
        print("6. List users")
        print("7. Add new user")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.list_available_books()
        elif choice == "2":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(user_id, isbn)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN to return: ")
            library.return_book(user_id, isbn)
        elif choice == "4":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, isbn))
        elif choice == "5":
            isbn = input("Enter ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == "6":
            library.list_users()
        elif choice == "7":
            name = input("Enter user name: ")
            library.add_user(User(name))


if __name__ == "__main__":
    main();