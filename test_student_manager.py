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