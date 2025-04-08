from __future__ import annotations

from src.models.task import Task, Status


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def get_status(self, task_id: int) -> Status | None:
        for task in self.tasks:
            if task.id == task_id:
                return task.status
        return None
