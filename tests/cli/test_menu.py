import json
import unittest
from contextlib import redirect_stdout
from io import StringIO
from tempfile import TemporaryDirectory
from unittest.mock import patch

from src.cli.menu import run
from src.storage import load_tasks
from tests.examples import example_task


class MenuTests(unittest.TestCase):
    def setUp(self):
        folder = TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.folder = folder.name
        location = patch("src.storage.PROJECT_FOLDER", self.folder)
        location.start()
        self.addCleanup(location.stop)

    def run_menu(self, answers):
        output = StringIO()
        with redirect_stdout(output), patch("builtins.input", side_effect=answers):
            run()
        return output.getvalue()


    def test_damaged_data_is_reported_on_startup(self):
        path = f"{self.folder}/tasks.json"
        with open(path, "w", encoding="utf-8") as file:
            file.write("broken")
        output = self.run_menu(["0"])
        self.assertIn("Could not load tasks:", output)
        with open(path, encoding="utf-8") as file:
            self.assertEqual(file.read(), "broken")

    def test_invalid_difficulty_stops_before_the_module_and_creates_nothing(self):
        output = self.run_menu(["3", "Read", "2026-10-21", "6", "0"])
        self.assertIn("Difficulty must be a whole number from 1 to 5.", output)
        self.assertNotIn("Task added successfully.", output)
        self.assertEqual(load_tasks(), [])

    def test_module_choice_retries_and_is_saved(self):
        answers = ["3", "Read", "2026-10-21", "2", "7", "3", "0"]
        output = self.run_menu(answers)
        self.assertIn("Please choose a number from 1 to 5.", output)
        self.assertIn("Task added successfully. ID: 1", output)
        self.assertEqual(load_tasks()[0]["module"], "Digital Business")

    def test_filter_uses_the_add_menu_order_for_all_five_modules(self):
        modules = ["Math", "PoM", "Digital Business", "Statistics", "Programming"]
        old_names = ["math", "pom", "digital business", "STATISTICS", "programming"]
        tasks = []
        for number, old_name in enumerate(old_names, 1):
            task = example_task(number, f"Assignment {number}")
            task["module"] = old_name
            tasks.append(task)
        with open(f"{self.folder}/tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file)

        for number, module in enumerate(modules, 1):
            with self.subTest(module=module):
                output = self.run_menu(["7", str(number), "0"])
                self.assertIn(f"  {number}. {module}", output)
                self.assertIn(f"Assignment {number} [active]", output)
                self.assertIn(f"Module: {module} |", output)
                self.assertEqual(output.count("[active]"), 1)

        output = self.run_menu(["7", "digital business", "6", "", "0"])
        self.assertEqual(output.count("Please choose a number from 1 to 5."), 2)
        self.assertNotIn("Assignment 3 [active]", output)
        self.assertIn("Filter cancelled.", output)

    def test_adding_task_retries_only_the_deadline_until_it_is_valid(self):
        answers = [
            "3", "Read", "2026-09-31", "30/09/2026", "2025-11-25", "2027-01-16",
            "2027-01-15", "2", "2", "0",
        ]
        output = StringIO()
        with redirect_stdout(output), patch("builtins.input", side_effect=answers) as inputs:
            run()
        prompts = [call.args[0] for call in inputs.call_args_list]
        self.assertEqual(prompts.count("Description: "), 1)
        self.assertEqual(prompts.count("Deadline (YYYY-MM-DD): "), 5)
        self.assertEqual(output.getvalue().count("Enter a valid deadline"), 2)
        self.assertEqual(output.getvalue().count("2026-09-01 to 2027-01-15"), 2)
        self.assertIn("Task added successfully. ID: 1", output.getvalue())

        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Read")
        self.assertEqual(tasks[0]["deadline"], "2027-01-15")


    def test_write_failure_returns_to_the_dashboard_without_confirming(self):
        answers = ["3", "Read", "2026-10-21", "2", "1", "1", "0"]
        with patch("src.storage.os.replace", side_effect=PermissionError("Access denied")):
            output = self.run_menu(answers)
        self.assertIn("Could not write the file: Access denied", output)
        self.assertNotIn("Task added successfully.", output)
        self.assertEqual(output.count("📚 Active tasks           | 0"), 2)
        self.assertEqual(load_tasks(), [])

    def test_interrupted_form_exits_without_saving(self):
        for interruption in (EOFError(), KeyboardInterrupt()):
            with self.subTest(interruption=interruption):
                output = self.run_menu(["3", "Draft", interruption])
                self.assertIn("Goodbye!", output)
                self.assertNotIn("Task added successfully.", output)
                self.assertEqual(load_tasks(), [])
