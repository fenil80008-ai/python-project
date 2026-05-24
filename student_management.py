import json
import os

FILE_NAME = "students.json"

# Load existing data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
else:
    students = []

# Save data function
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add Student
def add_student():

    roll = input("Enter Roll Number : ")

    # Check duplicate roll number
    for s in students:
        if s['roll'] == roll:
            print("❌ Roll Number Already Exists")
            return

    name = input("Enter Student Name : ")
    age = input("Enter Age : ")
    course = input("Enter Course : ")
    marks = float(input("Enter Marks : "))

    # Grade Calculation
    if marks >= 90:
        grade = 'A+'
    elif marks >= 75:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 40:
        grade = 'C'
    else:
        grade = 'Fail'

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    save_data()

    print("✅ Student Added Successfully")

# View Students
def view_students():

    if len(students) == 0:
        print("❌ No Records Found")
        return

    print("\n========== STUDENT RECORDS ==========")

    for s in students:
        print(f"""
Roll Number : {s['roll']}
Name        : {s['name']}
Age         : {s['age']}
Course      : {s['course']}
Marks       : {s['marks']}
Grade       : {s['grade']}
---------------------------------------
""")

# Search Student
def search_student():

    roll = input("Enter Roll Number : ")

    for s in students:
        if s['roll'] == roll:

            print("\n✅ Student Found")
            print(f"""
Name   : {s['name']}
Age    : {s['age']}
Course : {s['course']}
Marks  : {s['marks']}
Grade  : {s['grade']}
""")
            return

    print("❌ Student Not Found")

# Update Student
def update_student():

    roll = input("Enter Roll Number To Update : ")

    for s in students:

        if s['roll'] == roll:

            print("\nLeave blank if no change")

            new_name = input("Enter New Name : ")
            new_age = input("Enter New Age : ")
            new_course = input("Enter New Course : ")

            if new_name:
                s['name'] = new_name

            if new_age:
                s['age'] = new_age

            if new_course:
                s['course'] = new_course

            save_data()

            print("✅ Student Updated Successfully")
            return

    print("❌ Student Not Found")

# Delete Student
def delete_student():

    roll = input("Enter Roll Number To Delete : ")

    for s in students:

        if s['roll'] == roll:
            students.remove(s)
            save_data()

            print("✅ Student Deleted Successfully")
            return

    print("❌ Student Not Found")

# Topper Student
def topper_student():

    if len(students) == 0:
        print("❌ No Records Found")
        return

    topper = max(students, key=lambda x: x['marks'])

    print("\n🏆 TOPPER STUDENT")
    print(f"""
Name   : {topper['name']}
Marks  : {topper['marks']}
Grade  : {topper['grade']}
""")

# Main Program
while True:

    print("""
=========== SMART STUDENT MANAGEMENT SYSTEM ===========
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Topper
7. Exit
=======================================================
""")

    choice = input("Enter Your Choice : ")

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
        topper_student()

    elif choice == '7':
        print("🙏 Thank You For Using The System")
        break

    else:
        print("❌ Invalid Choice")
