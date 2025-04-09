import json
import data
from datetime import datetime

id = 0
database = {}
filtered_database = {}
sorted_database = {}

def generate_id():
    global id
    with open("id.txt") as id_file:
        id = id_file.read()
    print(id)
    new_id = int(id) + 1
    new_id = str(new_id)
    with open("id.txt", mode="w") as id_file:
        id_file.write(new_id)
    print(new_id)
    return id

def read_database():
    global database
    with open("database.json") as database_file:
        database = json.load(database_file)
    print(f"Вот текущая база данных: {database}.")
    return database

def update_database():
    with open("database.json", mode="w") as database_file:
        json.dump(database, database_file)
    print(f"Вот обновленная база данных: {database}.")

def add_task():
    id = generate_id()
    read_database()
    task_attribute = getattr(data, f"task_{id}") #да я спиздел вот эту строку у ИИ, но я реально не мог понять как это сделать, но зато потом почитал про getattr()
    database.update({f"{id}" : task_attribute})
    update_database()

def delete_task(id):
    read_database()
    if id in database:
        database.pop(id)
        update_database()
    else:
        print(f"Задачи с ID {id} нет в базе данных.")

def filter_by(filter):
    read_database()
    i = 0
    for task in database:
        if filter in database[task].values():
            filtered_database[task] = database[task]
            i += 1
    if i == 0:
        print(f"Задач с фильтром {filter} нет в базе данных.")
    print(filtered_database)

def filter_by_date(start_time, end_time):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    read_database()
    for task in database:
        creation = datetime.strptime(database[task]["creation date"], "%Y-%m-%d %H:%M:%S")
        if start <= creation <= end:
            filtered_database[task] = database[task]
    print(filtered_database)

def sort_by_old():
    read_database()
    sorted_database = dict(reversed(database.items()))
    print(sorted_database)