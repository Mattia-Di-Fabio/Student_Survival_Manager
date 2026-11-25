from datetime import date

from src import filters
from src.cli.task_forms import read_module_choice
from src.overview import task_summary
from src.task import MODULES


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


def filter_by_module(tasks):
    if not tasks:
        return "No matching tasks."
    choice = read_module_choice("Module number (Enter to cancel): ")
    if not choice:
        return "Filter cancelled."
    matches = filters.tasks_for_module(tasks, MODULES[choice])
    today = date.today()
    return list_text(matches, today, "No matching tasks.")


def show_overdue(tasks):
    today = date.today()
    overdue = filters.overdue_tasks(tasks, today)
    return list_text(overdue, today, "No overdue tasks.")
