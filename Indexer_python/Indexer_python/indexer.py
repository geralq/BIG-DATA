import string
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from file_manager import FileManager
import re
import json

nltk.download('stopwords')
class Indexer:
    def __init__(self):
        self.contents = {}
        self.dictionary = defaultdict(lambda: defaultdict(int))
        self.fm = FileManager()

    def __read_contents(self, folder_path):
        for file_name in self.fm.listdir(folder_path):
            if file_name.endswith(".txt"):
                file_name_without_extension = re.sub(r'\.txt$', '', file_name)
                file_path = self.fm.join(folder_path, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.contents[file_name_without_extension] = content

    def __tokenize_and_filter_words(self, text):
        text_without_punctuations = text.replace(".", "").replace('"', '').replace("'", "")
        words = nltk.word_tokenize(text_without_punctuations, language='english')
        stop_words = set(stopwords.words('english'))
        filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]
        cleaned_text = ' '.join(filtered_words)
        return cleaned_text

    def __process_file(self, content):
        cleaned_text = self.__tokenize_and_filter_words(content)
        words = cleaned_text.split()
        return words

    def build_index(self, folder_path):
        self.__read_contents(folder_path)
        for file_name, content in self.contents.items():
            words = self.__process_file(content)
            for word in words:
                self.dictionary[word][file_name] += 1

    
    def save_dictionary(self, json_file_path):
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.dictionary, json_file)

    def load_dictionary(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            self.dictionary = json.load(json_file)

    
    def search_word_in_dictionary(self, word):
        w = word.lower()
        frequencies = self.dictionary.get(w, None)
        if frequencies:
            sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
            file_names = [file_name for file_name in sorted_frequencies]
            return file_names
        return None


