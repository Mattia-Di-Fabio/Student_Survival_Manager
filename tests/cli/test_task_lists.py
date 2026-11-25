import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from src.cli.task_lists import filter_by_module, show_completed
from tests.examples import example_task


class TaskListTests(unittest.TestCase):
    def test_completed_list_shows_description_module_and_deadline(self):
        active = example_task(1, "Prepare slides")
        finished = example_task(2, "Hand in essay", module="History", status="completed")
        text = show_completed([active, finished])
        self.assertIn("Hand in essay [completed]", text)
        self.assertIn("Module: History", text)
        self.assertIn("Deadline: 2026-04-10", text)
        self.assertNotIn("Prepare slides", text)


    def test_module_without_matches(self):
        tasks = [example_task(module="Math"), example_task(2, module="PoM", status="completed")]
        output = StringIO()
        with redirect_stdout(output), patch("builtins.input", return_value="3"):
            result = filter_by_module(tasks)
        self.assertEqual(result, "No matching tasks.")
        self.assertIn("3. Digital Business", output.getvalue())

    def test_module_shows_active_and_completed_matches(self):
        first = example_task(1, "First essay", module="Digital Business")
        second = example_task(2, "Second essay", module="Digital Business")
        finished = example_task(3, "Finished essay", module="Digital Business", status="completed")
        other = example_task(4, "Math revision", module="Math")
        with redirect_stdout(StringIO()), patch("builtins.input", return_value="3"):
            result = filter_by_module([first, second, finished, other])
        self.assertIn("First essay [active]", result)
        self.assertIn("Second essay", result)
        self.assertIn("Finished essay [completed]", result)
        self.assertNotIn("Math revision", result)
