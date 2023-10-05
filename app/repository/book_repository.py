from sqlalchemy import select

from app.db.model import Book, Word


class BookRepository:
    def __init__(self, session):
        self.session = session

    def add_book(self, title, url):
        book = Book(book_title=title, book_url=url)
        self.session.add(book)
        self.session.commit()
        return book

    def find_book_by_id(self, id):
        stmt = select(Book).where(Book.id == id)
        return self.session.scalars(stmt).first()

    def find_books_from_word(self, word):
        stmt = select(Word).where(Word.word == word)
        word = self.session.scalars(stmt).first()
        if word is None:
            return None
        return word.books

    def find_book_by_title(self, title):
        stmt = select(Book).where(Book.book_title == title)
        return self.session.scalars(stmt).first()
