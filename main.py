"""Run the complete course scheduling system."""

from pathlib import Path

from UserStoryOne import LoadDisplayCourses
from UserStory6 import collect_requested_courses
from course_count_validation import ask_valid_course_count
from scheduler import parse_file
from story7 import display_schedule, find_valid_schedule
from story8 import NO_VALID_SCHEDULE_MESSAGE


DEFAULT_COURSE_FILE = Path(__file__).with_name("courses.txt")


def run_course_scheduler(course_file=DEFAULT_COURSE_FILE):
    """Run the course scheduling process from input through final output."""
    offered_courses = LoadDisplayCourses(course_file)

    if not offered_courses:
        return None

    course_sections = parse_file(course_file)
    number_of_courses = ask_valid_course_count(offered_courses)
    requested_courses = collect_requested_courses(
        number_of_courses,
        offered_courses,
    )

    schedule = find_valid_schedule(course_sections, requested_courses)

    if schedule is None:
        print(NO_VALID_SCHEDULE_MESSAGE)
        return None

    display_schedule(schedule)
    return schedule


if __name__ == "__main__":
    run_course_scheduler()
