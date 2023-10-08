from flask import Flask, jsonify
from indexer import Indexer

class API:
    def __init__(self, index_file_path):
        self.app = Flask(__name__)
        self.idx = Indexer()
        self.idx.load_index_from_json(index_file_path)

        @self.app.route('/api/search/<word>', methods=['GET'])
        def get_word(word):
            books = self.idx.search_word_in_dictionary(word)
            return jsonify({"books": books})

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    index_file_path = 'index.json'
    app = API(index_file_path)
    app.run()
