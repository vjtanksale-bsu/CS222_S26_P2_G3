import unittest
from unittest.mock import patch

from scheduler import Course

from main import run_course_scheduler


class TestMainProgram(unittest.TestCase):

    @patch("main.display_schedule")
    @patch("main.find_valid_schedule")
    @patch("main.collect_requested_courses", return_value=["CS120", "CS121"])
    @patch("main.ask_valid_course_count", return_value=2)
    @patch("main.parse_file")
    @patch("main.LoadDisplayCourses", return_value=["CS120", "CS121"])
    def test_runs_complete_process_and_displays_schedule(
        self,
        mock_load_courses,
        mock_parse_file,
        mock_course_count,
        mock_collect_courses,
        mock_find_schedule,
        mock_display_schedule,
    ):
        course_sections = [
            Course("CS120", "001", "MWF", "0900", "0950"),
            Course("CS121", "001", "TR", "1100", "1215"),
        ]
        mock_parse_file.return_value = course_sections
        mock_find_schedule.return_value = course_sections

        result = run_course_scheduler("courses.txt")

        self.assertEqual(result, course_sections)
        mock_load_courses.assert_called_once_with("courses.txt")
        mock_course_count.assert_called_once_with(["CS120", "CS121"])
        mock_collect_courses.assert_called_once_with(
            2,
            ["CS120", "CS121"],
        )
        mock_find_schedule.assert_called_once_with(
            course_sections,
            ["CS120", "CS121"],
        )
        mock_display_schedule.assert_called_once_with(course_sections)

    @patch("main.parse_file")
    @patch("main.LoadDisplayCourses", return_value=[])
    def test_stops_when_course_file_cannot_be_loaded(
        self,
        mock_load_courses,
        mock_parse_file,
    ):
        result = run_course_scheduler("missing.txt")

        self.assertIsNone(result)
        mock_load_courses.assert_called_once_with("missing.txt")
        mock_parse_file.assert_not_called()

    @patch("builtins.print")
    @patch("main.find_valid_schedule", return_value=None)
    @patch("main.collect_requested_courses", return_value=["CS120", "CS121"])
    @patch("main.ask_valid_course_count", return_value=2)
    @patch("main.parse_file", return_value=[])
    @patch("main.LoadDisplayCourses", return_value=["CS120", "CS121"])
    def test_displays_message_when_schedule_cannot_be_found(
        self,
        mock_load_courses,
        mock_parse_file,
        mock_course_count,
        mock_collect_courses,
        mock_find_schedule,
        mock_print,
    ):
        result = run_course_scheduler("courses.txt")

        self.assertIsNone(result)
        mock_print.assert_called_once_with("No valid schedule can be found.")


if __name__ == "__main__":
    unittest.main()
