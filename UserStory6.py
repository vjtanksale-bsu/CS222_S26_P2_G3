def collect_requested_courses(n, offeredCourses):
    selectedCourses = []
    print(f"Please enter the {n} course numbers you wish to register for:")
    while len(selectedCourses) < n:
        remaining = n - len(selectedCourses)
        userInput = input(f"Enter course number ({remaining} remaining): ").strip().upper()
        if userInput not in offeredCourses:
            print(f"Error: '{userInput}' is not offered this semester.")
            continue
        if userInput in selectedCourses:
            print(f"Error: You have already selected '{userInput}'. Duplicate entries are rejected.")
            continue
        selectedCourses.append(userInput)
        print(f"Successfully added '{userInput}'.")

    return selectedCourses
