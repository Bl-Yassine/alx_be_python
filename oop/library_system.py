# Mastering Inheritance and Composition in Python

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count = page_count

class Library(Book,EBook,PrintBook):
    def __init__(self):
        self._books = []

    def add_book(self,title,author,page_count,file_size,book):
        super().__init__(title,author,page_count,file_size)
        self._books.append(book)
    
    def list_books(self):
        print(f"the list books : {self._books}")
