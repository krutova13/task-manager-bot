from __future__ import annotations
from src.models.task import Task, Status


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def get_status(self, task_id: int) -> Status | None:
        for task in self.tasks:
            if task.id == task_id:
                return task.status
        return None
