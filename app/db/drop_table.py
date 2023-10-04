import psycopg

from app.db.config import config

commands = ("""DROP TABLE words CASCADE """,
            """DROP TABLE books CASCADE """,
            """DROP TABLE words_books CASCADE """)


def drop_tables():
    params = config()
    with psycopg.connect(**params) as conn:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
