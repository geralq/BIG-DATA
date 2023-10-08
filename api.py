from database_manager import DatabaseManager
from flask import Flask, jsonify, request


app = Flask(__name__)
dbm = DatabaseManager('database')


@app.route('/api/search/<word>', methods=['GET'])
def get_books(word):
    try:
        books_ids = dbm.select_books_ids(word)
        books = dbm.select_book_title(books_ids)
        return jsonify({"books": books})
    except Exception as e:
        return jsonify({"books": []})

