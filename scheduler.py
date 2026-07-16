class Course:

    def __init__(self, code, section, days, start, end):

        self.code = code

        self.section = section

        self.days = days

        self.start = int(start)

        self.end = int(end)

def parse_file(filename):

    courses = []

    with open(filename, "r") as file:

        for line in file:

            parts = line.split()

            if len(parts) == 5:

                courses.append(Course(*parts))

    return courses