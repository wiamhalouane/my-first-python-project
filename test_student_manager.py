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

def test_main_exit(monkeypatch, capsys):
    import main

    monkeypatch.setattr(
        "main.load_students",
        lambda: []
    )

    inputs = iter(["7"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    main.main()

    output = capsys.readouterr().out

    assert "Student Grade Manager" in output
    assert "Goodbye!" in output
def test_add_student(monkeypatch):
    students = []

    inputs = iter([
        "Lali",  # student name
        "2",     # number of grades
        "15",    # grade 1
        "17"     # grade 2
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    monkeypatch.setattr(
        "student_manager.save_students",
        lambda students: None
    )

    from student_manager import add_student

    add_student(students)

    assert len(students) == 1
    assert students[0].id == 1
    assert students[0].name == "Lali"
    assert students[0].grades == [15.0, 17.0]
    assert students[0].average == 16.0
def test_add_student_assigns_next_id(monkeypatch):
    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    inputs = iter([
        "Sara",  # student name
        "2",     # number of grades
        "16",    # grade 1
        "18"     # grade 2
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    monkeypatch.setattr(
        "student_manager.save_students",
        lambda students: None
    )

    from student_manager import add_student

    add_student(students)

    assert len(students) == 3
    assert students[2].id == 3
    assert students[2].name == "Sara"
    assert students[2].grades == [16.0, 18.0]
    assert students[2].average == 17.0
def test_show_students(capsys):
    from student_manager import show_students

    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    show_students(students)

    output = capsys.readouterr().out

    assert "ID: 1" in output
    assert "Name: Lali" in output
    assert "Grades: [12, 14]" in output
    assert "Average: 13.0" in output
    assert "Status: Passed" in output

    assert "ID: 2" in output
    assert "Name: Ali" in output
    assert "Grades: [18, 20]" in output
    assert "Average: 19.0" in output
    assert "Status: Passed" in output
def test_show_students_empty(capsys):
    from student_manager import show_students

    students = []

    show_students(students)

    output = capsys.readouterr().out

    assert "No students found" in output
def test_rank_students(capsys):
    from student_manager import rank_students

    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20]),
        Student(3, "Sara", [15, 16])
    ]

    rank_students(students)

    output = capsys.readouterr().out

    assert "Student Ranking" in output

    assert "Rank: 1" in output
    assert "Name: Ali" in output
    assert "Average: 19.0" in output

    assert "Rank: 2" in output
    assert "Name: Sara" in output
    assert "Average: 15.5" in output

    assert "Rank: 3" in output
    assert "Name: Lali" in output
    assert "Average: 13.0" in output
def test_rank_students_empty(capsys):
    from student_manager import rank_students

    students = []

    rank_students(students)

    output = capsys.readouterr().out

    assert "No students found" in output
def test_delete_student_not_found(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    delete_student(students)

    output = capsys.readouterr().out

    assert "Student not found" in output
    assert len(students) == 2
def test_update_student_not_found(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14]),
        Student(2, "Ali", [18, 20])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    update_student(students)

    output = capsys.readouterr().out

    assert "Student not found" in output
    assert students[0].grades == [12, 14]
    assert students[1].grades == [18, 20]
def test_search_student_invalid_id(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "abc"
    )

    search_student(students)

    output = capsys.readouterr().out

    assert "Please enter a valid ID." in output
def test_delete_student_invalid_id(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "abc"
    )

    delete_student(students)

    output = capsys.readouterr().out

    assert "Please enter a valid ID." in output
    assert len(students) == 1

def test_update_student_invalid_id(monkeypatch, capsys):
    students = [
        Student(1, "Lali", [12, 14])
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "abc"
    )

    update_student(students)

    output = capsys.readouterr().out

    assert "Please enter a valid ID." in output
    assert students[0].grades == [12, 14]
def test_add_student_rejects_invalid_number_of_grades(monkeypatch):
    students = []

    inputs = iter([
        "Lali",  # student name
        "0",     # invalid number of grades
        "2",     # valid number of grades
        "15",    # grade 1
        "17"     # grade 2
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    monkeypatch.setattr(
        "student_manager.save_students",
        lambda students: None
    )

    from student_manager import add_student

    add_student(students)

    assert len(students) == 1
    assert students[0].name == "Lali"
    assert students[0].grades == [15.0, 17.0]
    assert students[0].average == 16.0