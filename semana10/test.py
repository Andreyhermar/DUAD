def calculate_student_average(student):
    grades = student.get('grades', {})
    if not grades:
        print("no grades")
        return 0
    total = grades.get('spanish', 0) + grades.get('english', 0) + grades.get('social studies', 0) + grades.get('science', 0)
    average = total / 4
    print(f"Grades: {grades}, Average: {average}")
    return average

# One test student
student = {
    'first_name': 'Ana',
    'last_name': 'Martínez',
    'section': '11A',
    'grades': {
        'spanish': 90,
        'english': 85,
        'social studies': 88,
        'science': 92
    }
}

# Call the function
calculate_student_average(student)