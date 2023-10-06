import app.indexer.document_processor as dp
from app.db.in_memory_dictionary import InMemoryDictionary

if __name__ == "__main__":
    dictionary = InMemoryDictionary()
    dp = dp.DocumentProcessor(dictionary)

    dp.index_document(400)

    dictionary.save_dictionary()
    dictionary.print_dictionary()
