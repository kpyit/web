from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Task(BaseModel):
    id: int 
    title: str
    description: Optional[str] = None       # опциональные поля
    completed: Optional[bool] = False       #не завершена по умолчанию

tasks = []


@app.get("/")
async def root():
    return {"message":"api status up"}

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task.model_dump())
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    task_index = next((index for index, t in enumerate(tasks) if t['id'] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_index] = task.model_dump()
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task_index = next((index for index, task in enumerate(tasks) if task['id'] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks.pop(task_index)
    return deleted_task

# Запуск в окружении и в каталоге  uvicorn main_01:app --reload
# Документация
# http://127.0.0.1:8000/docs 
# http://127.0.0.1:8000/redoc#operation/root__get