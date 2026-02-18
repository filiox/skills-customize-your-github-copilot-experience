# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, production-ready REST APIs using the FastAPI framework. You'll practice creating endpoints, handling requests, implementing data validation, and working with databases.

## 📝 Tasks

### 🛠️ Create a Basic REST API

#### Description
Build a simple REST API with FastAPI that manages a list of books. Implement endpoints for creating, retrieving, and deleting books.

#### Requirements
Completed program should:

- Create a FastAPI application with a `/books` endpoint that returns a list of books
- Implement a POST endpoint to create new books with title, author, and year
- Implement a GET endpoint with path parameter to retrieve a specific book by ID
- Implement a DELETE endpoint to remove a book from the list
- Use Pydantic models for request/response validation


### 🛠️ Add Data Persistence and Error Handling

#### Description
Enhance the API with database integration and comprehensive error handling for a more robust application.

#### Requirements
Completed program should:

- Integrate a database (SQLite or similar) to persist book data
- Add proper HTTP status codes and error responses (404 for not found, 400 for bad requests)
- Implement input validation with meaningful error messages
- Add pagination to the book listing endpoint
- Include API documentation with descriptions for all endpoints
