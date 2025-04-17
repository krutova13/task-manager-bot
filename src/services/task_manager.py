from __future__ import annotations

from src.models.task import Task, Status
from src.storage.storage import Storage


class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage

    def add_task(self, task: Task):
        self.storage.save(task)

    def get_tasks(self) -> list[Task]:
        return self.storage.load()

    def get_status(self, task_id: int) -> Status | None:
        for task in self.storage.load():
            if task.id == task_id:
                return task.status
        return None
