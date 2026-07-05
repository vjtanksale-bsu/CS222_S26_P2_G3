"""
User Story 4: Enter Requested Course Numbers

As a student, I want to enter the course numbers I want to take,
so that the system can use my choices to build a schedule.
"""


def normalize_course_number(course_number):
    """Return a clean uppercase course number."""
    return course_number.strip().upper()


def collect_course_numbers(number_of_courses, input_func=input):
    """
    Ask the student to enter course numbers one at a time.

    This story focuses on collecting the requested number of course numbers.
    Validation against offered courses is handled by User Story 5.
    Duplicate checking is handled by User Story 6.
    """
    selected_courses = []

    while len(selected_courses) < number_of_courses:
        prompt = f"Enter course number {len(selected_courses) + 1} of {number_of_courses}: "
        entered_course = normalize_course_number(input_func(prompt))
        selected_courses.append(entered_course)

    return selected_courses


def display_selected_courses(selected_courses, output_func=print):
    """Display the course numbers entered by the student."""
    output_func("Selected courses:")
    for course_number in selected_courses:
        output_func(course_number)


if __name__ == "__main__":
    courses = collect_course_numbers(3)
    display_selected_courses(courses)
