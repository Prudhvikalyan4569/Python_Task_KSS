# Develop a Python program to manage student marks for three subjects. Store the subject
names in a tuple, maintain unique student names in a set, and store each student’s marks
in a list inside a dictionary where the key is the student name. Create user-defined
functions to add a student with marks, display all student records, and calculate the average
marks of a student. Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu. Also include
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
student name entered does not exist in the dictionary).




# Student Marks Management System

# Store subject names in a tuple
subjects = ("Python", "Java", "SQL")

# Store unique student names in a set
student_names = set()

# Store student marks in a dictionary
students = {}


# Recursive function to calculate total marks
def calculate_total(marks):
    if len(marks) == 0:
        return 0
    return marks[0] + calculate_total(marks[1:])


# Function to add a student
def add_student():
    try:
        name = input("Enter student name: ")

        if name in student_names:
            print("Student already exists!")
            return

        marks = []

        for subject in subjects:
            mark = float(input(f"Enter marks in {subject}: "))
            marks.append(mark)

        student_names.add(name)
        students[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter numeric marks only!")

    except TypeError:
        print("Error: Incorrect data type in marks!")


# Function to display all student records
def display_students():
    if not students:
        print("No student records found!")
        return

    print("\n----- Student Records -----")

    for name, marks in students.items():
        print("Student Name:", name)

        for i in range(len(subjects)):
            print(subjects[i], ":", marks[i])

        print("Total Marks:", calculate_total(marks))
        print("------------------------")


# Function to calculate average marks
def calculate_average():
    try:
        name = input("Enter student name: ")

        if name not in students:
            raise NameError("Student name does not exist!")

        marks = students[name]

        total = calculate_total(marks)

        average = total / len(marks)

        print("Student Name:", name)
        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except TypeError:
        print("Error: Incorrect data type in marks!")


# Main menu
while True:

    print("\n===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Average Marks")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank you! Program exited.")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Error: Please enter a valid menu number!")
