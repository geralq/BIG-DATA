class Book:

    def __init__(self, name, url):
        self.name: str = name
        self.url: str = url

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.url == other.url


class DictionaryEntry:

    def __init__(self, book: Book):
        self.book: Book = book
        self.count: int = 1

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        if self.book == other.book:
            return True

    def __repr__(self) -> str:
        return str(self.count) + "x " + str(self.book.name)


