import unittest

from course_count_validation import (
    ask_valid_course_count,
    get_distinct_course_numbers,
    validate_course_count,
)


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


class TestUserStory3(unittest.TestCase):

    def test_get_distinct_course_numbers_removes_duplicates(self):
        course_sections = [
            ("CS120", "001", "MWF", "0900", "0950"),
            ("CS121", "002", "TR", "1230", "1345"),
            ("CS120", "003", "TR", "1500", "1615"),
        ]

        result = get_distinct_course_numbers(course_sections)

        self.assertEqual(result, ["CS120", "CS121"])


    def test_validate_course_count_accepts_valid_count(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        self.assertTrue(validate_course_count(2, offered_courses))


    def test_validate_course_count_rejects_too_many_courses(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        with self.assertRaises(ValueError):
            validate_course_count(4, offered_courses)


    def test_ask_valid_course_count_repeats_until_count_is_not_too_large(self):
        offered_courses = ["CS120", "CS121", "CS222"]
        input_mock = InputMock(["5", "3"])
        output_mock = OutputMock()

        result = ask_valid_course_count(offered_courses, input_mock, output_mock)

        self.assertEqual(result, 3)
        self.assertEqual(len(output_mock.messages), 1)


if __name__ == "__main__":
    unittest.main()
