import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from UserStoryOne import LoadDisplayCourses


class TestUserStoryOne(unittest.TestCase):

    def test_loads_and_sorts_distinct_course_numbers(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            course_file = Path(temporary_directory) / "courses.txt"
            course_file.write_text(
                "CS120 001 MWF 0900 0950\n"
                "CS120 003 TR 0930 1045\n"
                "CS121 001 TR 1230 1345\n"
                "CS222 005 TR 1100 1215\n",
                encoding="utf-8",
            )

            with patch("builtins.print"):
                result = LoadDisplayCourses(course_file)

        self.assertEqual(result, ["CS120", "CS121", "CS222"])

    def test_ignores_blank_lines(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            course_file = Path(temporary_directory) / "courses.txt"
            course_file.write_text(
                "\nCS120 001 MWF 0900 0950\n\n",
                encoding="utf-8",
            )

            with patch("builtins.print"):
                result = LoadDisplayCourses(course_file)

        self.assertEqual(result, ["CS120"])

    def test_returns_empty_list_when_file_does_not_exist(self):
        missing_file = "file_that_does_not_exist.txt"

        with patch("builtins.print") as mock_print:
            result = LoadDisplayCourses(missing_file)

        self.assertEqual(result, [])
        self.assertIn("could not be found", mock_print.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
