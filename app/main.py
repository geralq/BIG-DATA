from sqlalchemy.orm import Session

from app.db import database
from app.db.model import Base
from app.indexer.document_processor import DocumentProcessor
from app.repository.book_repository import BookRepository
from app.repository.bookwords_repository import BookWordsRepository
from app.repository.word_repository import WordRepository

session = Session(database.engine)

book_repository = BookRepository(session)
word_repository = WordRepository(session)
bookwords_repository = BookWordsRepository(session)

if __name__ == "__main__":

    Base.metadata.create_all(database.engine)
    document_processor = DocumentProcessor(book_repository, word_repository, bookwords_repository)

    document_processor.index_document(500)
    document_processor.index_document(400)

    while True:
        word = input("Search for word: ")
        print(book_repository.find_books_from_word(word.lower()))
