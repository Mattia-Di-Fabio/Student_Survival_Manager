import unittest
from math import sqrt

from src.panic_points import panic_level, panic_points, panic_totals, workload_effect
from tests.examples import TODAY, example_task


class PanicTests(unittest.TestCase):
    def test_points_follow_the_deadline_formula(self):
        for days, expected in [(-2, 5), (0, 5), (1, 5 / sqrt(2)), (3, 2.5)]:
            with self.subTest(days=days):
                task = example_task(days=days, difficulty=5)
                self.assertAlmostEqual(panic_points(task, TODAY), expected)

    def test_each_pair_counts_once(self):
        self.assertEqual(workload_effect([]), 0)
        self.assertEqual(workload_effect([5]), 0)
        self.assertAlmostEqual(workload_effect([5, 2, 1]), 3.4)

    def test_score_matches_the_readme_example(self):
        tasks = [
            example_task(difficulty=5),
            example_task(2, difficulty=2),
            example_task(3, difficulty=1),
        ]
        base, score = panic_totals(tasks, TODAY)
        self.assertEqual(base, 8)
        self.assertAlmostEqual(score, 11.4)


    def test_level_boundaries_use_the_unrounded_score(self):
        cases = [
            (0, "NO PANIC 😎"), (0.001, "LOW 🙂"), (4.9999, "LOW 🙂"),
            (5, "MEDIUM 😐"), (14.9999, "MEDIUM 😐"), (15, "HIGH 😰"),
            (29.9999, "HIGH 😰"), (30, "CRITICAL 🚨"), (100, "CRITICAL 🚨"),
        ]
        for score, expected in cases:
            with self.subTest(score=score):
                self.assertEqual(panic_level(score), expected)


    def test_totals_use_points_before_rounding(self):
        first = example_task(1, days=1, difficulty=5)
        second = example_task(2, days=1, difficulty=5)
        base, score = panic_totals([first, second], TODAY)
        self.assertAlmostEqual(base, 10 / sqrt(2))
        self.assertAlmostEqual(score, 10 / sqrt(2) + 2.5)
