from data import save_students_to_csv, load_students_from_csv
from menu import show_main_menu
from actions import (
    add_student,
    update_student,
    delete_student,
    show_top_3_students,
    show_section_average,
    display_student_info
)

FILENAME = "students.csv"
students = load_students_from_csv(FILENAME)

def main():
    while True:
        option = show_main_menu()

        if option == 1:
            add_student(students)  # <<< THIS IS WHERE YOU CALL IT
            save_students_to_csv(students, FILENAME)

        elif option == 2:
            display_student_info(students)

        elif option == 3:
            update_student(students)
            save_students_to_csv(students, FILENAME)

        elif option == 4:
            delete_student(students)
            save_students_to_csv(students, FILENAME)

        elif option == 5:
            show_top_3_students(students)

        elif option == 6:
            show_section_average(students)

        elif option == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()  