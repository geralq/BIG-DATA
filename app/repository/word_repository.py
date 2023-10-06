from sqlalchemy import select

from app.db.model import Word


class WordRepository:

    def __init__(self, session):
        self.session = session

    def find_word(self, word: str):
        stmt = select(Word).where(Word.word == word)
        return self.session.scalars(stmt).first()

    def add_word(self, word_str):
        word = Word(word=word_str)
        self.session.add(word)
        self.session.commit()
        return word

    def add_word_with_book(self, word_str, book):
        word = self.add_word(word_str)
        word.books.append(book)
        self.session.commit()
        return word

    def add_book_to_word(self, word, book):
        word_db = self.session.get(Word, word.id)
        word_db.books.append(book)
        self.session.commit()
        return word_db
