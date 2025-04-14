from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

    def __str__(self):
        priority = {
            Priority.LOW: "Низкий",
            Priority.MEDIUM: "Средний",
            Priority.HIGH: "Высокий"
        }
        return priority[self]


class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()

    def __str__(self):
        status = {
            Status.NEW: "Новая",
            Status.IN_PROGRESS: "В работе",
            Status.DONE: "Готово"
        }
        return status[self]

@dataclass  # TODO: заменить на Pydantic
class Task:
    def __str__(self) -> str:
        return (f"Задача\n"
                f"Идентификатор: {self.id}\n"
                f"Название: {self.name}\n"
                f"Приоритет: {self.priority}\n"
                f"Крайний срок: {self.deadline}\n"
                f"Автор: {self.author}\n"
                f"Описание: {self.description}\n"
                f"Тема: {self.theme}\n"
                f"Идентификатор автора: {self.owner_id}\n"
                f"Статус: {self.status}\n"
                f"Дата создания: {self.creation_date}")

    id: int
    name: str
    priority: Priority
    deadline: datetime.date
    author: str
    description: str
    theme: str  # TODO: стоит использовать enum в будущем
    owner_id: int
    status: Status = Status
    creation_date: datetime = datetime.now()


