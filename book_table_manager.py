import sqlite3


class BookTableManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_book_table(self):
        conn = sqlite3.connect(self.db_name + '.db')
        cursor = conn.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS book (
                book_id INTEGER,
                title TEXT
            )
        '''
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        
    def select_books_ids(self, word):
        conn = sqlite3.connect(self.db_name + '.db')
        cursor = conn.cursor()

        consult = f"SELECT book_id FROM inverted_index WHERE word = ?"
        cursor.execute(consult, (word,))
        books_id = [register[0] for register in cursor.fetchall()]
        conn.close()
        return eval(books_id[0])

    def select_book_title(self, books_ids):
        conn = sqlite3.connect(self.db_name + '.db')
        cursor = conn.cursor()
        titles = []

        for book_id in books_ids:
            consult = "SELECT title FROM book WHERE book_id = ?"
            cursor.execute(consult, (book_id,))
            result = cursor.fetchone()
            if result:
                titles.append(result[0])

        conn.close()
        return titles
    
    def insert_into_book_table(self, idx, title):
        conn = sqlite3.connect(self.db_name + '.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM book WHERE book_id = ?', (idx,))
        existing_entry = cursor.fetchone()

        if existing_entry is None:
            cursor.execute(f'INSERT INTO book (book_id, title) VALUES (?, ?)', (idx, title))

        conn.commit()
        conn.close()