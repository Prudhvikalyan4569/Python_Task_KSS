# Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.


students = {
    "Prudhvi": 85,
    "Rahul": 90,
    "Kiran": 80
}

# Add a new student
students["Ravi"] = 95

# Update existing student's marks
students["Rahul"] = 92

# Print all student details
for name, marks in students.items():
    print(name, ":", marks)
