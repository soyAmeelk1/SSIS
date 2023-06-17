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
        print("2. List Course Data")
        print("3. Edit Course Data")
        print("4. Delete Course Data")
        print("5. Search Course")
        print("6. Back to Main Menu")

        choice = input("\n Enter your choice (1-6): ")

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
        elif choice == "6":
            break
        else:
            print("\n Invalid choice. Please try again.")

def write_student_data():
    while True:
        id_number = input("\n Enter ID Number (or 'q' to quit): ")
        if id_number == 'q':
            break

        # Check if student with the same ID already exists
        if is_student_exists(id_number):
            print("This student already exists.")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        gender = input("Enter Gender: ")
        year = input("Enter Year: ")
        course = input("Enter Course: ")

        student_data = [id_number, first_name, last_name, gender, year, course]
        append_student_data(student_data)

    print("\n Student Data written successfully.")

def is_student_exists(id_number):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id_number:
                return True
    return False

def append_student_data(data):
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def list_student_data():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print("\n Student Data listed successfully.")

def edit_student_data():
    while True:
        id_number = input("\n Enter ID Number to edit (or 'q' to quit): ")
        if id_number == 'q':
            break

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
    while True:
        id_number = input("\n Enter ID Number to delete (or 'q' to quit): ")
        if id_number == 'q':
            break

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
    while True:
        year = input("\n Enter the Year of student (or 'q' to quit): ")
        if year == 'q':
            break

        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[4] == year:
                    print(row)
                    found = True
            if not found:
                print("Student does not exist.")

def search_student_name():
    while True:
        name = input("\n Enter the first name of student (or 'q' to quit): ")
        if name == 'q':
            break

        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if name.lower() in row[1].lower() or name.lower() in row[2].lower():
                    print(row)
                    found = True
            if not found:
                print("Student does not exist.")

def write_course_data():
    while True:
        course_code = input("\n Enter Course Code (or 'q' to quit): ")
        if course_code == 'q':
            break

        if does_course_exists(course_code):
            print("This course already exists.")
            continue

        name = input("Enter Name: ")
        college = input("Enter College: ")
        course_data = [course_code, name, college]
        append_course_data(course_data)

    print("\n Course Data written successfully.")

def does_course_exists(course_code):
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == course_code:
                return True
    return False

def append_course_data(data):
    with open('courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def list_course_data():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print("\n Course Data listed successfully.")

def edit_course_data():
    while True:
        course_code = input("\n Enter Course Code to edit (or 'q' to quit): ")
        if course_code == 'q':
            break

        courses_data = []
        found = False

        with open('courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_code:
                    name = input("Enter new Name: ")
                    college = input("Enter new College: ")
                    courses_data.append([row[0], name, college])
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
    while True:
        course_code = input("\n Enter Course Code to delete (or 'q' to quit): ")
        if course_code == 'q':
            break

        courses_data = []
        found = False

        with open('courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_code:
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
    while True:
        course_code = input("\n Enter the Course Code to search course (or 'q' to quit): ")
        if course_code == 'q':
            break

        with open('courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_code:
                    print(row)

main_menu()
