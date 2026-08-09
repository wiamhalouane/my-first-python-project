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

    student = {
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
        print("Name:", student["name"])
        print("Grades:", student["grades"])
        print("Average:", student["average"])

        if student["average"] >= 10:
            print("Status: Passed")
        else:
            print("Status: Failed")


load_students()

while True:

    print("\nStudent Grade Manager")
    print("1. Add student")
    print("2. Show students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")