import tempfile
import unittest
from pathlib import Path

from scheduler import Course, find_schedule, overlap, parse_file, valid_schedule
from story8 import NO_VALID_SCHEDULE_MESSAGE, run_story8


class InputMock:
    def __init__(self, responses):
        self.responses = list(responses)
        self.index = 0

    def __call__(self, prompt):
        response = self.responses[self.index]
        self.index += 1
        return response


class OutputMock:
    def __init__(self):
        self.messages = []

    def __call__(self, message):
        self.messages.append(message)


class TestScheduler(unittest.TestCase):

    def test_overlap_true(self):
        first_course = Course("CS120", "001", "MWF", "900", "1000")
        second_course = Course("CS121", "002", "MWF", "930", "1100")

        self.assertTrue(overlap(first_course, second_course))

    def test_overlap_false_when_days_do_not_match(self):
        first_course = Course("CS120", "001", "MWF", "900", "1000")
        second_course = Course("CS121", "002", "TR", "900", "1000")

        self.assertFalse(overlap(first_course, second_course))

    def test_valid_schedule(self):
        first_course = Course("CS120", "001", "MWF", "900", "1000")
        second_course = Course("CS121", "002", "TR", "900", "1000")

        self.assertTrue(valid_schedule([first_course, second_course]))

    def test_invalid_schedule(self):
        first_course = Course("CS120", "001", "MWF", "900", "1000")
        second_course = Course("CS121", "002", "MWF", "930", "1100")

        self.assertFalse(valid_schedule([first_course, second_course]))

    def test_find_schedule_returns_none_when_selected_courses_conflict(self):
        first_course = Course("CS120", "001", "MWF", "900", "1000")
        second_course = Course("CS121", "002", "MWF", "930", "1100")

        result = find_schedule([first_course, second_course])

        self.assertIsNone(result)

    def test_find_schedule_chooses_non_conflicting_sections(self):
        courses = [
            Course("CS120", "001", "MWF", "900", "1000"),
            Course("CS120", "002", "TR", "900", "1000"),
            Course("CS121", "001", "MWF", "930", "1100"),
        ]

        result = find_schedule(courses, ["CS120", "CS121"])

        self.assertIsNotNone(result)
        self.assertEqual([course.section for course in result], ["002", "001"])

    def test_find_schedule_returns_none_when_all_combinations_conflict(self):
        courses = [
            Course("CS120", "001", "MWF", "900", "1000"),
            Course("CS121", "001", "MWF", "930", "1100"),
        ]

        result = find_schedule(courses, ["CS120", "CS121"])

        self.assertIsNone(result)

    def test_parse_file_reads_valid_course_lines(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            course_file = Path(temporary_directory) / "courses.txt"
            course_file.write_text(
                "CS120 001 MWF 900 1000\n"
                "bad line\n"
                "CS121 001 TR 1100 1215\n",
                encoding="utf-8",
            )

            result = parse_file(course_file)

        self.assertEqual([course.code for course in result], ["CS120", "CS121"])

    def test_story8_notifies_when_no_valid_schedule_can_be_found(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            course_file = Path(temporary_directory) / "courses.txt"
            course_file.write_text(
                "CS120 001 MWF 900 1000\n"
                "CS121 001 MWF 930 1100\n",
                encoding="utf-8",
            )
            input_mock = InputMock(["2", "CS120", "CS121"])
            output_mock = OutputMock()

            result = run_story8(course_file, input_mock, output_mock)

        self.assertIsNone(result)
        self.assertIn(NO_VALID_SCHEDULE_MESSAGE, output_mock.messages)


if __name__ == "__main__":
    unittest.main()
