import json
import os

from src.task import make_task


SOURCE_FOLDER = os.path.dirname(__file__)
PROJECT_FOLDER = os.path.dirname(SOURCE_FOLDER)


def project_file(name):
    return os.path.join(PROJECT_FOLDER, name)


def read_saved_task(record):
    fields = ("id", "description", "deadline", "difficulty", "module", "status")
    if not isinstance(record, dict):
        raise ValueError("Invalid task in tasks.json.")
    for field in fields:
        if field not in record:
            raise ValueError(f"Missing field in tasks.json: {field}")

    task = make_task(
        record["id"], record["description"], record["deadline"],
        record["difficulty"], record["module"], record["status"],
    )
    return task


def load_tasks(path=None):
    if path is None:
        path = project_file("tasks.json")
    tasks = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            raise ValueError("Expected a list in tasks.json.")

        ids = set()
        for record in records:
            task = read_saved_task(record)
            if task["id"] in ids:
                raise ValueError(f"Duplicate task ID in tasks.json: {task['id']}")
            tasks.append(task)
            ids.add(task["id"])
    return tasks


def write_tasks(tasks, path=None):
    if path is None:
        path = project_file("tasks.json")
    name, _ = os.path.splitext(path)
    temporary_file = name + ".tmp"
    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)
        file.write("\n")
    os.replace(temporary_file, path)


def save_task(tasks, task, previous=None, path=None):
    updated = tasks.copy()
    if previous is None:
        updated.append(task)
    else:
        index = updated.index(previous)
        updated[index] = task

    write_tasks(updated, path)
    tasks[:] = updated
    return task
