from datetime import datetime, date

from src.models.task import Task, Priority, Status
from src.services.task_manager import TaskManager

task1 = Task(
    id=1,
    name="Создать 10 тасок",
    priority=Priority.HIGH,
    deadline=date(2025, 4, 9),
    author="Алтынников",
    description="Написать задачи для Обучения и развития своих навыков",
    theme="Обучение Python",
    owner_id=34,
    status=Status.NEW,
    creation_date=datetime.now()
)

task2 = Task(
    id=2,
    name="Создать 20 тасок",
    priority=Priority.MEDIUM,
    deadline=date(2025, 3, 8),
    author="Гребенюк",
    description="Написать задачи для Обучения и развития своих навыков",
    theme="Обучение Python",
    owner_id=33,
    status=Status.IN_PROGRESS,
    creation_date=datetime.now()
)

task3 = Task(
    id=3,
    name="Создать 30 тасок",
    priority=Priority.LOW,
    deadline=date(2025, 10, 10),
    author="Артемова",
    description="Написать задачи для Обучения и развития своих навыков",
    theme="Обучение Python",
    owner_id=1,
    status=Status.DONE,
    creation_date=datetime.now()
)

manager = TaskManager()

manager.add_task(task1)
manager.add_task(task2)

print(manager.get_tasks())