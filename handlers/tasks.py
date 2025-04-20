from typing import List

from fastapi import APIRouter, status
from schema.task_schema import Task
from fixtures import tasks as fixture_tasks

router = APIRouter(
    prefix="/task",
    tags=["task"],
)


@router.get(
    "/all",
    response_model=List[Task],
)
async def get_tasks():
    return fixture_tasks


@router.post(
    "/",
    response_model=Task,
)
async def create_task(task: Task):
    fixture_tasks.append(task)
    return task


@router.patch(
    "/{task_id}",
    response_model=Task,
)
async def update_task(task_id: int, name: str):
    for task in fixture_tasks:
        if task["id"] == task_id:
            task["name"] = name
            return task
        return None
    return None


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(task_id: int,):
    for index, task in enumerate(fixture_tasks):
        if task["id"] == task_id:
            del fixture_tasks[index]
            return {"message": "task deleted"}
    return {"message": "task not found"}