[![Tests](https://github.com/wiamhalouane/my-first-python-project/actions/workflows/tests.yml/badge.svg)](https://github.com/wiamhalouane/my-first-python-project/actions/workflows/tests.yml)

#Student Grade Manager

A Python command-line application for managing student grades and storing student data using JSON.

Features

* Add students
* Automatically generate student IDs
* Add multiple grades
* Calculate student averages
* Display student information
* Search students by ID
* Delete students
* Update student grades
* Validate grades between 0 and 20
* Save and load data using JSON
* Automated tests with pytest
* Organized code using Python modules

Project Structure

my-first-python-project/
│
├── main.py
├── student_manager.py
├── storage.py
├── students.json
├── test_student_manager.py
├── requirements.txt
├── README.md
└── .gitignore

Requirements

* Python 3.10+
* pip

Installation

Clone the repository:

git clone https://github.com/wiamhalouane/my-first-python-project.git

Move into the project directory:

cd my-first-python-project

Install the dependencies:

python -m pip install -r requirements.txt

Run the Application

Start the application with:

python main.py

You will see:

Student Grade Manager
1. Add student
2. Show students
3. Search student
4. Delete student
5. Update student
6. Exit

Run Tests

Run the automated tests with:

python -m pytest

The tests cover the average calculation and JSON data storage.

Data Storage

Student data is stored in students.json.

Example:

[
    {
        "id": 1,
        "name": "Sara",
        "grades": [
            15.0,
            18.0
        ],
        "average": 16.5
    }
]

Technologies

* Python
* JSON
* pytest
* Git
* GitHub

What I Learned

This project helped me practice:

* Python functions
* Lists and dictionaries
* Loops and conditionals
* Input validation
* File handling
* JSON serialization and deserialization
* Error handling
* Python modules
* Automated testing
* Git and GitHub
* Project refactoring

Future Improvements

Possible future features:

* Student ranking
* Sort students by average
* Export reports
* Graphical user interface
* Database storage
* More comprehensive automated tests

Author

Wiam Halouane

This project was built as part of my Python learning journey.