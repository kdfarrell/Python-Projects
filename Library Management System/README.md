# Library Management System

## Project Complete Overview

The **Library Management System** is a fully implemented, console-based Python application that allows users to manage books and borrow/return them in a simulated library environment. The project is designed to showcase Python fundamentals along with **Object-Oriented Programming (OOP) principles**.

This version includes:

- A **Book class** representing individual books
- A **User class** for library patrons
- A **Library class** to manage book collections and track borrow/return activity
- Preloaded **sample productivity books** for immediate interaction
- Full error handling and validation for real-world scenarios


## Project Features

### Book Class

- Attributes: `title`, `author`, `isbn`, `is_borrowed`
- Methods: `borrow()`, `return_book()`, `__str__()`
- Prevents double borrowing and displays user-friendly book info

### User Class

- Attributes: `name`, `user_id`, `borrowed_books`
- Methods: `borrow_book(book)`, `return_book(book)`, `list_borrowed_books()`
- Tracks all books borrowed by a user

### Library Class

- Manages book collection using ISBN as a unique key
- Methods: `add_book(book)`, `remove_book(isbn)`, `borrow_book(isbn)`, `return_book(isbn)`, `list_available_books()`
- Handles invalid ISBNs and prevents duplicate entries

## How to Run

1. Ensure Python 3 is installed
2. Clone or download the project
3. Navigate to the project directory
4. Run the program:

```bash
python main.py
```
