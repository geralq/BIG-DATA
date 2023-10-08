import sqlite3


class InvertedIndexTableManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_inverted_index_table(self):
        conn = sqlite3.connect(self.db_name + '.db')
        cursor = conn.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS inverted_index (
                word TEXT,
                book_id TEXT
            )
        '''
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()

    def insert_into_inverted_index_table(self, word, book_id):
        conn = sqlite3.connect(self.db_name + '.db')
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM inverted_index WHERE word = ? AND book_id = ?', (word, str(book_id)))
        existing_entry = cursor.fetchone()

        if existing_entry is None:
            cursor.execute(f'INSERT INTO inverted_index (word, book_id) VALUES (?, ?)', (word, str(book_id)))

        conn.commit()
        conn.close()