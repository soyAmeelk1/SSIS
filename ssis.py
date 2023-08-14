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
        print("\nStudent Menu")
        print("1. Write Student Data")
        print("2. List Student Data")
        print("3. Edit Student Data")
        print("4. Delete Student Data")
        print("5. Search Student by Year Data")
        print("6. Search Student by Name Data")
        print("7. Back to Main Menu")

        choice = input("\nEnter your choice (1-7): ")

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
            print("\nInvalid choice. Please try again.")

def course_menu():
    while True:
        print("\nCourse Menu")
        print("1. Write Course Data")
        print("2. List Course Data")
        print("3. Edit Course Data")
        print("4. Delete Course Data")
        print("5. Search Course")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice (1-6): ")

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
            print("\nInvalid choice. Please try again.")

def write_student_data():
    while True:
        id_number = input("\nEnter ID Number (or 'q' to quit): ")
        if id_number == 'q':
            break

        if is_student_exists(id_number):
            print("This student already exists.")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        gender = input("Enter Gender: ")
        year = input("Enter Year: ")
        course = input("Enter Course Name: ")

        student_data = [id_number, first_name, last_name, gender, year, course]
        append_student_data(student_data)

    print("\nStudent Data written successfully.")

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
        id_number = input("\nEnter ID Number to edit (or 'q' to quit): ")
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
        id_number = input("\nEnter ID Number to delete (or 'q' to quit): ")
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
        year = input("\nEnter the Year of student (or 'q' to quit): ")
        if year == 'q':
            break

        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[4].strip() == year.strip():  # Use strip() to remove whitespace
                    print(row[:-1])  # Exclude the last element (course) in the output
                    found = True
            if not found:
                print("Student does not exist.")

def search_student_name():
    while True:
        name = input("\nEnter the first name of student (or 'q' to quit): ")
        if name == 'q':
            break

        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if name.lower() in row[1].lower() or name.lower() in row[2].lower():
                    print(row[:-1])  # Exclude the last element (course) in the output
                    found = True
            if not found:
                print("Student does not exist.")

def write_course_data():
    while True:
        course_name = input("\nEnter Course Name (or 'q' to quit): ")
        if course_name == 'q':
            break

        if does_course_exists(course_name):
            print("This course already exists.")
            continue

        course_code = input("Enter Course Code: ")
        college = input("Enter College: ")
        course_data = [course_name, course_code, college]
        append_course_data(course_data)

        print("\nCourse Data written successfully.")

def does_course_exists(course_name):
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == course_name:
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
    print("\nCourse Data listed successfully.")

def edit_course_data():
    while True:
        course_name = input("\nEnter Course Name to edit (or 'q' to quit): ")
        if course_name == 'q':
            break

        courses_data = []
        found = False

        with open('courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_name:
                    code = input("Enter new code: ")
                    college = input("Enter new College: ")
                    courses_data.append([course_name, code, college])
                    found = True
                else:
                    courses_data.append(row)

        if found:
            with open('courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(courses_data)
            print("Course data updated successfully.")
        else:
            print("Course not found.")

def delete_course_data():
    while True:
        course_name = input("\nEnter Course Name to delete (or 'q' to quit): ")
        if course_name == 'q':
            break

        courses_data = []
        students_data = []  # Collect students not enrolled in the deleted course

        found = False

        with open('courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_name:
                    found = True
                else:
                    courses_data.append(row)

        if found:
            with open('courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(courses_data)

            with open('students.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[5] != course_name:  # Keep students not enrolled in the deleted course
                        students_data.append(row)

            with open('students.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(students_data)

            print("Course data and associated student data deleted successfully.")
        else:
            print("Course not found.")

        # Call the main menu to return to the main program loop
        main_menu()

def search_courses():
    while True:
        search_query = input("\nEnter a Course Code or Name (or 'q' to quit): ")
        if search_query == 'q':
            break

        with open('courses.csv', 'r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if search_query.lower() in row[0].lower() or search_query.lower() in row[1].lower():
                    print(row)
                    found = True
            if not found:
                print("Course not found.")

main_menu()
