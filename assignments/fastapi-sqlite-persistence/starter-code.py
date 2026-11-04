import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import uvicorn
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


DATABASE_PATH = Path(__file__).with_name("books.db")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0)


class Book(BookCreate):
    id: int


app = FastAPI(title="Books API with SQLite")


@contextmanager
def database_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def row_to_book(row: sqlite3.Row) -> Book:
    return Book(
        id=row["id"],
        title=row["title"],
        author=row["author"],
        year=row["year"],
    )


def initialize_database() -> None:
    with database_connection() as connection:
        raise NotImplementedError


@app.on_event("startup")
def startup() -> None:
    initialize_database()


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate) -> Book:
    raise NotImplementedError


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate) -> Book:
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)