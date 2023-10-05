from sqlalchemy import select, update

from app.db.model import BookWord


class BookWordsRepository:
    def __init__(self, session):
        self.session = session

    def find_book_word(self, word, book):
        stmt = (select(BookWord)
                .where(BookWord.book_id == book.id, BookWord.word_id == word.id))
        return self.session.scalars(stmt).first()

    def increase_word_count(self, word, book):
        record = self.find_book_word(word, book)
        stmt = (update(BookWord)
                .where(BookWord.book_id == book.id, BookWord.word_id == word.id)
                .values(count=record.count + 1))
        self.session.execute(stmt)
        self.session.commit()
