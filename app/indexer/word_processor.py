import nltk
import ssl
from nltk.corpus import stopwords

import app.db.postgres_word as word_db

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


def insert_word_to_db(word, book_id):

    # Check if word is already in database
    db_records = word_db.find_word_by_name(word)
    if len(db_records) == 0:
        word_id = word_db.insert_word(word)
    else:
        word_id = db_records[0][0]

    # Check if world is already assigned to the book
    if len(word_db.find_book_word(word_id, book_id)) == 0:
        word_db.add_book_to_word(word_id, book_id)


