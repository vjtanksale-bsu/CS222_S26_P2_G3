import unittest

from offered_course_validation import (
    collect_valid_course_numbers,
    is_course_offered,
    validate_offered_course,
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


class TestUserStory5(unittest.TestCase):

    def test_is_course_offered_returns_true_for_offered_course(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        self.assertTrue(is_course_offered("cs120", offered_courses))


    def test_is_course_offered_returns_false_for_unoffered_course(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        self.assertFalse(is_course_offered("CS999", offered_courses))


    def test_validate_offered_course_returns_normalized_course(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        result = validate_offered_course(" cs121 ", offered_courses)

        self.assertEqual(result, "CS121")


    def test_validate_offered_course_rejects_unoffered_course(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        with self.assertRaises(ValueError):
            validate_offered_course("CS999", offered_courses)


    def test_collect_valid_course_numbers_rejects_invalid_and_asks_again(self):
        offered_courses = ["CS120", "CS121", "CS222"]
        input_mock = InputMock(["CS999", "CS120"])
        output_mock = OutputMock()

        result = collect_valid_course_numbers(1, offered_courses, input_mock, output_mock)

        self.assertEqual(result, ["CS120"])
        self.assertEqual(len(output_mock.messages), 1)
        self.assertIn("CS999 is not an offered course", output_mock.messages[0])


if __name__ == "__main__":
    unittest.main()
