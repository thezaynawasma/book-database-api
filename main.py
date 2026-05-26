from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Book schema
class Book(BaseModel):
    title: str
    author: str
    release_date: str
    genre: str
    isbn: str

# Fake database
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

# Home route
@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to the Book Database API"
    }

# Get all books
@app.get("/books", tags=["Books"])
def get_books():
    return books

# Get one book
@app.get("/books/{book_id}", tags=["Books"])
def get_book(book_id: int):

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

# Create a new book
@app.post(
    "/books",
    tags=["Books"],
    status_code=status.HTTP_201_CREATED
)
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

# Update a book
@app.put("/books/{book_id}", tags=["Books"])
def update_book(book_id: int, updated_book: Book):

    for book in books:
        if book["id"] == book_id:

            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["release_date"] = updated_book.release_date
            book["genre"] = updated_book.genre
            book["isbn"] = updated_book.isbn

            return {
                "message": "Book updated successfully",
                "book": book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

# Delete a book
@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: int):

    for book in books:
        if book["id"] == book_id:

            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )