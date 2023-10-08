from database_manager import DatabaseManager
from file_manager import FileManager
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
import os

class Indexer:
    
    dbm = DatabaseManager('database')
    fm = FileManager()

    def __init__(self, datalake_dir, content_dir):
        self.datalake_dir = datalake_dir
        self.content_dir = content_dir
        self.dictionary = dict()

    def inverted_index_of(self):
        files = [self.fm.join(self.datalake_dir, self.content_dir, file) 
                 for file in self.fm.listdir(self.fm.join(self.datalake_dir, self.content_dir))]
        
        for idx, file in enumerate(files):
            f, b = self.__read_file(file)
            self.dbm.insert_into_book_table(idx+1, b)
            self.__word_divider(f, idx+1)
        self.__insert_into_inverted_index_table(self.dictionary)

    def __read_file(self, filename):
        file = open(filename, 'r', encoding='utf-8')
        book = os.path.basename(filename).replace('.txt', '')
        file.close()
        return file, book
    
    def __word_divider(self, file, idx):
        file = open(file.name, 'r', encoding='utf-8')
        for line in file:
            words = re.findall(r'\b[a-zA-Z\']+\b', line)
            words = [word.lower() for word in words]
            self.__add_to_dictionary(idx, words)
        file.close()

    def __add_to_dictionary(self, idx, words):
        for word in words:
            if word not in stop_words:
                if word not in self.dictionary:
                    self.dictionary[word] = [idx]
                elif word in self.dictionary and idx not in self.dictionary[word]:
                    self.dictionary[word].append(idx)

    def __insert_into_inverted_index_table(self, dictionary):
        for word, book_id in dictionary.items():
            self.dbm.insert_into_inverted_index_table(word, book_id)
