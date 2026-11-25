import unittest
from datetime import date

from src.deadline import parse_deadline, parse_semester_deadline


class DeadlineTests(unittest.TestCase):
    def test_valid_leap_day(self):
        self.assertEqual(parse_deadline("2028-02-29"), date(2028, 2, 29))

    def test_invalid_dates_and_formats(self):
        for value in ("2026-02-29", "2026-04-31", "10/04/2026", "20260410", ""):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_deadline(value)

    def test_semester_includes_both_endpoints(self):
        self.assertEqual(parse_semester_deadline("2026-09-01"), date(2026, 9, 1))
        self.assertEqual(parse_semester_deadline("2027-01-15"), date(2027, 1, 15))

    def test_semester_rejects_dates_outside_the_range(self):
        for value in ("2025-11-25", "2026-08-31", "2027-01-16"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "2026-09-01 to 2027-01-15"):
                    parse_semester_deadline(value)
