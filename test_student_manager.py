import storage

from student_manager import calculate_average


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