from __future__ import annotations

from datetime import date

from src.models.task import Task, Status


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def get_status(self, task_id: int) -> Status | None:
        for task in self.tasks:
            if task.id == task_id:
                return task.status
        return None

    def add_task(self, task: Task):
        self.tasks.append(task)

    def delete_task(self, task_id: int):
        found_task_counter = 0
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                found_task_counter += 1
        if found_task_counter == 0:
            print(f"Задачи с ID {task_id} нет в базе данных.")

    def sort_by_old(self):
        self.tasks.reverse()

    def filter_by_priority(self, filter: str):
        filtered_task_counter = 0
        filtered_database = []
        for task in self.tasks:
            if task.priority.name == filter:
                filtered_database.append(task)
                filtered_task_counter += 1
        if filtered_task_counter == 0:
            print(f"Задач с фильтром {filter} нет в базе данных.")
        else:
            print(filtered_database)

    def filter_by_status(self, filter: str):
        filtered_task_counter = 0
        filtered_database = []
        for task in self.tasks:
            if task.status.name == filter:
                filtered_database.append(task)
                filtered_task_counter += 1
        if filtered_task_counter == 0:
            print(f"Задач с фильтром {filter} нет в базе данных.")
        else:
            print(filtered_database)

    def filter_by_author(self, filter: str):
        filtered_task_counter = 0
        filtered_database = []
        for task in self.tasks:
            if str(task.author) == filter:
                filtered_database.append(task)
                filtered_task_counter += 1
        if filtered_task_counter == 0:
            print(f"Задач от автора {filter} нет в базе данных.")
        else:
            print(filtered_database)

    def filter_by_deadline(self, filter: date):
        filtered_task_counter = 0
        filtered_database = []
        for task in self.tasks:
            if task.deadline == filter:
                filtered_database.append(task)
                filtered_task_counter += 1
        if filtered_task_counter == 0:
            print(f"Задач с дедлайном {filter} нет в базе данных.")
        else:
            print(filtered_database)