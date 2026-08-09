import json

students = []


def calculate_average(grades):
    return sum(grades) / len(grades)


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student():

    name = input("Enter student name: ")

    number_of_grades = int(input("How many grades? "))

    grades = []

    for i in range(number_of_grades):
        grade = float(input(f"Enter grade {i+1}: "))
        grades.append(grade)

    average = calculate_average(grades)

    student_id = len(students) + 1

    student = {
        "id": student_id,
        "name": name,
        "grades": grades,
        "average": average
    }

    students.append(student)

    save_students()

    print("Student added successfully!")

def show_students():

    if len(students) == 0:
        print("No students found")
        return

    for student in students:
        print("----------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Grades:", student["grades"])
        print("Average:", student["average"])

        if student["average"] >= 10:
            print("Status: Passed")
        else:
            print("Status: Failed")

def search_student():

    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:
            print("----------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Grades:", student["grades"])
            print("Average:", student["average"])

            if student["average"] >= 10:
                print("Status: Passed")
            else:
                print("Status: Failed")

            return

    print("Student not found")

def delete_student():

    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found")

def update_student():
    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:

            print("Current grades:", student["grades"])

            number_of_grades = int(input("How many grades? "))

            grades = []

            for i in range(number_of_grades):
                grade = float(input(f"Enter new grade {i+1}: "))
                grades.append(grade)

            student["grades"] = grades
            student["average"] = calculate_average(grades)

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found")


load_students()

while True:

    print("\nStudent Grade Manager")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Update student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")