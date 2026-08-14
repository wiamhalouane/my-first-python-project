import json

import storage
from student import Student
from student_manager import calculate_average, get_ranked_students


def test_calculate_average():
    grades = [10, 15, 20]
    result = calculate_average(grades)

    assert result == 15


def test_student_calculate_average():
    student = Student(1, "Lali", [12, 14])

    assert student.average == 13


def test_student_to_dict():
    student = Student(1, "Lali", [12, 14])

    data = student.to_dict()

    assert data["id"] == 1
    assert data["name"] == "Lali"
    assert data["grades"] == [12, 14]
    assert data["average"] == 13


def test_student_from_dict():
    data = {
        "id": 1,
        "name": "Lali",
        "grades": [12, 14],
        "average": 13
    }

    student = Student.from_dict(data)

    assert student.id == 1
    assert student.name == "Lali"
    assert student.grades == [12, 14]
    assert student.average == 13


def test_get_ranked_students():
    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20]),
        Student(3, "Sara", [15, 16])
    ]

    ranked_students = get_ranked_students(students)

    assert ranked_students[0].name == "Ali"
    assert ranked_students[1].name == "Sara"
    assert ranked_students[2].name == "Lali"


def test_save_and_load_students(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    storage.save_students(students)

    loaded_students = storage.load_students()

    assert len(loaded_students) == 2
    assert loaded_students[0].name == "Lali"
    assert loaded_students[0].average == 13
    assert loaded_students[1].name == "Ali"
    assert loaded_students[1].average == 19