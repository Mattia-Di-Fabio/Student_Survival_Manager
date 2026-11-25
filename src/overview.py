from src.deadline import deadline_label
from src.filters import tasks_with_status
from src.panic_points import panic_level, panic_points, panic_totals


def dashboard_lines(tasks, today):
    active = tasks_with_status(tasks, "active")
    completed = tasks_with_status(tasks, "completed")
    base, score = panic_totals(tasks, today)
    level = panic_level(score)
    lines = [
        f"Active tasks: {len(active)}",
        f"Completed tasks: {len(completed)}",
        f"Base Panic Points: {base:.2f}",
        f"Overall Panic Score: {score:.2f}",
        f"Panic Level: {level}",
    ]
    return lines


def task_summary(task, today):
    deadline = deadline_label(task, today)
    points = panic_points(task, today)
    lines = [
        f"#{task['id']} {task['description']} [{task['status']}]",
        f"   Module: {task['module']} | Deadline: {deadline}",
        f"   Difficulty: {task['difficulty']}/5 | Panic Points: {points:.2f}",
    ]
    return "\n".join(lines)
