"""
User Story 5: Reject a Course Number That Is Not Offered

As a student, I want the system to reject course numbers that are not offered,
so that my schedule is built only from available courses.
"""


def normalize_course_number(course_number):
    """Return a clean uppercase course number."""
    return course_number.strip().upper()


def is_course_offered(course_number, offered_course_numbers):
    """Check whether a course number exists in the offered course list."""
    normalized_course = normalize_course_number(course_number)

    normalized_offered_courses = {
        normalize_course_number(offered_course)
        for offered_course in offered_course_numbers
    }

    return normalized_course in normalized_offered_courses


def validate_offered_course(course_number, offered_course_numbers):
    """
    Validate that an entered course number is offered.

    Returns the normalized course number if valid.
    Raises ValueError if the course number is not offered.
    """
    normalized_course = normalize_course_number(course_number)

    if not is_course_offered(normalized_course, offered_course_numbers):
        raise ValueError(f"{normalized_course} is not an offered course.")

    return normalized_course


def collect_valid_course_numbers(
    number_of_courses,
    offered_course_numbers,
    input_func=input,
    output_func=print,
):
    """Ask for course numbers and only store courses that are offered."""
    selected_courses = []

    while len(selected_courses) < number_of_courses:
        prompt = f"Enter course number {len(selected_courses) + 1} of {number_of_courses}: "
        entered_course = input_func(prompt)

        try:
            valid_course = validate_offered_course(entered_course, offered_course_numbers)
            selected_courses.append(valid_course)
        except ValueError as error:
            output_func(f"Error: {error}")

    return selected_courses


if __name__ == "__main__":
    offered_courses = ["CS120", "CS121", "CS222"]
    selected = collect_valid_course_numbers(2, offered_courses)
    print(selected)
