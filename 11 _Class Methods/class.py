# Class Methods:
class Book:
    total_books = 0  # Class variable to keep track of all books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increase count by 1

    def __init__(self):
        Book.increment_book_count()  # Automatically called when a new Book is created

b1 = Book()    
b2 = Book() 
b3 = Book()    
b4 = Book()  


print("Total books:", Book.total_books)
