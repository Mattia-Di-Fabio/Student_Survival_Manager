from shutil import get_terminal_size

from src.cli import task_forms
from src.storage import load_tasks


MENU = {
    "3": ("Add a task", task_forms.add_task),
}


def show_menu(width):
    items = [" 0. Exit"]
    for number, (label, _) in MENU.items():
        items.append(f"{number:>2}. {label}")

    column_width = max(len(item) for item in items) + 3
    columns = max(1, min(3, width // column_width))
    print("\nMenu")
    for start in range(0, len(items), columns):
        row = items[start:start + columns]
        print("".join(item.ljust(column_width) for item in row).rstrip())


def run_choice(choice, tasks):
    if choice in MENU:
        label, action = MENU[choice]
        print(f"\n--- {label} ---")
        try:
            message = action(tasks)
        except ValueError as error:
            message = str(error)
        except OSError as error:
            message = f"Could not write the file: {error}"
    else:
        message = "Choose a number from 0 to 12."
    return message


def menu_loop(tasks):
    print("\n🎓 Welcome to Student Survival Manager!")

    show_menu(get_terminal_size().columns)
    prompt = "\nYour choice (0–12, Enter for menu): "
    choice = input(prompt).strip()
    while choice != "0":
        if choice:
            print(run_choice(choice, tasks))
        else:
            show_menu(get_terminal_size().columns)
        choice = input(prompt).strip()
    print("\nGoodbye! You've got this! 👋")


def run():
    try:
        tasks = load_tasks()
        menu_loop(tasks)
    except (OSError, ValueError) as error:
        print(f"Could not load tasks: {error}")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
