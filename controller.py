from indexer import Indexer
from database_manager import DatabaseManager
from book_manager import BookManager
from api import app

class Controller:
    def __init__(self):
        pass

    def controller(self):
        dbm = DatabaseManager('database')
        idx = Indexer('datalake', 'content')
        mcm = BookManager('datalake', 'metadata', 'content')

        dbm.create_book_table()
        dbm.create_inverted_index_table()

        mcm.makedirs()
        mcm.book_manager()
        idx.inverted_index_of()
        
        app.run(debug=True)
