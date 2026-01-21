class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_borrowed = False
    
    def borrow_book(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self._is_borrowed = True
            print(f"You borrowed '{self.title}'.")

    def return_book(self):
        if not self._is_borrowed:
            print(f"'{self.title}' was not borrowed.")
        else:
            self._is_borrowed = False
            print(f"You returned '{self.title}'.")

    def __str__(self):
        status = "Yes" if self._is_borrowed == False else "No"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailable: {status}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, isbn={self.isbn!r}, is_borrowed={self.is_borrowed!r})"