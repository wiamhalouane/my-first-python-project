import json

from student import Student


def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        return [Student.from_dict(student) for student in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: students.json is empty or corrupted.")
        return []


def save_students(students):
    data = [student.to_dict() for student in students]

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)