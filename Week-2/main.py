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
