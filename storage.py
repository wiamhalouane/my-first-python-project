import json


def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: students.json is empty or corrupted.")
        return []


def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)