from scheduler import find_schedule, normalize_course_code, parse_file


NO_VALID_SCHEDULE_MESSAGE = "No valid schedule can be found."


def run_story8(course_file="courses.txt", input_func=input, output_func=print):
    courses = parse_file(course_file)

    output_func("Available courses:")
    for course in courses:
        output_func(
            f"{course.code} {course.section} {course.days} "
            f"{course.start} {course.end}"
        )

    try:
        number_of_courses = int(input_func("How many courses: "))
    except ValueError:
        output_func("Invalid input")
        return None

    if number_of_courses <= 0:
        output_func(NO_VALID_SCHEDULE_MESSAGE)
        return None

    requested_course_codes = []
    offered_course_codes = {course.code for course in courses}

    for _ in range(number_of_courses):
        course_code = normalize_course_code(input_func("Enter course code: "))

        if course_code not in offered_course_codes:
            output_func(f"Course not found: {course_code}")
            return None

        requested_course_codes.append(course_code)

    result = find_schedule(courses, requested_course_codes)

    if result is None:
        output_func(NO_VALID_SCHEDULE_MESSAGE)
        return None

    output_func("")
    output_func("Valid schedule:")
    for course in result:
        output_func(
            f"{course.code} {course.section} {course.days} "
            f"{course.start} {course.end}"
        )

    return result


if __name__ == "__main__":
    run_story8()
