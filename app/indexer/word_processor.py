import ssl

import nltk
from nltk.corpus import stopwords

from app.db.model import Book

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

prepositions = ["about", "above", "across", "after", "against", "along", "amid", "among", "around", "as", "at",
                "before", "behind", "below", "beneath", "beside", "between", "beyond", "but", "by", "concerning",
                "considering", "despite", "down", "during", "except", "for", "from", "in", "inside", "into", "like",
                "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "regarding", "round", "since",
                "through", "to", "toward", "under", "underneath", "until", "unto", "up", "upon", "with", "within",
                "without"]


class WordProcessor:

    def __init__(self, book_repository, word_repository, bookwords_repository):
        self.book_repository = book_repository
        self.word_repository = word_repository
        self.bookwords_repository = bookwords_repository

    @staticmethod
    def is_word_correct(word):
        return not (word in stop_words or word in prepositions or not word.isalpha())

    @staticmethod
    def change_word(word):
        return word.lower()

    def insert_word_to_db(self, word: str, book: Book):

        word = self.change_word(word)
        if not self.is_word_correct(word):
            return

        # Check if word is already in database
        word_entity = self.word_repository.find_word(word)

        # Word is not in the database
        if word_entity is None:
            self.word_repository.add_word_with_book(word, book)
            return

        # Word is in the database
        # Check if word is already assigned to the book
        if book not in word_entity.books:
            self.word_repository.add_book_to_word(word_entity, book)
        else:
            self.bookwords_repository.increase_word_count(word_entity, book)
