from src.deadline import parse_deadline


MODULES = {
    "1": "Math",
    "2": "PoM",
    "3": "Digital Business",
    "4": "Statistics",
    "5": "Programming",
}


def normalize_module(module):
    name = " ".join(module.split())
    key = name.casefold()
    if key in ("", "unassigned"):
        return "Unassigned"
    for module_name in MODULES.values():
        if key == module_name.casefold():
            return module_name
    return name


def read_description(description):
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Enter a description for the task.")
    return description.strip()


def read_difficulty(value):
    text = str(value).strip()
    if text not in ("1", "2", "3", "4", "5"):
        raise ValueError("Difficulty must be a whole number from 1 to 5.")
    difficulty = int(text)
    return difficulty


def task_record(task_id, description, due_date, difficulty, module, status):
    if type(task_id) is not int or task_id < 1:
        raise ValueError("Task IDs must be positive integers.")
    if not isinstance(module, str):
        raise ValueError("Enter a module name or leave it blank.")
    if status not in ("active", "completed"):
        raise ValueError("Unknown task status.")

    task = {
        "id": task_id,
        "description": description,
        "deadline": due_date.isoformat(),
        "difficulty": difficulty,
        "module": normalize_module(module),
        "status": status,
    }
    return task


def make_task(task_id, description, deadline, difficulty, module, status="active"):
    description = read_description(description)
    due_date = parse_deadline(deadline)
    difficulty = read_difficulty(difficulty)
    task = task_record(task_id, description, due_date, difficulty, module, status)
    return task


def next_task_id(tasks):
    largest = 0
    for task in tasks:
        if task["id"] > largest:
            largest = task["id"]
    return largest + 1


def find_task(tasks, task_id):
    selected = None
    for task in tasks:
        if task["id"] == task_id:
            selected = task
            break
    return selected
