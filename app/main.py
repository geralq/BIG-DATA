from db.create_table import create_tables
from db.drop_table import drop_tables

import indexer.document_processor as document_processor

if __name__ == "__main__":
    try:
        drop_tables()
    except Exception as error:
        print(error)

    create_tables()

    document_processor.index_document(500)
