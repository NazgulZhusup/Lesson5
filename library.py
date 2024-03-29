# Создайте класс Book с атрибутами title, author, и isbn.
# Создайте класс Library, который будет управлять коллекцией книг. Внутри Library используйте словарь или список для хранения книг.
# Реализуйте методы для добавления книг в библиотеку, удаления книг по ISBN и поиска книг по автору.
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book_by_isbn(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

# Пример использования
library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789"))
library.add_book(Book("Moby Dick", "Herman Melville", "987654321"))
library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "123123123"))

print("Библиотека после добавления книг:")
for book in library.books:
    print(book)

library.remove_book_by_isbn("987654321")
print("\nБиблиотека после удаления книги по ISBN:")
for book in library.books:
    print(book)

print("\nПоиск книг по автору 'F. Scott Fitzgerald':")
for book in library.find_books_by_author("F. Scott Fitzgerald"):
    print(book)
