import ssl
from collections import defaultdict

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

prepositions = ["about", "above", "across", "after", "against", "along", "amid", "among", "around", "as", "at",
                "before", "behind", "below", "beneath", "beside", "between", "beyond", "but", "by", "concerning",
                "considering", "despite", "down", "during", "except", "for", "from", "in", "inside", "into", "like",
                "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "regarding", "round", "since",
                "through", "to", "toward", "under", "underneath", "until", "unto", "up", "upon", "with", "within",
                "without"]


def inverted_index_of(datalake):
    dictionary = defaultdict(list)

    for document in datalake:
        word_split(document, dictionary)

    return dictionary


def word_split(filename, dictionary):
    file = open(filename, 'r', encoding='utf-8')
    for line in file:
        words = nltk.tokenize.sent_tokenize(line, language='english')
        for word in words:
            word = change_word(word)
            insert_word_to_dict(filename, word, dictionary)


def check_word(word, dictionary):
    if word in stop_words:
        return False
    elif word in dictionary:
        return False
    return True


def change_word(word):
    return word.lower()


def insert_word_to_dict(filename, word, dictionary):
    if check_word(word, dictionary):

        if not dictionary[word].__contains__(filename):
            dictionary[word].append(filename)

    return dictionary


document_list = ["datalake/test.txt"]

my_dict = inverted_index_of(document_list)

print(my_dict)
