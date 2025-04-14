from student_db import add_student, view_students, update_student, delete_student, close_db

def show_menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        student_id = int(input("Student ID: "))
        fname = input("First Name: ")
        lname = input("Last Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        email = input("Email: ")
        add_student((student_id, fname, lname, age, grade, email))
        print("✅ Student added!")

    elif choice == "2":
        students = view_students()
        for s in students:
            print(s)

    elif choice == "3":
        student_id = int(input("Enter Student ID to update: "))
        field = input("Enter field to update (FirstName, LastName, Age, Grade, Email): ")
        new_value = input("Enter new value: ")
        update_student(student_id, field, new_value)
        print("✅ Student updated!")

    elif choice == "4":
        student_id = int(input("Enter Student ID to delete: "))
        delete_student(student_id)
        print("🗑️ Student deleted!")

    elif choice == "5":
        close_db()
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
