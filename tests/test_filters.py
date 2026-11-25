import unittest

from src.filters import tasks_with_status
from tests.examples import example_task


class FilterTests(unittest.TestCase):
    def setUp(self):
        self.late = example_task(1, "Hand in lab", days=-2)
        self.today = example_task(2, "Book exam", module="Maths")
        self.week = example_task(3, "Lab notes", days=7)
        self.later = example_task(4, "Read chapter", days=8, module="History")
        self.finished = example_task(5, "First LAB", days=3, status="completed")
        self.tasks = [self.late, self.today, self.week, self.later, self.finished]

    def test_completed_list_contains_only_finished_tasks(self):
        self.assertEqual(tasks_with_status(self.tasks, "completed"), [self.finished])
