import unittest

from course_number_entry import collect_course_numbers, normalize_course_number


class InputMock:
    def __init__(self, responses):
        self.responses = list(responses)
        self.index = 0

    def __call__(self, prompt):
        response = self.responses[self.index]
        self.index += 1
        return response


class TestUserStory4(unittest.TestCase):

    def test_normalize_course_number_removes_spaces_and_uppercases(self):
        self.assertEqual(normalize_course_number(" cs120 "), "CS120")


    def test_collect_course_numbers_collects_exact_requested_number(self):
        input_mock = InputMock(["CS120", "cs121", " CS222 "])

        result = collect_course_numbers(3, input_mock)

        self.assertEqual(result, ["CS120", "CS121", "CS222"])


    def test_collect_course_numbers_collects_one_course(self):
        input_mock = InputMock(["MATH165"])

        result = collect_course_numbers(1, input_mock)

        self.assertEqual(result, ["MATH165"])


if __name__ == "__main__":
    unittest.main()
