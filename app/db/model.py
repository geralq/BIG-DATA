from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey, Column, Integer, Table


class Base(DeclarativeBase):
    pass


class BookWord(Base):
    __tablename__ = "book_words"

    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    word_id = Column(Integer, ForeignKey('words.id'), primary_key=True)
    count = Column(Integer, default=1)


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    book_url: Mapped[str] = mapped_column(unique=True, nullable=False)


class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    books: Mapped[List["Book"]] = relationship(secondary="book_words")
