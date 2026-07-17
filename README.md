# CS 222 Project 2: Course Scheduling System

## Authors

- Pengyu Lu
- Charlie Rosales
- YiRan Cao

## Project Overview

This project is a Python course scheduling system that helps a student choose courses for a semester. The program reads all available course sections from a text file, accepts the student's requested courses, and searches for a schedule without time conflicts. If no valid schedule is available, the program notifies the student.

The project was developed in three iterations using Test-Driven Development, Clean Code practices, separate branches for user stories, pull requests, and GitHub merges.

## Features

The system supports the following user stories:

1. Display all offered course numbers.
2. Ask how many courses the student wants to take.
3. Prevent the student from requesting more courses than are offered.
4. Accept the requested course numbers.
5. Reject a course number that is not offered.
6. Reject the same course when it is entered more than once.
7. Find and display a valid schedule without time conflicts.
8. Notify the student when no valid schedule can be found.

## Course File Format

The program reads course information from a file named `courses.txt` in the project directory. Each line must contain the course number, section number, meeting days, start time, and end time.

Example:

```text
CS120 001 MWF 0900 0950
CS120 003 TR 0900 1015
CS121 001 TR 1230 1345
CS222 005 TR 1100 1215
```

## Requirements

- Python 3
- No third-party packages are required

## How to Run the Program

1. Download or clone the repository.
2. Add a valid `courses.txt` file to the root of the project.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

The program will display the offered courses, ask how many courses the student wants, collect the requested course numbers, and display a valid schedule or a message explaining that no valid schedule was found.

## How to Run the Tests

Run all unit tests from the root of the project:

```bash
python -m unittest discover -v
```

The test files cover course input, course-count validation, offered-course validation, duplicate-course rejection, time-conflict detection, valid-schedule generation, and the no-schedule result.

## Main Project Files

- `main.py`: runs the complete course scheduling process
- `UserStoryOne.py`: loads and displays offered course numbers
- `course_count_input.py`: accepts the requested course count
- `course_count_validation.py`: validates the requested course count
- `course_number_entry.py`: collects course numbers
- `offered_course_validation.py`: rejects courses that are not offered
- `UserStory6.py`: rejects duplicate course selections
- `scheduler.py`: reads course sections and contains scheduling logic
- `story7.py`: finds and displays a valid schedule
- `story8.py`: notifies the student when a valid schedule cannot be found
- `test_*.py`: unit tests for the user stories and scheduling logic
