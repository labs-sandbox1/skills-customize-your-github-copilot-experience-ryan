# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. Understand HTTP methods, routing, request validation, and automatic API documentation while creating a fully functional API.

## 📝 Tasks

### 🛠️	Build a Task Management API

#### Description
Create a REST API for managing tasks using FastAPI. The API should support creating, reading, updating, and deleting tasks with proper validation and error handling.

#### Requirements
Completed program should:

- Use FastAPI framework to create API endpoints
- Implement GET endpoint to retrieve all tasks
- Implement GET endpoint to retrieve a single task by ID
- Implement POST endpoint to create new tasks with validation
- Implement PUT endpoint to update existing tasks
- Implement DELETE endpoint to remove tasks
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper error handling for invalid requests


### 🛠️	Test and Document Your API

#### Description
Test your API endpoints using FastAPI's automatic interactive documentation and verify all functionality works correctly.

#### Requirements
Completed program should:

- Run the FastAPI server successfully using uvicorn
- Access the automatic API docs at `/docs` endpoint
- Successfully test all CRUD operations through the docs interface
- Validate that Pydantic models enforce data types correctly
- Handle edge cases like missing tasks or invalid data
- Include at least one query parameter (e.g., filter by status)
