from book_table_manager import BookTableManager
from inverted_index_table_manager import InvertedIndexTableManager


class DatabaseManager(BookTableManager, InvertedIndexTableManager):
    def __init__(self, db_name):
        self.db_name = db_name
        BookTableManager.__init__(self, db_name)
        InvertedIndexTableManager.__init__(self, db_name)