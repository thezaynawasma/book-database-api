# Book Database API

A simple REST API built with FastAPI for managing a book database.

## Features

- Get all books
- Get a single book
- Add a new book
- Update a book
- Delete a book

## Technologies Used

- Python
- FastAPI
- Uvicorn

## Installation

Clone the repository:

```bash
git clone <your-github-repo-link>
```

Open the project folder:

```bash
cd book-database-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /books | Get all books |
| GET | /books/{id} | Get one book |
| POST | /books | Add a new book |
| PUT | /books/{id} | Update a book |
| DELETE | /books/{id} | Delete a book |

## Notes

This project uses an in-memory Python list as a temporary database. Data resets when the server restarts.

## Author

Created as part of Backend Development Internship Project 1.