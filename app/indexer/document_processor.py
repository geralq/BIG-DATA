import nltk
import requests
import psycopg2

from sqlalchemy.orm import Session


import app.indexer.word_processor as word_processor
from app.db import database


def locate_start_of_ebook(document):
    line = "*** START OF THE PROJECT GUTENBERG"
    line_index = str(document).find(line) + len(line)
    return str(document).find("***", line_index) + len("***")


def index_document(book_id):
    with Session(database.engine) as session:
        content = download_book(book_id)
        try:
            book = database.add_book(session, locate_title(content), make_url_from_id(book_id))
        except Exception as ex:
            print(ex)
            return
        content = content[locate_start_of_ebook(content):]
        process_book(session, book, content)


def make_url_from_id(doc_id):
    return "https://www.gutenberg.org/cache/epub/" + str(doc_id) + "/pg" + str(doc_id) + ".txt"


def locate_title(document):
    title = "Title: "
    start_index = str(document).find(title) + len(title)
    end_index = str(document).find('\\', start_index)
    return str(document)[start_index:end_index]


def download_book(doc_id):
    return requests.get(make_url_from_id(doc_id)).content


def process_book(session, book, document):
    words = nltk.word_tokenize(str(document))
    for word in words:
        word = word_processor.change_word(word)
        if word.isalpha() and word_processor.is_word_correct(word):
            word_processor.insert_word_to_db(session, word, book)
