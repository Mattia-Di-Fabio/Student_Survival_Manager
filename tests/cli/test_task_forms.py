import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from src.cli.task_forms import read_module


class TaskFormTests(unittest.TestCase):


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
