class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
    
    def __len__(self):
        return self.pages
    
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python 101", 300)
book2 = Book("Advanced Python", 450)
print(book1)
print(f"Total pages: {book1 + book2}")
