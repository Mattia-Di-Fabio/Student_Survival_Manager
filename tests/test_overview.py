import unittest

from src.overview import dashboard_lines
from tests.examples import TODAY, example_task


class OverviewTests(unittest.TestCase):
    def test_dashboard_counts_three_active_and_two_completed(self):
        tasks = [example_task(1), example_task(2), example_task(3),
                 example_task(4, status="completed"), example_task(5, status="completed")]
        lines = dashboard_lines(tasks, TODAY)
        self.assertIn("Active tasks: 3", lines)
        self.assertIn("Completed tasks: 2", lines)

    def test_dashboard_with_no_active_tasks(self):
        lines = dashboard_lines([example_task(status="completed")], TODAY)
        self.assertEqual(lines, [
            "Active tasks: 0", "Completed tasks: 1", "Base Panic Points: 0.00",
            "Overall Panic Score: 0.00", "Panic Level: NO PANIC 😎",
        ])

    def test_dashboard_at_fifteen_points(self):
        tasks = [example_task(1, difficulty=5), example_task(2, difficulty=5)]
        lines = dashboard_lines(tasks, TODAY)
        self.assertIn("Base Panic Points: 10.00", lines)
        self.assertIn("Overall Panic Score: 15.00", lines)
        self.assertIn("Panic Level: HIGH 😰", lines)
