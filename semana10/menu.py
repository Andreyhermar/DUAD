# menu.py

def show_main_menu():
    print("\n--- Main Menu ---")
    print("1. Add Student")
    print("2. Show student information")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Top 3 Students")
    print("6. Average per section")
    print("7. Exit Program")
    return get_user_choice(7)

def show_update_menu():
    print("\n--- Update Menu ---")
    print("1. Update Name")
    print("2. Update Section")
    print("3. Update Grades")
    print("4. Exit")
    return get_user_choice(4)

def show_grades_menu():
    print("\n--- Grades Menu ---")
    print("1. Spanish")
    print("2. English")
    print("3. Social Studies")
    print("4. Science")
    print("5. Exit")
    return get_user_choice(5)

def get_user_choice(max_option):
    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= max_option:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_option}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
