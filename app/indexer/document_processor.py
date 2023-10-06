import nltk
import requests

import app.indexer.word_processor as word_processor


class DocumentProcessor:

    def __init__(self, book_repository, word_repository, bookwords_repository):
        self.book_repository = book_repository
        self.word_repository = word_repository
        self.bookwords_repository = bookwords_repository
        self.word_processor = word_processor.WordProcessor(book_repository, word_repository, bookwords_repository)

    @staticmethod
    def locate_start_of_ebook(document):
        line = "*** START OF THE PROJECT GUTENBERG"
        line_index = str(document).find(line) + len(line)
        return str(document).find("***", line_index) + len("***")

    @staticmethod
    def make_url_from_book_id(book_id):
        return "https://www.gutenberg.org/cache/epub/" + str(book_id) + "/pg" + str(book_id) + ".txt"

    @staticmethod
    def locate_title(document):
        title = "Title: "
        start_index = str(document).find(title) + len(title)
        end_index = str(document).find('\\', start_index)
        return str(document)[start_index:end_index]

    @staticmethod
    def download_book(url):
        return requests.get(url).content

    def process_book(self, book, document):
        words = nltk.word_tokenize(str(document))
        for word in words:
            self.word_processor.insert_word_to_db(word, book)

    def index_document(self, book_id):
        url = self.make_url_from_book_id(book_id)
        content = self.download_book(url)
        title = self.locate_title(content)

        book = self.book_repository.add_book(title, url)

        ebook = content[self.locate_start_of_ebook(content):]
        self.process_book(book, ebook)
