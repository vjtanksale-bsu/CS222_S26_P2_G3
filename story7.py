from itertools import product

def has_common_day(first_days, second_days):

    return bool(set(first_days) & set(second_days))

def has_time_conflict(first_course, second_course):

    if not has_common_day(first_course.days, second_course.days):

        return False

    return (

        first_course.start < second_course.end

        and second_course.start < first_course.end

    )

def is_valid_schedule(schedule):

    for first_index in range(len(schedule)):

        for second_index in range(first_index + 1, len(schedule)):

            if has_time_conflict(

                schedule[first_index],

                schedule[second_index]

            ):

                return False

    return True

def group_sections_by_course(courses):

    grouped_sections = {}

    for course in courses:

        if course.code not in grouped_sections:

            grouped_sections[course.code] = []

        grouped_sections[course.code].append(course)

    return grouped_sections

def find_valid_schedule(courses, selected_course_codes):

    grouped_sections = group_sections_by_course(courses)

    section_options = []

    for course_code in selected_course_codes:

        if course_code not in grouped_sections:

            return None

        section_options.append(grouped_sections[course_code])

    for schedule in product(*section_options):

        if is_valid_schedule(schedule):

            return list(schedule)

    return None

def display_schedule(schedule):

    if schedule is None:

        return False

    print("\nValid schedule:")

    for course in schedule:

        print(

            course.code,

            course.section,

            course.days,

            f"{course.start:04d}",

            f"{course.end:04d}"

        )

    return True