from storage import load_students

from student_manager import (
    add_student,
    show_students,
    search_student,
    delete_student,
    update_student,
    rank_students
)


def main():
    students = load_students()

    while True:

        print("\nStudent Grade Manager")
        print("1. Add student")
        print("2. Show students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Update student")
        print("6. Student ranking")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            update_student(students)

        elif choice == "6":
            rank_students(students)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()