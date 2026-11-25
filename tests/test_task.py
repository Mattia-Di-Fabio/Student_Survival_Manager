import unittest

from src.task import make_task, next_task_id
from tests.examples import example_task


class TaskTests(unittest.TestCase):
    def test_new_task_records_the_fields_and_starts_active(self):
        task = make_task(7, "  Revise chapter two  ", "2026-04-12", "4", "  math  ")
        self.assertEqual(task, {
            "id": 7,
            "description": "Revise chapter two",
            "deadline": "2026-04-12",
            "difficulty": 4,
            "module": "Math",
            "status": "active",
        })

    def test_blank_module_is_unassigned(self):
        task = example_task(module="  ")
        self.assertEqual(task["module"], "Unassigned")

    def test_description_is_required(self):
        with self.assertRaises(ValueError):
            example_task(description="   ")

    def test_difficulty_is_a_whole_number_between_one_and_five(self):
        for value in (0, 6, -1, "hard", "", "2.5", 3.5):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    example_task(difficulty=value)
        for value in (1, 5):
            task = example_task(difficulty=value)
            self.assertEqual(task["difficulty"], value)

    def test_next_id_follows_the_largest_existing_id(self):
        tasks = [example_task(9), example_task(2)]
        self.assertEqual(next_task_id([]), 1)
        self.assertEqual(next_task_id(tasks), 10)
