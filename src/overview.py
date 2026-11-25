from src.deadline import deadline_label
from src.panic_points import panic_points


def task_summary(task, today):
    deadline = deadline_label(task, today)
    points = panic_points(task, today)
    lines = [
        f"#{task['id']} {task['description']} [{task['status']}]",
        f"   Module: {task['module']} | Deadline: {deadline}",
        f"   Difficulty: {task['difficulty']}/5 | Panic Points: {points:.2f}",
    ]
    return "\n".join(lines)
