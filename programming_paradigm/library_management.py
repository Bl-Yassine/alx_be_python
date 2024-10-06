class Book:
    def __init__(self,title,author,_is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

class Library:
    def __init__(self,_books):
        self._books = _books

    def add_book(self,book):
        self._books.append(book)
    
    def check_out_book(self,book,title):
        self._books.remove(book[title])
    
    

    def list_available_books(self):
        print(f" {self._books}")