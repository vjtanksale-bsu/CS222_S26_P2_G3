from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Course:
    code: str
    section: str
    days: str
    start: int
    end: int

    def __init__(self, code, section, days, start, end):
        object.__setattr__(self, "code", normalize_course_code(code))
        object.__setattr__(self, "section", str(section).strip())
        object.__setattr__(self, "days", str(days).strip().upper())
        object.__setattr__(self, "start", int(start))
        object.__setattr__(self, "end", int(end))


def normalize_course_code(course_code):
    return str(course_code).strip().upper()


def parse_file(filename):
    courses = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()

            if len(parts) != 5:
                continue

            courses.append(Course(*parts))

    return courses


def overlap(first_course, second_course):
    if not (set(first_course.days) & set(second_course.days)):
        return False

    return not (
        first_course.end <= second_course.start
        or second_course.end <= first_course.start
    )


def valid_schedule(schedule):
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            if overlap(schedule[i], schedule[j]):
                return False

    return True


def find_schedule(courses, requested_course_codes=None):
    """
    Return one non-overlapping section for every requested course.

    If requested_course_codes is omitted, courses is treated as the full list
    that must fit together. The function returns None instead of silently
    dropping a requested course.
    """
    if requested_course_codes is None:
        return tuple(courses) if courses and valid_schedule(courses) else None

    requested_codes = [normalize_course_code(code) for code in requested_course_codes]
    sections_by_code = {
        requested_code: [
            course for course in courses if course.code == requested_code
        ]
        for requested_code in requested_codes
    }

    if any(len(sections) == 0 for sections in sections_by_code.values()):
        return None

    section_options = [sections_by_code[code] for code in requested_codes]

    for possible_schedule in product(*section_options):
        if valid_schedule(possible_schedule):
            return possible_schedule

    return None

