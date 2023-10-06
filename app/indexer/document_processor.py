import re

import nltk
import requests

import app.indexer.word_processor as word_processor
from app.indexer.model import Book


class DocumentProcessor:

    def __init__(self, in_memory_dictionary):
        self.dictionary = in_memory_dictionary
        self.word_processor = word_processor.WordProcessor(in_memory_dictionary)

    @staticmethod
    def locate_start_of_ebook(document):
        return re.search("\*\*\* .*? \*\*\*", str(document)).end()

    @staticmethod
    def remove_meta_data(document):
        return str(document)[DocumentProcessor.locate_start_of_ebook(document):]

    @staticmethod
    def make_url_from_id(doc_id):
        return "https://www.gutenberg.org/cache/epub/" + str(doc_id) + "/pg" + str(doc_id) + ".txt"

    @staticmethod
    def locate_title(document):
        title = "Title: "
        start_index = str(document).find(title) + len(title)
        end_index = str(document).find('\\', start_index)
        return str(document)[start_index:end_index]

    @staticmethod
    def download_book(doc_id):
        return requests.get(DocumentProcessor.make_url_from_id(doc_id)).content

    def index_document(self, book_id):
        content = self.download_book(book_id)
        title = self.locate_title(content)
        url = self.make_url_from_id(book_id)

        book = Book(title, url)

        self.process_book(book, content)

    def process_book(self, book: Book, document: bytes):
        words = nltk.word_tokenize(str(document))
        for word in words:
            self.word_processor.insert_word_to_db(word, book)
