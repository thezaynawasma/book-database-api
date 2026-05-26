from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    release_date: str
    genre: str
    isbn: str

books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "release_date": "1937-09-21",
        "genre": "Fantasy",
        "isbn": "9780547928227"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "release_date": "1949-06-08",
        "genre": "Dystopian",
        "isbn": "9780451524935"
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome to the Book Database API"
    }

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
def create_book(book: Book):

    new_book = {
        "id": len(books) + 1,
        **book.dict()
    }

    books.append(new_book)

    return {
        "message": "Book added successfully",
        "book": new_book
    }

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Book not found")