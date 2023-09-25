from collections import defaultdict


def inverted_index_of(document_list):
    dictionary = defaultdict(list)

    for document in document_list:
        word_split(document, dictionary)

    return dictionary


# 1. remove meta-data from book
# 2. Create the indexer
# 2.1 Read the book
#
#
# Create dictionary


# FOR EVERY LINE IN DOCUMENT:
# remove all symbols expect A-Z, a-z, and spaces
#
#

# FOR EVERY WORD IN LINE:
# isItWord (word) -> bool
# isPreposition (word) -> bool
# isInDictionary (word) -> bool
# insertWordToDict (docName, word, dict) -> dict


def word_split(filename, dictionary):
    file = open(filename, 'r', encoding='utf-8')
    for line in file:
        words = line.split()
        for word in words:
            insert_word_to_dict(filename, word, dictionary)


def check_word(word):
    # TODO: check if correct word
    # TODO: check if it is preposition
    # TODO: check if it already in dictionary
    return True


def change_word(word):
    return word.lower()


def insert_word_to_dict(filename, word, dictionary):
    if check_word(word):

        if not dictionary[change_word(word)].__contains__( filename ):
            dictionary[change_word(word)].append( filename )

    return dictionary


document_list = ["datalake/test.txt"]

my_dict = inverted_index_of(document_list)

print(my_dict)
