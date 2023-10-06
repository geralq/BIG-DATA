import ssl

import nltk
from nltk.corpus import stopwords

from app.db.in_memory_dictionary import InMemoryDictionary
from app.indexer.model import Book

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

    def __init__(self, in_memory_dictionary: InMemoryDictionary):
        self.dictionary = in_memory_dictionary

    @staticmethod
    def is_word_correct(word):
        return not (word in stop_words or word in prepositions)

    @staticmethod
    def change_word(word):
        return word.lower()

    def insert_word_to_db(self, word: str, book: Book):

        word = self.change_word(word)

        if not word.isalpha() or word in prepositions or word in stop_words:
            return

        if not self.dictionary.is_word_in_dictionary(word):
            self.dictionary.add_word(word)
        self.dictionary.assign_book_to_word(word, book)
