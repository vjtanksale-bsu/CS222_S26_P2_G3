import unittest

from course_count_input import ask_course_count, parse_course_count


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


class TestUserStory2(unittest.TestCase):

    def test_parse_course_count_accepts_positive_whole_number(self):
        self.assertEqual(parse_course_count("3"), 3)

    def test_parse_course_count_rejects_non_number(self):
        with self.assertRaises(ValueError):
            parse_course_count("abc")

    def test_parse_course_count_rejects_zero(self):
        with self.assertRaises(ValueError):
            parse_course_count("0")

    def test_parse_course_count_rejects_negative_number(self):
        with self.assertRaises(ValueError):
            parse_course_count("-2")

    def test_ask_course_count_repeats_until_valid_input(self):
        input_mock = InputMock(["abc", "0", "2"])
        output_mock = OutputMock()

        result = ask_course_count(input_mock, output_mock)

        self.assertEqual(result, 2)
        self.assertEqual(len(output_mock.messages), 2)


if __name__ == "__main__":
    unittest.main()
