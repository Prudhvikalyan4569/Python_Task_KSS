# Student Attendance Record
A teacher wants to store student attendance in a file named attendance.txt. Write a
Python program that takes a student name as input and appends it to the file. Then
display the contents of the file.


# Function to add student name to the file
def add_student():
    name = input("Enter student name: ")

    with open("attendance.txt", "a") as file:
        file.write(name + "\n")

    print("Student attendance added successfully!")


# Function to display attendance records
def display_attendance():
    print("\nStudent Attendance Records:")

    with open("attendance.txt", "r") as file:
        content = file.read()
        print(content)


# Main program
add_student()
display_attendance()

