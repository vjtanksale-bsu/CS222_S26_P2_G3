"""
User Story 3: Prevent Entering More Courses Than Offered

As a student, I want the system to reject a course count greater than the
number of offered courses, so that I do not try to register for more courses
than are available.
"""


def get_distinct_course_numbers(course_sections):
    """
    Return a sorted list of distinct course numbers.

    course_sections can contain tuples/lists where index 0 is the course
    number or dictionaries with a 'course_number' key.
    """
    course_numbers = set()

    for section in course_sections:
        if isinstance(section, dict):
            course_number = section["course_number"]
        else:
            course_number = section[0]

        course_numbers.add(course_number.strip().upper())

    return sorted(course_numbers)


def validate_course_count(course_count, offered_course_numbers):
    """
    Make sure the requested course count is not greater than the number
    of distinct offered courses.
    """
    total_offered_courses = len(set(offered_course_numbers))

    if course_count > total_offered_courses:
        raise ValueError(
            f"The student requested {course_count} courses, but only "
            f"{total_offered_courses} distinct courses are offered."
        )

    return True


def ask_valid_course_count(offered_course_numbers, input_func=input, output_func=print):
    """
    Ask for a course count and reject numbers greater than the number of
    offered courses.
    """
    while True:
        user_input = input_func("How many courses would you like to register for? ")

        try:
            course_count = int(user_input)
        except ValueError:
            output_func("Error: Course count must be a positive whole number.")
            continue

        if course_count <= 0:
            output_func("Error: Course count must be greater than zero.")
            continue

        try:
            validate_course_count(course_count, offered_course_numbers)
            return course_count
        except ValueError as error:
            output_func(f"Error: {error}")


if __name__ == "__main__":
    offered = ["CS120", "CS121", "CS222"]
    count = ask_valid_course_count(offered)
    print(f"Valid course count: {count}")
