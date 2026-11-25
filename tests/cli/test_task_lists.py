import unittest

from src.cli.task_lists import show_completed
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
