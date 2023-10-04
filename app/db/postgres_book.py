import psycopg

from app.db.config import config


def insert_book(book_name, book_url):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO books (book_name, book_source) VALUES (%s, %s) RETURNING book_id", (book_name, book_url))
            return cur.fetchone()[0]


def read_all():
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books")
            return cur.fetchall()


def find_book_by_id(book_id):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books WHERE book_id = (%s)", (book_id,))
            return cur.fetchall()


def find_book_by_name(book_name):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books WHERE book_name = (%s)", (book_name,))
            return cur.fetchall()


def delete_book(book_id):
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM books WHERE book_id = (%s)", (book_id,))
