import app.indexer.document_processor as dp
from app.db.in_memory_dictionary import InMemoryDictionary

if __name__ == "__main__":
    dictionary = InMemoryDictionary()
    dp = dp.DocumentProcessor(dictionary)
    dp.index_document(400)
    dp.index_document(300)
    dp.index_document(500)
    dictionary.save_dictionary()

    while True:
        query = input("Search for word: ")
        print( dictionary.find_word(query))
