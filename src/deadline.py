from datetime import date


SEMESTER_START = date(2026, 9, 1)
SEMESTER_END = date(2027, 1, 15)


def parse_deadline(text):
    message = "Enter a valid deadline in YYYY-MM-DD format."
    try:
        deadline = date.fromisoformat(text)
    except (TypeError, ValueError):
        raise ValueError(message) from None
    if deadline.isoformat() != text:
        raise ValueError(message)
    return deadline


def parse_semester_deadline(text):
    deadline = parse_deadline(text)
    if not SEMESTER_START <= deadline <= SEMESTER_END:
        raise ValueError(f"Enter a deadline from {SEMESTER_START} to {SEMESTER_END}.")
    return deadline


def days_until(task, today):
    deadline = date.fromisoformat(task["deadline"])
    difference = deadline - today
    return difference.days


def deadline_label(task, today):
    label = task["deadline"]
    if task["status"] == "active":
        days = days_until(task, today)
        if days < 0:
            label += " (OVERDUE)"
        elif days == 0:
            label += " (due today)"
        elif days == 1:
            label += " (due tomorrow)"
        else:
            label += f" (in {days} days)"
    return label
