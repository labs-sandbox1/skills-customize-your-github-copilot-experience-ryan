"""
FastAPI REST API Starter Code
Build a Task Management API using FastAPI

To run this application:
1. Install FastAPI and uvicorn: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Visit http://localhost:8000/docs for interactive API documentation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create FastAPI app instance
app = FastAPI(title="Task Management API", version="1.0.0")

# Pydantic model for Task
class Task(BaseModel):
    """
    Task model with validation
    TODO: Add fields like title, description, completed status
    """
    id: int
    title: str
    # TODO: Add more fields here

# In-memory storage for tasks
tasks = [
    {"id": 1, "title": "Learn FastAPI", "description": "Complete the REST API assignment", "completed": False},
    {"id": 2, "title": "Build an API", "description": "Create a task management system", "completed": False}
]

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Task Management API"}

@app.get("/tasks")
def get_tasks():
    """
    Get all tasks
    TODO: Implement this endpoint to return all tasks
    BONUS: Add query parameter to filter by completed status
    """
    pass

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """
    Get a single task by ID
    TODO: Implement this endpoint to return a specific task
    - Return 404 if task not found
    """
    pass

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    """
    Create a new task
    TODO: Implement this endpoint to create a new task
    - Add the task to the tasks list
    - Return the created task
    """
    pass

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    """
    Update an existing task
    TODO: Implement this endpoint to update a task
    - Find the task by ID
    - Update its properties
    - Return 404 if task not found
    """
    pass

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """
    Delete a task
    TODO: Implement this endpoint to delete a task
    - Remove the task from the list
    - Return 404 if task not found
    - Return 204 status code on success
    """
    pass
