# Mastering Inheritance and Composition in Python

class Book:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book : {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size
        print(f"EBook: {title} by {author}, File Size :{file_size}KB")
        pass

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count = page_count
        print(f"PrintBook: {title} by {self.author}, PAge Count: {page_count}")
        pass
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
