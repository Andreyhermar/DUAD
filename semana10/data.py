import csv
import os

def save_students_to_csv(students, filename):
    if not students:
        print("\nNo hay estudiantes para exportar.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "first_name", "second_name", "last_name", "second_last_name",
            "section", "spanish", "english", "social_studies", "science"
        ])
        writer.writeheader()

        for student in students:
            row = {
                "first_name": student["first_name"],
                "second_name": student.get("second_name", ""),
                "last_name": student["last_name"],
                "second_last_name": student.get("second_last_name", ""),
                "section": student["section"],
                "spanish": student["grades"]["spanish"],
                "english": student["grades"]["english"],
                "social_studies": student["grades"]["social studies"],
                "science": student["grades"]["science"]
            }
            writer.writerow(row)
    print(f"\n✅ {len(students)} estudiantes exportados a {filename}")

def load_students_from_csv(filename):
    students = []
    if not os.path.exists(filename):
        print("\nNo students have been added to the database. A new file will be created when students are added.")
        return students  # Empty list
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "first_name": row["first_name"],
                    "second_name": row["second_name"],
                    "last_name": row["last_name"],
                    "second_last_name": row["second_last_name"],
                    "section": row["section"],
                    "grades": {
                        "spanish": int(row["spanish"]),
                        "english": int(row["english"]),
                        "social studies": int(row["social_studies"]),
                        "science": int(row["science"])
                    }
                }
                students.append(student)
        print(f"\n✅ {len(students)} estudiantes importados desde {filename}")
    except Exception as e:
        print(f"⚠️ Error al cargar estudiantes: {e}")
    # except FileNotFoundError: 
    #     print("There is no students list previously created, We'll start with a new students list.") # First run, file doesn't exist yet
    return students