class User:

    total_users = 0

    def __init__(self, name):
        User.total_users += 1
        self.name = name
        self.user_id = f"USR-{User.total_users:05d}"
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False
        
    def list_borrowed_books(self):
        if self.borrowed_books:
            for i, book in enumerate(self.borrowed_books, start=1):
                print(f"{i}: {book.title}")
        else:
            print("No books borrowed.")

    def __str__(self):
        return(f"Name: {self.name}\nID: {self.user_id}\nBooks Borrowed: {len(self.borrowed_books)}")
    
    def __repr__(self):
        return (f"User(name={self.name!r}, user_id={self.user_id!r}, "
                f"borrowed_books={[book.title for book in self.borrowed_books]!r})")
