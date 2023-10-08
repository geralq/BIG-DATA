from indexer import Indexer
from book_manager import BookManager
from api import API
from time import time

class Controller:
    def __init__(self, content_path, json_file_path):
        self.content_path = content_path
        self.json_file_path = json_file_path

    def run(self):

        start = time()
        idx = Indexer()
        bm = BookManager('datalake', 'metadata', 'content')

        bm.makedirs()
        bm.book_manager()
        idx.build_index(self.content_path)

        idx.save_index_to_json(self.json_file_path)

        end = time()

        print(f"Time taken: {end - start} seconds")
        
        app = API(self.json_file_path)
        app.run()