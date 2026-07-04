"""
User Story 2: Enter the Number of Courses

As a student, I want to enter how many courses I would like to register for,
so that the system knows how many course numbers to collect from me.
"""


def parse_course_count(user_input):
    """
    Convert the student's input into a positive whole number.

    Raises ValueError if the input is not a positive whole number.
    """
    try:
        course_count = int(user_input)
    except ValueError:
        raise ValueError("Course count must be a positive whole number.")

    if course_count <= 0:
        raise ValueError("Course count must be greater than zero.")

    return course_count


def ask_course_count(input_func=input, output_func=print):
    """
    Ask the student how many courses they want to register for.

    This function keeps asking until the student enters a positive whole number.
    """
    while True:
        user_input = input_func("How many courses would you like to register for? ")

        try:
            return parse_course_count(user_input)
        except ValueError as error:
            output_func(f"Error: {error}")


if __name__ == "__main__":
    count = ask_course_count()
    print(f"You selected {count} course(s).")
