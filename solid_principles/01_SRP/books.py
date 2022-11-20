class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, name):
        self.name = name
        self.books =[]
    def add_book(self, book:Book):
        self.books.append(book)
    def location(self,book):
        if book in self.books:
            return "Book is in the library."

book1 = Book('Lord of the Rings', 'JJ Tolkin')
book2 = Book('Leonardos sypher', 'Dan Braun')

city_library = Library('Ivan Vazov')
city_library.add_book(book1)
city_library.add_book(book2)
print(city_library.location(book1))
