from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Table, ForeignKey, Column


class Base(DeclarativeBase):
    pass


association_table = Table(
    "book_word",
    Base.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("word_id", ForeignKey("words.id")),
)


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    book_url: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, book_title={self.book_title!r}, book_url={self.book_url!r})"


class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    books: Mapped[List["Book"]] = relationship(secondary=association_table)

    def __repr__(self) -> str:
        return f"Word(id={self.id!r}, word={self.word!r})"
