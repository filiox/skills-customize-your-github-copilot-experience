from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# Define a Pydantic model for Book
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int

# In-memory storage for books (replace with database later)
books_db: List[Book] = [
    Book(id=1, title="Python Basics", author="John Doe", year=2023),
    Book(id=2, title="Web Development", author="Jane Smith", year=2024),
]

# TODO: Implement GET /books endpoint to retrieve all books

# TODO: Implement POST /books endpoint to create a new book

# TODO: Implement GET /books/{book_id} endpoint to retrieve a specific book

# TODO: Implement DELETE /books/{book_id} endpoint to delete a book

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
