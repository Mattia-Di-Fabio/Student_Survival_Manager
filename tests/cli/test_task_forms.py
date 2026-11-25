import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from src.cli.task_forms import read_module, read_task
from tests.examples import example_task


class TaskFormTests(unittest.TestCase):


    def test_editing_all_fields_preserves_id_and_status(self):
        original = example_task(7, status="completed")
        answers = ["New essay", "2026-09-01", "5", "5"]
        with redirect_stdout(StringIO()), patch("builtins.input", side_effect=answers):
            edited = read_task(7, original)
        self.assertEqual(edited, {
            "id": 7, "description": "New essay", "deadline": "2026-09-01",
            "difficulty": 5, "module": "Programming", "status": "completed",
        })
        self.assertEqual(original["description"], "Lab report")

    def test_module_choices_and_invalid_input(self):
        modules = ["Math", "PoM", "Digital Business", "Statistics", "Programming"]
        for number, module in enumerate(modules, 1):
            with self.subTest(module=module):
                with redirect_stdout(StringIO()), patch("builtins.input", return_value=str(number)):
                    self.assertEqual(read_module(), module)

        output = StringIO()
        with redirect_stdout(output), patch("builtins.input", side_effect=["6", "abc", "3"]):
            self.assertEqual(read_module(), "Digital Business")
        self.assertEqual(output.getvalue().count("Please choose a number"), 2)

    def test_blank_module_and_existing_module(self):
        with redirect_stdout(StringIO()), patch("builtins.input", return_value=""):
            self.assertEqual(read_module(), "Unassigned")
            self.assertEqual(read_module("History"), "History")

    def test_enter_keeps_current_values(self):
        original = example_task()
        with redirect_stdout(StringIO()), patch("builtins.input", side_effect=["", "", "", ""]):
            edited = read_task(1, original)
        self.assertEqual(edited, original)

    def test_invalid_edit_preserves_all_original_fields(self):
        original = example_task()
        invalid_edits = [
            ["   "],
            ["New essay", "2026-02-31"],
            ["New essay", "2027-01-16"],
            ["New essay", "", "6"],
        ]
        for answers in invalid_edits:
            with self.subTest(answers=answers):
                with redirect_stdout(StringIO()), patch("builtins.input", side_effect=answers):
                    with self.assertRaises(ValueError):
                        read_task(1, original)
                self.assertEqual(original, example_task())
