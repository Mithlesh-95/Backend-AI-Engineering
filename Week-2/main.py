from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks_list = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build first API", "done": False},
    {"id": 3, "title": "Test the endpoints", "done": True},
]

@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
async def health():
    return {"Status" : "ok"}

@app.get("/tasks")
async def tasks():
    return tasks_list

@app.get("/tasks/{id}")
async def get_tasks(id: int):
    for task in tasks_list:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

from pydantic import BaseModel

class Task(BaseModel):
    title: str

@app.post("/tasks", status_code=201)
async def add_task(task: Task):

    if task.title.strip() == "string" or task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks_list) + 1,
        "title": task.title,
        "done": False
    }

    tasks_list.append(new_task)

    return {
        "message": "Task added successfully",
        "task": new_task
    }

