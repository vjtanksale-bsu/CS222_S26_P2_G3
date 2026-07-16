import unittest

from scheduler import Course

from story7 import (

    has_time_conflict,

    is_valid_schedule,

    find_valid_schedule

)

class TestStory7(unittest.TestCase):

    def test_courses_with_overlapping_times_conflict(self):

        first = Course("CS120", "001", "MWF", "0900", "0950")

        second = Course("CS121", "001", "MWF", "0930", "1045")

        self.assertTrue(has_time_conflict(first, second))

    def test_courses_on_different_days_do_not_conflict(self):

        first = Course("CS120", "001", "MWF", "0900", "0950")

        second = Course("CS121", "001", "TR", "0900", "1015")

        self.assertFalse(has_time_conflict(first, second))

    def test_valid_schedule_contains_one_section_per_course(self):

        courses = [

            Course("CS120", "001", "MWF", "0900", "0950"),

            Course("CS120", "002", "MWF", "1300", "1350"),

            Course("CS121", "001", "MWF", "0930", "1045"),

            Course("CS121", "002", "TR", "1100", "1215")

        ]

        schedule = find_valid_schedule(

            courses,

            ["CS120", "CS121"]

        )

        self.assertIsNotNone(schedule)

        self.assertEqual(len(schedule), 2)

        self.assertEqual(

            {course.code for course in schedule},

            {"CS120", "CS121"}

        )

        self.assertTrue(is_valid_schedule(schedule))

    def test_returns_none_when_every_combination_conflicts(self):

        courses = [

            Course("CS120", "001", "MWF", "0900", "1000"),

            Course("CS121", "001", "MWF", "0930", "1030")

        ]

        schedule = find_valid_schedule(

            courses,

            ["CS120", "CS121"]

        )

        self.assertIsNone(schedule)

    def test_returns_none_for_unavailable_course(self):

        courses = [

            Course("CS120", "001", "MWF", "0900", "0950")

        ]

        schedule = find_valid_schedule(

            courses,

            ["CS120", "CS999"]

        )

        self.assertIsNone(schedule)

if __name__ == "__main__":

    unittest.main()