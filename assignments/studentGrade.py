"""
Student Grade Tracker

- Uses a dictionary where:
    keys   = student names
    values = list of test scores

Functions:
1. Add a new student
2. Add a grade for an existing student
3. Calculate average grade for each student
4. Find the student with the highest average
5. Display all students and their grades in a formatted table
"""

# Student data storage
students = {}

# Function to add a new student
def add_student(name):
    if name in students:
        print(f" {name} already exists.")
    else:
        students[name] = []
        print(f" Student {name} added.")

# Function to add a grade
def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f" Added grade {grade} for {name}.")
    else:
        print(f" Student {name} not found.")

# Function to calculate average grade
def calculate_average(name):
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        return 0

# Function to find top student
def top_student():
    if not students:
        return None
    return max(students, key=lambda s: calculate_average(s))

# Function to display all students
def display_students():
    print("\nStudent Grade Report")
    print("-" * 40)
    print(f"{'Name':<15}{'Grades':<20}{'Average'}")
    print("-" * 40)
    for name, grades in students.items():
        avg = calculate_average(name)
        print(f"{name:<15}{str(grades):<20}{avg:.2f}")
    print("-" * 40)


# -------- Console Menu --------
while True:
    print("\nStudent Grade Tracker Menu:")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Show All Students")
    print("4. Show Top Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        add_student(name)

    elif choice == "2":
        name = input("Enter student name: ")
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                add_grade(name, grade)
            else:
                print(" Grade must be between 0 and 100.")
        except ValueError:
            print(" Invalid input. Please enter a number.")

    elif choice == "3":
        display_students()

    elif choice == "4":
        top = top_student()
        if top:
            print(f" Top Student: {top} with average {calculate_average(top):.2f}")
        else:
            print(" No students available.")

    elif choice == "5":
        print("Exiting program. Goodbye ")
        break

    else:
        print(" Invalid choice. Please select 1-5.")





