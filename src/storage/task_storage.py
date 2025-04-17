from src.models.task import Task
from src.storage.storage import Storage


class TaskStorage(Storage):

    def __init__(self):
        self._tasks: list[Task] = []
        self._init_db()

    def _init_db(self):
        pass

    def save(self, task: Task):
        pass

    def load(self) -> list[Task] | None:
        pass
