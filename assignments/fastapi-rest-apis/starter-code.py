from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field
import uvicorn


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0)


class Book(BookCreate):
    id: int


app = FastAPI(title="Books API")
books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


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