import psycopg

from app.db.config import config

commands = ("""
    CREATE TABLE IF NOT EXISTS books (
    book_id SERIAL PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL UNIQUE ,
    book_source VARCHAR(255) NOT NULL UNIQUE )
    """,

            """CREATE TABLE IF NOT EXISTS words (
            word_id SERIAL PRIMARY KEY,
            word_name VARCHAR(255) NOT NULL UNIQUE )
            """,

            """CREATE TABLE IF NOT EXISTS words_books (
            word_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            PRIMARY KEY (word_id, book_id),
            FOREIGN KEY (word_id)
                REFERENCES words (word_id),
            FOREIGN KEY (book_id)
                REFERENCES books (book_id))
            """)


def create_tables():
    params = config()
    print('Connecting to the PostgreSQL database...')
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
    print('Database connection closed.')
