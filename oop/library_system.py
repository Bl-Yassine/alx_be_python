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
        self.books = []

    def add_book(self,title,author,page_count,file_size,book):
        super().__init__(title,author,page_count,file_size)
        book_info = {
            "title" : title,
            "author" : author,
            "file_size" : file_size,
            "page" : page_count,
        }
        self.books.append(book_info)
    
    def list_books(self):
        def __str__(self):
            return f"the list books : {self.books}"
