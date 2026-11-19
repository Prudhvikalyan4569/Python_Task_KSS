# Student Information System (Class & Object)
A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details.



# Create a Student class
class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    # Method to display student details
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("----------------------")


# Create objects for three students
student1 = Student("Rahul", 101, 85)
student2 = Student("Anita", 102, 90)
student3 = Student("Ravi", 103, 78)

# Display student details
student1.display_details()
student2.display_details()
student3.display_details()
