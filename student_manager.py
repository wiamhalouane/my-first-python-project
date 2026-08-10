from storage import save_students

def calculate_average(grades):
    return sum(grades) / len(grades)


def get_grade(grade_number):
    while True:
        try:
            grade = float(input(f"Enter grade {grade_number}: "))

            if 0 <= grade <= 20:
                return grade

            print("Grade must be between 0 and 20.")

        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    name = input("Enter student name: ")

    while True:
        try:
            number_of_grades = int(input("How many grades? "))

            if number_of_grades > 0:
                break

            print("Number of grades must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    grades = []

    for i in range(number_of_grades):
        grade = get_grade(i + 1)
        grades.append(grade)

    average = calculate_average(grades)

    if students:
        student_id = max(student["id"] for student in students) + 1
    else:
        student_id = 1

    student = {
        "id": student_id,
        "name": name,
        "grades": grades,
        "average": average
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def show_students(students):
    if len(students) == 0:
        print("No students found")
        return

    for student in students:
        print("----------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Grades:", student["grades"])
        print("Average:", round(student["average"], 2))

        if student["average"] >= 10:
            print("Status: Passed")
        else:
            print("Status: Failed")

def get_ranked_students(students):
    return sorted(
        students,
        key=lambda student: student["average"],
        reverse=True
    )


def rank_students(students):
    if len(students) == 0:
        print("No students found")
        return

    ranked_students = get_ranked_students(students)

    print("\nStudent Ranking")

    for position, student in enumerate(ranked_students, start=1):
        print("----------------")
        print("Rank:", position)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Average:", round(student["average"], 2))

def search_student(students):
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for student in students:
        if student["id"] == student_id:
            print("----------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Grades:", student["grades"])
            print("Average:", round(student["average"], 2))

            if student["average"] >= 10:
                print("Status: Passed")
            else:
                print("Status: Failed")

            return

    print("Student not found")


def delete_student(students):
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found")


def update_student(students):
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for student in students:
        if student["id"] == student_id:

            print("Current grades:", student["grades"])

            while True:
                try:
                    number_of_grades = int(input("How many grades? "))

                    if number_of_grades > 0:
                        break

                    print("Number of grades must be greater than 0.")

                except ValueError:
                    print("Please enter a valid number.")

            grades = []

            for i in range(number_of_grades):
                grade = get_grade(i + 1)
                grades.append(grade)

            student["grades"] = grades
            student["average"] = calculate_average(grades)

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found")
