import os

import nltk
import requests

import app.indexer.word_processor as word_processor
from app.repository.book_repository import BookRepository
from app.repository.bookwords_repository import BookWordsRepository
from app.repository.word_repository import WordRepository


class DocumentProcessor:

    def __init__(self, book_repository, word_repository, bookwords_repository):
        self.book_repository: BookRepository = book_repository
        self.word_repository: WordRepository = word_repository
        self.bookwords_repository: BookWordsRepository = bookwords_repository
        self.word_processor: word_processor.WordProcessor = word_processor.WordProcessor(book_repository, word_repository, bookwords_repository)

    def process_book(self, book, document):
        words = nltk.word_tokenize(str(document))
        for word in words:
            self.word_processor.insert_word_to_db(word, book)

    def index_documents(self, content_dir: dir):
        for file in os.listdir(content_dir):

            filename = os.path.join(content_dir, file)
            f = open(filename, "r")
            content = f.read()

            title, file_extension = os.path.splitext(file)
            if self.book_repository.find_book_by_title(title) is not None:
                print("Book with title=", title, " is already indexed.", sep='')
                return
            book = self.book_repository.add_book(title)

            self.process_book(book, content)
