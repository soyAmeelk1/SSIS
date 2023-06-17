import csv

def main_menu():
    while True:
        print("Main Menu")
        print("1. Student Data")
        print("2. Course Data")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu():
    while True:
        print("\n Student Menu")
        print("1. Write Student Data")
        print("2. List Student Data")
        print("3. Edit Student Data")
        print("4. Delete Student Data")
        print("5. Search Student by Year Data")
        print("6. Search Student by Name Data")
        print("7. Back to Main Menu")

        choice = input("\n Enter your choice (1-7): ")

        if choice == "1":
            write_student_data()
        elif choice == "2":
            list_student_data()
        elif choice == "3":
            edit_student_data()
        elif choice == "4":
            delete_student_data()
        elif choice == "5":
            search_student_year()
        elif choice == "6":
            search_student_name()
        elif choice == "7":
            break
        else:
            print("\n Invalid choice. Please try again.")

def course_menu():
    while True:
        print("\n Course Menu")
        print("1. Write Course Data")
        print("2. Read Course Data")
        print("3. Edit Course Data")
        print("4. Delete Course Data")
        print("5. List Courses")
        print("6. Search Course")
        print("7. Back to Main Menu")

        choice = input("\n Enter your choice (1-7): ")

        if choice == "1":
            write_course_data()
        elif choice == "2":
            list_course_data()
        elif choice == "3":
            edit_course_data()
        elif choice == "4":
            delete_course_data()
        elif choice == "5":
            search_courses()
        #elif choice == "6":
            #search_course()
        elif choice == "7":
            break
        else:
            print("\n Invalid choice. Please try again.")

def write_student_data():
    students_data = []
    while True:
        id_number = input("\n Enter ID Number (or 'q' to quit): ")
        if id_number == 'q':
            break
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        gender = input("Enter Gender: ")
        year = input("Enter Year: ")
        course = input("Enter Course: ")
        students_data.append([id_number, first_name, last_name, gender, year, course])

    with open('students.csv', 'a', newline='') as file:  # Use 'a' mode to append new data
        writer = csv.writer(file)
        writer.writerows(students_data)
    print("\n Student Data written successfully.")

def list_student_data():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print("\n Student Data listed successfully.")

def edit_student_data():
    id_number = input("\n Enter ID Number to edit: ")
    students_data = []
    found = False

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id_number:
                first_name = input("Enter new First Name: ")
                last_name = input("Enter new Last Name: ")
                gender = input("Enter new Gender: ")
                year = input("Enter new Year: ")
                course = input("Enter new Course: ")
                students_data.append([id_number, first_name, last_name, gender, year, course])
                found = True
            else:
                students_data.append(row)

    if found:
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students_data)
        print("Student data updated successfully.")
    else:
        print("Student not found.")

def delete_student_data():
    id_number = input("\n Enter ID Number to delete: ")
    students_data = []
    found = False

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id_number:
                found = True
            else:
                students_data.append(row)

    if found:
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students_data)
        print("Student data deleted successfully.")
    else:
        print("Student not found.")

def search_student_year():
    year = input("\n Enter the Year of student: ")
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == year:
                print(row)

def search_student_name():
    name = input("\n Enter the name of student: ")
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if name.lower() in row[1].lower() or name.lower() in row[2].lower():
                print(row)

def write_course_data():
    courses_data = []
    while True:
        id = input("\n Enter ID (or 'q' to quit): ")
        if id == 'q':
            break
        name = input("Enter Name: ")
        code = input("Enter Code: ")
        courses_data.append([id, name, code])

    with open('courses.csv', 'a', newline='') as file:  # Use 'a' mode to append new data
        writer = csv.writer(file)
        writer.writerows(courses_data)
    print("\n Course Data written successfully.")

def list_course_data():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print("\n Course Data listed successfully.")

def edit_course_data():
    id_number = input("\n Enter ID Number to edit: ")
    courses_data = []
    found = False

    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id_number:
                name = input("Enter new Name: ")
                code = input("Enter new Code: ")
                courses_data.append([id_number, name, code])
                found = True
            else:
                courses_data.append(row)

    if found:
        with open('courses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(courses_data)
        print("\n Course data updated successfully.")
    else:
        print("\n Course not found.")

def delete_course_data():
    id = input("\n Enter ID to delete: ")
    courses_data = []
    found = False

    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                found = True
            else:
                courses_data.append(row)

    if found:
        with open('courses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(courses_data)
        print("Course data deleted successfully.")
    else:
        print("Course not found.")

def search_courses():
    id = input("\n Enter the ID to search course: ")
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == id:
                print(row)

# Start the program
main_menu()
