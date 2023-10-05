from sqlalchemy.orm import Session

from app.db import database
from app.db.model import Base
from app.indexer.document_processor import index_document

if __name__ == "__main__":

    Base.metadata.drop_all(database.engine)
    Base.metadata.create_all(database.engine)

    index_document(500)

    while True:
        word = input("Word to search for: ")
        print(database.find_books_from_word(Session(database.engine), word))
