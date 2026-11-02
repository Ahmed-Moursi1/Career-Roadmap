"""Student Management System - Day 1 Python project."""
students = []


def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_age():
    while True:
        try:
            age = int(input("Age: "))
            if age > 0:
                return age
            print("Age must be greater than zero.")
        except ValueError:
            print("Enter a valid whole number.")


def ask_grades():
    while True:
        raw = input("Grades (0-100), separated by spaces; press Enter for none: ").strip()
        if not raw:
            return []
        try:
            grades = [float(x) for x in raw.split()]
            if all(0 <= grade <= 100 for grade in grades):
                return grades
            print("Every grade must be between 0 and 100.")
        except ValueError:
            print("Enter numbers separated by spaces.")


def average(grades):
    return sum(grades) / len(grades) if grades else None


def find_student(name):
    for student in students:
        if student["name"].casefold() == name.casefold():
            return student
    return None


def add_student():
    print("\n--- Add Student ---")
    name = ask_text("Name: ")
    if find_student(name):
        print("A student with that name already exists.")
        return
    students.append({"name": name, "age": ask_age(), "grades": ask_grades()})
    print("Student added successfully.")


def show_students():
    print("\n--- Students ---")
    if not students:
        print("No students found.")
        return
    for number, student in enumerate(students, 1):
        avg = average(student["grades"])
        avg_text = f"{avg:.2f}" if avg is not None else "No grades"
        print(f'{number}. {student["name"]} | Age: {student["age"]} | '
              f'Grades: {student["grades"]} | Average: {avg_text}')


def search_student():
    name = ask_text("Student name to search: ")
    student = find_student(name)
    if not student:
        print("Student not found.")
        return
    avg = average(student["grades"])
    print(f'Name: {student["name"]}\nAge: {student["age"]}')
    print(f'Grades: {student["grades"]}')
    print(f'Average: {avg:.2f}' if avg is not None else "Average: No grades")


def update_student():
    name = ask_text("Current student name: ")
    student = find_student(name)
    if not student:
        print("Student not found.")
        return
    new_name = ask_text("New name: ")
    existing = find_student(new_name)
    if existing and existing is not student:
        print("That name is already used.")
        return
    student["name"] = new_name
    student["age"] = ask_age()
    student["grades"] = ask_grades()
    print("Student updated successfully.")


def delete_student():
    name = ask_text("Student name to delete: ")
    student = find_student(name)
    if not student:
        print("Student not found.")
        return
    students.remove(student)
    print("Student deleted successfully.")


def show_class_average():
    grades = []
    for student in students:
        grades.extend(student["grades"])
    avg = average(grades)
    print(f"Class average: {avg:.2f}" if avg is not None
          else "There are no grades to calculate an average.")


def main():
    actions = {
        "1": add_student,
        "2": show_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
        "6": show_class_average,
    }
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add student")
        print("2. Show all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Calculate class average")
        print("0. Exit")
        choice = input("Choose (0-6): ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Choose a number from 0 to 6.")


if __name__ == "__main__":
    main()
