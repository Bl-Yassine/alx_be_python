# Mastering Inheritance and Composition in Python

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size :{self.file_size}KB"

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, PAge Count: {self.page_count}"

class Library(Book,EBook,PrintBook):
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book) 

        if isinstance(book, EBook):
            self.books.append(book) 

        elif isinstance(book, PrintBook):
            self.books.append(book)      

        else:
            pass

    def list_books(self):
        for book in self.books:
            return book
                
                