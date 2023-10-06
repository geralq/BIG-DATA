import json

import jsonpickle

from app.indexer.model import Book, DictionaryEntry


class InMemoryDictionary:
    inverted_index = {}
    file_path = "data/inverted_index.json"

    def assign_book_to_word(self, word, book: Book):

        if self.is_book_associated_with_word(word, book):
            index = self.inverted_index[word].index(DictionaryEntry(book))
            self.inverted_index[word][index].count = self.inverted_index[word][index].count+1
            return
        else:
            entry = DictionaryEntry(book)
            self.inverted_index[word].append(entry)

    def is_book_associated_with_word(self, word: str, book: Book):
        if word not in self.inverted_index:
            return False
        return DictionaryEntry(book) in self.inverted_index[word]

    def add_word(self, word):
        self.inverted_index[word] = []

    def find_word(self, word):
        return self.inverted_index[word]

    def is_word_in_dictionary(self, word):
        return word in self.inverted_index

    def print_dictionary(self):
        for elem in self.inverted_index:
            print(elem, self.inverted_index[elem])

    def load_dictionary(self):
        with open(self.file_path, "r") as file:
            self.inverted_index = jsonpickle.decode(file.read())

    def save_dictionary(self):
        with open(self.file_path, "w") as file:
            file.write(jsonpickle.encode(self.inverted_index)
)
