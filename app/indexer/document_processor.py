import nltk
import requests

import app.db.postgres_book as book_db

import app.indexer.word_processor as word_processor


def locate_start_of_ebook(document):
    line = "*** START OF THE PROJECT GUTENBERG"
    line_index = str(document).find(line) + len(line)
    return str(document).find("***", line_index) + len("***")


def index_document(book_id):
    content = download_book(book_id)
    title = locate_title(content)
    db_book_id = book_db.insert_book(title, make_url_from_id(book_id))
    process_book(db_book_id, content)


def make_url_from_id(doc_id):
    return "https://www.gutenberg.org/cache/epub/" + str(doc_id) + "/pg" + str(doc_id) + ".txt"


def locate_title(document):
    title = "Title: "
    start_index = str(document).find(title) + len(title)
    end_index = str(document).find('\\', start_index)
    return str(document)[start_index:end_index]


def download_book(doc_id):
    return requests.get(make_url_from_id(doc_id)).content


def process_book(book_id, document):
    words = nltk.word_tokenize(str(document))
    for word in words:
        if word.isalpha():
            word_processor.insert_word_to_db(word_processor.change_word(word), book_id)
