from src.deadline import days_until
from src.task import normalize_module


def tasks_with_status(tasks, status):
    matches = []
    for task in tasks:
        if task["status"] == status:
            matches.append(task)
    return matches


def tasks_for_module(tasks, module):
    module = normalize_module(module).casefold()
    matches = []
    for task in tasks:
        if task["module"].casefold() == module:
            matches.append(task)
    return matches


def overdue_tasks(tasks, today):
    overdue = []
    for task in tasks_with_status(tasks, "active"):
        if days_until(task, today) < 0:
            overdue.append(task)
    return overdue
