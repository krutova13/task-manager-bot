from datetime import datetime
import uuid

# 1
task_1 = {
    'name': 'Создать 10 тасок',
    'priority': 'Высокий',
    'term': '2025-04-05',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Написать задачи для Обучения и развития своих навыков',
    'topic': 'Обучения Python',
    'id': str(uuid.uuid4()),
    'status': 'Done'
}
# 2
task_2 = {
    'name': 'Разобрать беклог',
    'priority': 'Средний',
    'term': '2025-04-15',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Разобрать беклог задач в Jira',
    'topic': 'Беклог',
    'id': str(uuid.uuid4()),
    'status': 'To Do'
}
# 3
task_3 = {
    'name': 'Провести 1 то 1',
    'priority': 'Средний',
    'term': '2025-04-09',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Провести 1 то 1 с руководителем, поставить цели ИПР',
    'topic': 'ИПР',
    'id': str(uuid.uuid4()),
    'status': 'To Do'
}
# 4
task_4 = {
    'name': 'Общее собрание QA',
    'priority': 'Высокий',
    'term': '2025-04-08',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Провести общую встречу QA стрима, погрузиться в проблематику команд, выстроить план их решения',
    'topic': 'Планирование',
    'id': str(uuid.uuid4()),
    'status': 'To Do'
}
# 5
task_5 = {
    'name': 'Написать 1 автотест API',
    'priority': 'Средний',
    'term': '2025-04-15',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Покрыть автотестами 1 GET запроса API Dialer',
    'topic': 'Обучения Python',
    'id': str(uuid.uuid4()),
    'status': 'In Progress'
}
# 6
task_6 = {
    'name': 'Провести Дейли',
    'priority': 'Низкий',
    'term': '2025-04-07',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Провести дейли команды Dialer, обсудить статусы задач по каждой компетенции и актуализировать план',
    'topic': 'Планирование',
    'id': str(uuid.uuid4()),
    'status': 'To Do'
}
# 7
task_7 = {
    'name': 'Провести регресс тестирование будущего релиза',
    'priority': 'Высокий',
    'term': '2025-04-09',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Создать запуск в алюре, пройти кейсы регресса, создать отчет ',
    'topic': 'Тестирование',
    'id': str(uuid.uuid4()),
    'status': 'To Do'
}
# 8
task_8 = {
    'name': 'Провести тестирование новой функциональности',
    'priority': 'Высокий',
    'term': '2025-04-10',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Протестировать новую фичу, завести баги указав соответствующую метку, заполнить отчет',
    'topic': 'Тестирование',
    'id': str(uuid.uuid4()),
    'status': 'In Progress'
}
# 9
task_9 = {
    'name': 'Пройти курс автоматизации от Тета',
    'priority': 'Высокий',
    'term': '2025-04-25',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Пройти курс от Тета, закрепить свои знания практическими заданиями',
    'topic': 'Обучения Python',
    'id': str(uuid.uuid4()),
    'status': 'Done'
}
# 10
task_10 = {
    'name': 'Провести 1 то 1 с каждым сотрудником',
    'priority': 'Высокий',
    'term': '2025-04-15',
    'author': 'Алтынников',
    'creation date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'description': 'Обсудить точки роста и составить ИПР каждому сотруднику команды Dialer',
    'topic': 'ИПР',
    'id': str(uuid.uuid4()),
    'status': 'To Do'
}
