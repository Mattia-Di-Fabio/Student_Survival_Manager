import json
import os
import unittest
from tempfile import TemporaryDirectory

from src.storage import load_tasks, save_task
from tests.examples import example_task


class StorageTests(unittest.TestCase):
    def setUp(self):
        folder = TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = os.path.join(folder.name, "tasks.json")
        self.temporary_file = os.path.join(folder.name, "tasks.tmp")

    def test_first_start_has_an_empty_list(self):
        self.assertEqual(load_tasks(self.path), [])

    def test_add_then_edit_and_reload(self):
        tasks = []
        first = example_task(description="Préparer le résumé")
        second = example_task(2, status="completed")
        added = save_task(tasks, first, path=self.path)
        self.assertEqual(added, first)
        save_task(tasks, second, path=self.path)
        edited = example_task(description="Final résumé", difficulty=5)
        saved = save_task(tasks, edited, first, path=self.path)
        self.assertEqual(saved, edited)
        self.assertEqual(tasks, [edited, second])
        self.assertEqual(load_tasks(self.path), tasks)

    def test_invalid_file_is_reported_and_preserved(self):
        for content in ("broken", "{}", "[{}]", "[1]"):
            with self.subTest(content=content):
                with open(self.path, "w", encoding="utf-8") as file:
                    file.write(content)
                with self.assertRaises(ValueError):
                    load_tasks(self.path)
                with open(self.path, encoding="utf-8") as file:
                    self.assertEqual(file.read(), content)

    def test_rejects_duplicate_ids_and_invalid_saved_fields(self):
        task = example_task()
        invalid_date = dict(task, deadline="2026-02-31")
        invalid_status = dict(task, status="pending")
        invalid_id = dict(task, id=0)
        invalid_module = dict(task, module=None)
        for records in ([task, task], [invalid_date], [invalid_status], [invalid_id], [invalid_module]):
            with self.subTest(records=records):
                with open(self.path, "w", encoding="utf-8") as file:
                    json.dump(records, file)
                with self.assertRaises(ValueError):
                    load_tasks(self.path)

    def test_failed_save_preserves_the_previous_task(self):
        tasks = []
        original = example_task()
        save_task(tasks, original, path=self.path)
        os.mkdir(self.temporary_file)
        edited = example_task(description="Different")
        with self.assertRaises(OSError):
            save_task(tasks, edited, original, path=self.path)
        self.assertEqual(tasks, [original])
        self.assertEqual(load_tasks(self.path), [original])
