import json

import storage
from student import Student
from student_manager import calculate_average, get_ranked_students, get_grade, delete_student, update_student, search_student 
from student_manager import get_grade 


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

def test_load_students_with_corrupted_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with open("students.json", "w") as file:
        file.write("This is not valid JSON")

    students = storage.load_students()

    assert students == []

def test_get_grade_rejects_invalid_grade(monkeypatch):
    inputs = iter(["25", "18"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    grade = get_grade(1)

    assert grade == 18

def test_get_grade_rejects_negative_grade(monkeypatch):
    inputs = iter(["-5", "15"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    grade = get_grade(1)

    assert grade == 15

def test_delete_student(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    delete_student(students)

    assert len(students) == 1
    assert students[0].id == 2
    assert students[0].name == "Ali"

def test_update_student(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    inputs = iter([
        "1",   # student ID
        "2",   # number of grades
        "15",  # grade 1
        "17"   # grade 2
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    update_student(students)

    assert students[0].name == "Lali"
    assert students[0].grades == [15.0, 17.0]
    assert students[0].average == 16.0

def test_search_student_found(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2"
    )

    search_student(students)

    output = capsys.readouterr().out

    assert "Name: Ali" in output
    assert "Average: 19.0" in output
    assert "Status: Passed" in output

def test_search_student_not_found(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    search_student(students)

    output = capsys.readouterr().out

    assert "Student not found" in output