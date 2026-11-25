
from src.deadline import parse_deadline, parse_semester_deadline
from src.storage import save_task
from src.task import MODULES, next_task_id, read_description, read_difficulty, task_record


def read_module_choice(prompt):
    for number, module in MODULES.items():
        print(f"  {number}. {module}")
    choice = input(prompt).strip()
    while choice and choice not in MODULES:
        print("Please choose a number from 1 to 5.")
        choice = input(prompt).strip()
    return choice


def read_module(current=None):
    print("\nChoose your module")
    if current is None:
        prompt = "Module number (Enter for Unassigned): "
    else:
        prompt = f"Module number (Enter to keep {current}): "

    choice = read_module_choice(prompt)
    if choice:
        return MODULES[choice]
    if current is not None:
        return current
    return "Unassigned"


def read_field(label, current=None):
    if current is not None:
        label = f"{label} [{current}]"
    answer = input(f"{label}: ")
    value = answer.strip()
    if answer == "" and current is not None:
        value = current
    return value


def read_deadline(current=None):
    label = "Deadline (YYYY-MM-DD)"
    if current is not None:
        answer = read_field(label, current)
        if answer == current:
            return parse_deadline(answer)
        return parse_semester_deadline(answer)

    deadline = None
    while deadline is None:
        answer = read_field(label)
        try:
            deadline = parse_semester_deadline(answer)
        except ValueError as error:
            print(error)
    return deadline


def read_task(task_id, previous=None):
    if previous is None:
        previous = {}
    else:
        print("Press Enter to keep the current value.")
    answer = read_field("Description", previous.get("description"))
    description = read_description(answer)
    due_date = read_deadline(previous.get("deadline"))
    answer = read_field("Difficulty (1-5)", previous.get("difficulty"))
    difficulty = read_difficulty(answer)
    module = read_module(previous.get("module"))
    status = previous.get("status", "active")
    task = task_record(task_id, description, due_date, difficulty, module, status)
    return task


def add_task(tasks):
    task_id = next_task_id(tasks)
    task = read_task(task_id)
    saved = save_task(tasks, task)
    return f"Task added successfully. ID: {saved['id']}\nYou're ready to get started! ✨"
