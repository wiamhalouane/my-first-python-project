from student_manager import calculate_average
from storage import save_students, load_students


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
    students = [
        {
            "id": 1,
            "name": "Sara",
            "grades": [15, 18],
            "average": 16.5
        }
    ]

    test_file = tmp_path / "test_students.json"

    def test_save(students):
        import json

        with open(test_file, "w") as file:
            json.dump(students, file, indent=4)

    def test_load():
        import json

        with open(test_file, "r") as file:
            return json.load(file)

    test_save(students)
    loaded_students = test_load()

    assert loaded_students == students