import os


def LoadDisplayCourses(filePath):
    if not os.path.exists(filePath):
        print(f"Error: The course input file '{filePath}' could not be found.")
        return []

    offeredCourses = set()

    try:
        with open(filePath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()
                courseNumber = parts[0].strip().upper()
                offeredCourses.add(courseNumber)
    except Exception as error:
        print(f"Error reading file: {error}")
        return []

    sortedCourses = sorted(offeredCourses)
    print("\n--- Offered Course Numbers ---")
    for course in sortedCourses:
        print(course)
    print("------------------------------\n")

    return sortedCourses
