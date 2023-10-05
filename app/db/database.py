import configparser

from sqlalchemy import URL
from sqlalchemy import create_engine, select, update

from app.db.model import Book, Word, BookWord

config = configparser.ConfigParser()
config.read("app/db/database.ini")

url_object = URL.create(
    "postgresql",
    username=config["postgresql"]["user"],
    password=config["postgresql"]["password"],
    host=config["postgresql"]["host"],
    port=int(config["postgresql"]["port"]),
    database=config["postgresql"]["dbname"])

engine = create_engine(url_object)


def find_book_by_title(session, title):
    stmt = select(Book).where(Book.book_title == title)
    return session.scalars(stmt).first()


def add_book(session, title, url):
    book = Book(book_title=title, book_url=url)
    session.add(book)
    session.commit()
    return book


def find_word(session, word):
    stmt = select(Word).where(Word.word == word)
    return session.scalars(stmt).first()


def add_word(session, word):
    word = Word(word=word)
    session.add(word)
    session.commit()
    return word


def find_book_by_id(session, id):
    stmt = select(Book).where(Book.id == id)
    return session.scalars(stmt).first()


def find_books_from_word(session, word):
    stmt = select(Word).where(Word.word == word)
    word = session.scalars(stmt).first()
    if word is None:
        return None
    return word.books


def find_book_word(session, word, book):
    stmt = select(BookWord).where(BookWord.book_id == book.id, BookWord.word_id == word.id)
    return session.scalars(stmt).first()


def increase_count(session, word, book):
    record = find_book_word(session, word, book)
    stmt = (
        update(BookWord).
        where(BookWord.book_id == book.id, BookWord.word_id == word.id).
        values(count=record.count + 1))
    session.execute(stmt)
    session.commit()
