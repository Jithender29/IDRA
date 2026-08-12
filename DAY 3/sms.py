# STUDENT MANAGEMENT SYSTEM

students = []

def add_student():
    student ={}
    student['ID']= input("Enter student ID: ")
    student['NAME']= input("Enter Student Name: ")
    student['Age']= int(input("Enter Student Age: "))
    student['Course']= input("Enter Student Course: ")
    student['Marks']= float(input("Enter Student Marks: "))
    students.appen(student)
    print("Student Added successfully\n")

def view_students():
    if not students:
        print("No students found\n")
        return
    print("\n----------Student Records--------\n")
    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}, Marks: {student['Marks']}\n")

def search_student():
    key = input("Enter Student ID or Name: ")
    found = False
    for student in students:
        if student['ID']== key or student['Name'].lower() == key.lower():
            print(f" FOUND: ID:{student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}, Marks: {student['Marks']}\n")
            found = True
            break
        if not found:
            print("No student found in records\n")

def update_student():
    sid = input("Enter student id to update: ")
    for student in students:
        if student['ID']== sid:
            name = input(f"Name ({student['Name']}): ")
            age = input(f"Age ({student['Age']}): ")
            course = input(f"Course ({student['Course']}): ")
            marks = input(f"Marks ({student['Marks']}): ")
            if name: student['Name'] = name
            if age: student['Age'] = int(age)
            if course: student['Course'] = course
            if marks: student['Marks'] = float(marks)
            print("Student record updated successfully\n")
            return
    print("Student ID not found.\n")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for student in students:
        if student['ID'] == sid:
            students.remove(student)
            print("Student record deleted successfully\n")
            return
    print("Student ID not found\n")


while True:
    print("--------Student Management System --------\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
        
    choice = input("Enter your choice (1-6): ")
        
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting Student Management System. Goodbye")
        break
    else:
        print("Invalid choice. Please try again.\n")

    