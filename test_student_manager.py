import storage

from student_manager import calculate_average
from student_manager import get_ranked_students

def test_calculate_average():
    grades = [10, 15, 20]

    result = calculate_average(grades)

    assert result == 15


def test_calculate_average_with_two_grades():
    grades = [12, 14]

    result = calculate_average(grades)

    assert result == 13


def test_calculate_average_with_same_grades():
    grades = [10, 10, 10]

    result = calculate_average(grades)

    assert result == 10


def test_save_and_load_students(tmp_path, monkeypatch):
    test_file = tmp_path / "students.json"

    monkeypatch.chdir(tmp_path)

    students = [
        {
            "id": 1,
            "name": "Sara",
            "grades": [15, 18],
            "average": 16.5
        }
    ]

    storage.save_students(students)

    loaded_students = storage.load_students()

    assert loaded_students == students

def test_get_ranked_students():
    students = [
        {
            "id": 1,
            "name": "Lali",
            "grades": [12, 14],
            "average": 13
        },
        {
            "id": 2,
            "name": "Ali",
            "grades": [18, 19],
            "average": 18.5
        },
        {
            "id": 3,
            "name": "Sara",
            "grades": [15, 16],
            "average": 15.5
        }
    ]

    ranked_students = get_ranked_students(students)

    assert ranked_students[0]["name"] == "Ali"
    assert ranked_students[1]["name"] == "Sara"
    assert ranked_students[2]["name"] == "Lali"

def test_load_students_with_invalid_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with open("students.json", "w") as file:
        file.write("This is not valid JSON")

    students = storage.load_students()

    assert students == []