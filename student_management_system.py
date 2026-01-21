students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    level = input("Enter Level: ")

    students[student_id] = {
        "name": name,
        "course": course,
        "level": level
    }
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No students available.\n")
        return

    for student_id, details in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Course: {details['course']}")
        print(f"Level: {details['level']}\n")

def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        students[student_id]["name"] = input("Enter new name: ")
        students[student_id]["course"] = input("Enter new course: ")
        students[student_id]["level"] = input("Enter new level: ")
        print("Student updated successfully.\n")
    else:
        print("Student not found.\n")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")

def main_menu():
    while True:
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.\n")

main_menu()
