[![Tests](https://github.com/wiamhalouane/my-first-python-project/actions/workflows/tests.yml/badge.svg)](https://github.com/wiamhalouane/my-first-python-project/actions/workflows/tests.yml)
# Student Grade Manager

A Python command-line application for managing students, grades, averages, and rankings.

The project uses JSON for data storage and pytest for automated testing.

## Features

- Add students
- Automatically generate student IDs
- Add multiple grades
- Validate grades between 0 and 20
- Calculate student averages
- Display student information
- Show pass/fail status
- Search students by ID
- Update student grades
- Delete students
- Rank students by average
- Save student data to JSON
- Load student data from JSON
- Handle missing or corrupted JSON files
- Automated testing with pytest
- Continuous Integration with GitHub Actions

## Technologies

- Python
- Object-Oriented Programming (OOP)
- JSON
- pytest
- Git
- GitHub Actions

## Project Structure

```text
my-first-python-project/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── main.py
├── student.py
├── student_manager.py
├── storage.py
├── students.json
├── test_student_manager.py
├── requirements.txt
├── .gitignore
└── README.md