import unittest
from unittest.mock import patch

from UserStory6 import collect_requested_courses


class TestUserStorySix(unittest.TestCase):

    def test_collects_requested_courses(self):
        offered_courses = ["CS120", "CS121", "CS222"]

        with patch("builtins.input", side_effect=["CS120", "CS121"]):
            with patch("builtins.print"):
                result = collect_requested_courses(2, offered_courses)

        self.assertEqual(result, ["CS120", "CS121"])

    def test_normalizes_lowercase_input(self):
        offered_courses = ["CS120"]

        with patch("builtins.input", return_value=" cs120 "):
            with patch("builtins.print"):
                result = collect_requested_courses(1, offered_courses)

        self.assertEqual(result, ["CS120"])

    def test_rejects_course_that_is_not_offered(self):
        offered_courses = ["CS120"]

        with patch("builtins.input", side_effect=["CS999", "CS120"]):
            with patch("builtins.print") as mock_print:
                result = collect_requested_courses(1, offered_courses)

        self.assertEqual(result, ["CS120"])
        printed_messages = [str(call.args[0]) for call in mock_print.call_args_list]
        self.assertTrue(any("not offered" in message for message in printed_messages))

    def test_rejects_duplicate_course_and_asks_again(self):
        offered_courses = ["CS120", "CS121"]

        with patch(
            "builtins.input",
            side_effect=["CS120", "CS120", "CS121"],
        ):
            with patch("builtins.print") as mock_print:
                result = collect_requested_courses(2, offered_courses)

        self.assertEqual(result, ["CS120", "CS121"])
        printed_messages = [str(call.args[0]) for call in mock_print.call_args_list]
        self.assertTrue(any("Duplicate" in message for message in printed_messages))


if __name__ == "__main__":
    unittest.main()
