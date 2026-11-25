from datetime import date

from src import filters
from src.overview import task_summary


def list_text(tasks, today, empty_message):
    lines = []
    for task in tasks:
        lines.append(task_summary(task, today))
    if not lines:
        lines.append(empty_message)
    return "\n\n".join(lines)


def show_completed(tasks):
    today = date.today()
    completed = filters.tasks_with_status(tasks, "completed")
    return list_text(completed, today, "No completed tasks.")
