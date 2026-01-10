from menu import show_update_menu, show_grades_menu
import re

class Student:
    def __init__(self, first_name, last_name, section,
                second_name="", second_last_name="", grades=None):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.second_last_name = second_last_name
        self.section = section
        self.grades = grades if grades else {
            "spanish": 0,
            "english": 0,
            "social studies": 0,
            "science": 0
        }

    # Dictionary
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "last_name": self.last_name,
            "second_last_name": self.second_last_name,
            "section": self.section,
            "grades": self.grades
        }

    # Para imprimir el nombre completo
    def full_name(self):
        return f"{self.first_name} {self.second_name} {self.last_name} {self.second_last_name}".strip()

def get_student_info():
    print("\n--- Add New Student ---")

    # Get and validate first name
    while True:
        first_name = input("First name (required): ").strip()
        if not first_name.isalpha() or len(first_name) < 2:
            print("First name must be at least 2 letters and contain only letters.")
        else:
            break

    # Get second name (optional, no validation)
    second_name = input("Second name (optional): ").strip()

    # Get and validate last name
    while True:
        last_name = input("Last name (required): ").strip()
        if not last_name.isalpha() or len(last_name) < 2:
            print("Last name must be a valid name and contain only letters.")
        else:
            break

    # Get second last name (optional, no validation)
    second_last_name = input("Second last name (optional): ").strip()

    #Valid section
    section = get_valid_section()

    # Function to get a valid grade
    def get_valid_grade(subject):
        while True:
            grade_input = input(f"{subject} grade (1-100): ").strip()
            if grade_input.isdigit():
                grade = int(grade_input)
                if 1 <= grade <= 100:
                    return grade
            print(f"Invalid input. Enter a number between 1 and 100 for {subject}.")

    # Get grades
    grades = {
        "spanish" : get_valid_grade("spanish"),
        "english" : get_valid_grade("english"),
        "social_studies" : get_valid_grade("social studies"),
        "science" : get_valid_grade("science")
    }

    return Student(first_name, last_name, section, second_name, second_last_name, grades)
    # Return the student as a dictionary
    # return {
    #     "first_name": first_name,
    #     "second_name": second_name,
    #     "last_name": last_name,
    #     "second_last_name": second_last_name,
    #     "section": section,
    #     "grades": {
    #         "spanish": spanish,
    #         "english": english,
    #         "social studies": social_studies,
    #         "science": science
    #     }
    # }

def add_student(students):
    student = get_student_info()
    students.append(student)
    print("\nStudent added successfully.")

    print(students)

def get_valid_section():
    while True:
        section = input("Section (e.g. 11B): ").strip().upper()
        if re.match(r"^(1[0-1]|[1-9])[A-H]$", section):
            return section
        else:
            print("Section must be a number from 1 to 11 followed by a letter A-H (e.g. 8C).")


def find_student(students):
    if not check_students_exist(students):
        return
    
    while True:
        print("\n--- Find Student ---")
        
        while True:
            first_name = input("Enter first name: ").strip()
            if first_name.isalpha():
                break
            else:
                print("First name must contain only letters.")
        
        while True:
            last_name = input("Enter last name: ").strip()
            if last_name.isalpha():
                break
            else:
                print("Last name must contain only letters.")

        section = get_valid_section()

        matches = []
        for student in students:
            if (student.first_name.lower() == first_name.lower() and
                student.last_name.lower() == last_name.lower() and
                student.section.upper() == section.upper()):
                matches.append(student)

        if not matches:
            print("No matching students found.")
            retry = input("Do you want to try again? (y/n): ").strip().lower()
            if retry == 'y':
                continue
            elif retry == 'n':
                return
            else:
                print("Invalid input, Please enter 'y' or 'n")

        if len(matches) == 1:
            return matches[0]

        print(f"\nFound {len(matches)} matching students:")
        for idx, student in enumerate(matches, start=1):
            full_name = student.full_name()
            print(f"{idx}. {full_name.strip()}")

        while True:
            try:
                choice = int(input("Please select a student from the list by entering the corresponding number: "))
                if 1 <= choice <= len(matches):
                    return matches[choice - 1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

# Actualizar estudiante
def update_student(students):
    print("\n--- Update Student ---")
    student = find_student(students)
    if not student:
        return

    while True:
        choice = show_update_menu()
        if choice == 1:
            update_name(student)  # Esta función puedes agregarla más adelante
        elif choice == 2:
            update_section(student)
        elif choice == 3:
            update_grades(student)
        elif choice == 4:
            print("Returning to main menu.")
            break

# Actualizar sección
def update_section(student):
    print("\n--- Update Section ---")
    student.section = get_valid_section()
    print("Section updated successfully.")

# Actualizar notas
def update_grades(student):
    while True:
        choice = show_grades_menu()
        if choice == 1:
            update_single_grade(student, 'spanish')
        elif choice == 2:
            update_single_grade(student, 'english')
        elif choice == 3:
            update_single_grade(student, 'social studies')
        elif choice == 4:
            update_single_grade(student, 'science')
        elif choice == 5:
            print("Returning to update menu.")
            break

# Validación de nota individual
def update_single_grade(student, subject_key):
    while True:
        try:
            grade = int(input(f"Enter new grade for {subject_key}: "))
            if 1 <= grade <= 100:
                student.grades[subject_key] = grade
                print(f"{subject_key} updated successfully.")
                break
            else:
                print("Grade must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def update_name(student):
    print("\n--- Update Full Name ---")
    print(f"Current Name: {student.full_name()}")

    new_first_name = input("Enter new first name (leave blank to keep current): ").strip()
    new_second_name = input("Enter new second name (leave blank to keep current): ").strip()
    new_last_name = input("Enter new last name (leave blank to keep current): ").strip()
    new_second_last_name = input("Enter new second last name (leave blank to keep current): ").strip()

    if new_first_name:
        student.first_name = new_first_name
    if new_second_name:
        student.second_name = new_second_name
    else:
        student.second_name = student.get('second_name', '')  # Ensure the field exists
    if new_last_name:
        student.last_name = new_last_name
    if new_second_last_name:
        student.second_last_name = new_second_last_name
    else:
        student.second_last_name = student.get('second_last_name', '')  # Ensure the field exists

    print("Student full name updated successfully.")

#calculate average
def calculate_student_average(student):
    grades = student.grades
    if not grades:
        print("no grades")
        return 0
    total = sum(grades.values())
    return total / len(grades)
    
def show_top_3_students(students):
    print("\n--- Top 3 Students ---")
    if not check_students_exist(students):
        return
    print(students)
    #students.clear()
    # Calculate averages
    student_averages = []
    for student in students:
        avg = calculate_student_average(student)
        student_averages.append((student, avg))

    # Sort by average descending
    top_students = sorted(student_averages, key=lambda x: x[1], reverse=True)[:3]

    for student, avg in top_students:
        print(f"{student.full_name()} - Section: {student.section} - Average: {avg:.2f}")


def show_section_average(students):
    print("\n--- Average per section ---")
    if not check_students_exist(students):
        return
    
    while True:
        section = get_valid_section()

    # Filter students in that section
        section_students = [s for s in students if s.section.upper() == section]
    
        if not section_students:
            print(f"\nNo students found in section {section}.")
            retry = input("Do you want to try another section? (y/n): ").strip().lower()
            if retry == 'y':
                continue
            else:
                return
        else:
    # Calculate total average
            total = 0
            for student in section_students:
                total += calculate_student_average(student)

            section_avg = total / len(section_students)
            print(f"The average for section {section} is: {section_avg:.2f}")
            return
    
def delete_student(students):
    print("\n--- Delete Student ---")
    
    student = find_student(students)  # Reuse the existing find_student function

    if not student:
        return  # No match found or user cancelled selection

    # Confirm deletion
    full_name = student.full_name()
    confirm = input(f"Are you sure you want to delete {full_name}? (y/n): ").strip().lower()
    
    if confirm == 'y':
        students.remove(student)
        print(f"{full_name} has been deleted.")
    else:
        print("Deletion cancelled.")

def display_student_info(students):
    print("\n--- Show Student Information ---")
    
    if not students:
        print("No students found.")
        return
    
    for i, student in enumerate(students, 1):
        print(f"\n--- Student #{i} ---")
        print(f"Name: {student.fullname()}")
        print(f"Section: {student.section}")
        print("Grades:")
        for subject, grade in student.grades.items():
            print(f"  {subject}: {grade}")
    # # print("\n--- Show Student Information ---")
    # # student = find_student(students)
    # # if not student:
    #     return
    
    # print("\n--- Student Information ---")
    # print(f"Name: {student['first_name']} {student.get('second_name', '')} {student['last_name']} {student.get('second_last_name', '')}")
    # print(f"Section: {student['section']}")
    # print("\nGrades:")
    # for subject, grade in student['grades'].items():
    #     print(f"  {subject}: {grade}")

def check_students_exist(students):
    if not students:
        print("\nThere are no students in the system to load, Please add students first.")
        return False
    return True