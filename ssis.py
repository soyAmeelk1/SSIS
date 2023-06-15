import csv

def write_student_data():
    students_data = []
    while True:
        id_number = input("Enter ID Number (or 'q' to quit): ")
        if id_number == 'q':
            break
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        gender = input("Enter Gender: ")
        year = input("Enter Year: ")
        course = input("Enter Course: ")
        students_data.append([id_number, first_name, last_name, gender, year, course])

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students_data)

def write_course_data():
    courses_data = []
    while True:
        id = input("Enter ID (or 'q' to quit): ")
        if id == 'q':
            break
        name = input("Enter Name: ")
        code = input("Enter Code: ")
        courses_data.append([id, name, code])

    with open('courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(courses_data)

def read_student_data():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def read_course_data():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def edit_student_data():
    id_number = input("Enter ID Number to edit: ")
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
    id_number = input("Enter ID Number to delete: ")
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

def list_students_by_year(year):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == year:
                print(row)

def search_students_by_name(name):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if name.lower() in row[1].lower() or name.lower() in row[2].lower():
                print(row)

# Menu for data manipulation
while True:
    print("\n--- Menu ---")
    print("1. Write Student Data")
    print("2. Write Course Data")
    print("3. Read Student Data")
    print("4. Read Course Data")
    print("5. Edit Student Data")
    print("6. Delete Student Data")
    print("7. List Students by Year")
    print("8. Search Students by Name")
    print("9. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        write_student_data()
    elif choice == '2':
        write_course_data()
    elif choice == '3':
        read_student_data()
    elif choice == '4':
        read_course_data()
    elif choice == '5':
        edit_student_data()
    elif choice == '6':
        delete_student_data()
    elif choice == '7':
        year = input("Enter Year: ")
        list_students_by_year(year)
    elif choice == '8':
        name = input("Enter Name: ")
        search_students_by_name(name)
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")
