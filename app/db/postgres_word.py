from app.db.config import config

import psycopg


def read_all():
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM words")
            return cur.fetchall()


def insert_word(word_name):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO words (word_name) VALUES (%s) RETURNING word_id", (word_name,))
            return cur.fetchone()[0]


def add_book_to_word(word_id, book_id):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO words_books (word_id, book_id) VALUES (%s, %s)", (word_id, book_id,))


def find_book_word(word_id, book_id):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM words_books WHERE (word_id = %s AND book_id = %s)", (word_id, book_id,))
            return cur.fetchall()


def find_word_by_id(word_id):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM words WHERE word_id = (%s)", (word_id,))
            return cur.fetchall()


def find_word_by_name(word_name):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM words WHERE word_name = (%s)", (word_name,))
            return cur.fetchall()


def delete_word(word_id):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM words WHERE word_id = (%s)", (word_id,))
