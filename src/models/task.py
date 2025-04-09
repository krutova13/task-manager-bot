from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()


@dataclass  # TODO: заменить на Pydantic
class Task:
    id: int
    name: str
    priority: Priority
    deadline: datetime
    author: str
    description: str
    theme: str  # TODO: стоит использовать enum в будущем
    owner_id: int
    status: Status = Status.NEW
    creation_date: datetime = datetime.now()
