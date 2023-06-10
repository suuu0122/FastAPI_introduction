from fastapi import APIRouter
from typing import List
import api.schemas.task as task_schema


router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]

@router.get("/tasks")
async def create_tasks():
    pass

@router.post("/tasks")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass