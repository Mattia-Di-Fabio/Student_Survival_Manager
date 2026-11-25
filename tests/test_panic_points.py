import unittest
from math import sqrt

from src.panic_points import panic_points
from tests.examples import TODAY, example_task


class PanicTests(unittest.TestCase):
    def test_points_follow_the_deadline_formula(self):
        for days, expected in [(-2, 5), (0, 5), (1, 5 / sqrt(2)), (3, 2.5)]:
            with self.subTest(days=days):
                task = example_task(days=days, difficulty=5)
                self.assertAlmostEqual(panic_points(task, TODAY), expected)
