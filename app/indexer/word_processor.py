import ssl

import nltk
from nltk.corpus import stopwords

from app.db import database

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


def is_word_correct(word):
    return not (word in stop_words or word in prepositions)


def change_word(word):
    return word.lower()


def insert_word_to_db(session, word, book):
    # Check if word is already in database
    word_entity = database.find_word(session, word)

    # Word is not in the database
    if word_entity is None:
        word_entity = database.add_word(session, word)
        word_entity.books.append(book)
        session.commit()
        return

    # Word is in the database
    # Check if word is already assigned to the book
    if book not in word_entity.books:
        word_entity.books.append(book)
    else:
        database.increase_count(session, word_entity, book)
