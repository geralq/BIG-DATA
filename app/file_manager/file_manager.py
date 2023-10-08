import os
import re

import requests


class FileManager:

    def __init__(self, document_dir):
        self.document_dir = document_dir

        self.metadata_dir = os.path.join(document_dir, "metadata")
        self.content_dir = os.path.join(document_dir, "content")

        self.make_directory(self.metadata_dir)
        self.make_directory(self.content_dir)

    def download_book(self, book_id: int):
        data = requests.get(self.make_url_from_id(book_id)).content

        file_name = FileManager.sanitize_file_name(self.get_title(data))

        self.separate_metadata(data, file_name)
        self.separate_content(data, file_name)

    @staticmethod
    def sanitize_file_name(file_name):
        invalid_chars = '\\/:*?"<>|'
        for char in invalid_chars:
            file_name = file_name.replace(char, '-')
        file_name = file_name.strip().rstrip('.')
        return file_name

    def separate_metadata(self, document, name):
        metadata = FileManager.get_metadata(document)
        FileManager.write_file(os.path.join(self.metadata_dir, name + ".txt"), metadata)

    def separate_content(self, document, name):
        content = FileManager.get_content(document)
        FileManager.write_file(os.path.join(self.content_dir, name + ".txt"), content)

    @staticmethod
    def make_url_from_id(doc_id):
        return "https://www.gutenberg.org/cache/epub/" + str(doc_id) + "/pg" + str(doc_id) + ".txt"

    @staticmethod
    def get_metadata(document: bytes):
        match = "***"
        index = str(document).find(match) - len(match)
        return str(document)[:index]

    @staticmethod
    def get_content(document: bytes):
        start_of_content = FileManager.locate_start_of_content(document)
        return str(document)[start_of_content:]

    @staticmethod
    def get_title(document):
        title = "Title: "
        start_index = str(document).find(title) + len(title)
        end_index = str(document).find('\\', start_index)
        return str(document)[start_index:end_index]

    @staticmethod
    def write_file(file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    @staticmethod
    def locate_start_of_content(document: bytes):
        return re.search("\*\*\* .*? \*\*\*", str(document)).end()

    @staticmethod
    def make_directory(directory):
        os.makedirs(directory, exist_ok=True)
