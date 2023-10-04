from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_title: Mapped[str] = mapped_column(String(100))
    book_url: Mapped[str]

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, book_title={self.book_title!r}, book_url={self.book_url!r})"


class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(100))

    books: Mapped[List[Book]] = relationship(back_populates='book')

    def __repr__(self) -> str:
        return f"Word(id={self.id!r}, word={self.word!r})"

