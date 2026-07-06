import os

def LoadDisplayCourses(filePath):
    if not os.path.exists(filePath):
        print(f"Error: The course input file '{filePath}' could not be found.")
        return []

    offeredCourses = set()

    try:
        with open(filePath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                courseNumber = parts[0].strip().upper()
                offeredCourses.add(courseNumber)
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    sortedCourses = sorted(list(offeredCourses))
    print("\n--- Offered Course Numbers ---")
    for course in sortedCourses:
        print(course)
    print("------------------------------\n")

    return sortedCourses
