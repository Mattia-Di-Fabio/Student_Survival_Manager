import json
import os
import unittest
from tempfile import TemporaryDirectory

from src.storage import load_tasks
from tests.examples import example_task


class StorageTests(unittest.TestCase):
    def setUp(self):
        folder = TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = os.path.join(folder.name, "tasks.json")
        self.temporary_file = os.path.join(folder.name, "tasks.tmp")

    def test_first_start_has_an_empty_list(self):
        self.assertEqual(load_tasks(self.path), [])


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
