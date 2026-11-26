# . Advanced Simulation System
Scenario:
Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistic




import random
import numpy as np
import pandas as pd
import math


# Student Class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"


try:

    students = []

    names = [
        "Prudhvi",
        "Rahul",
        "Arun",
        "Kalyan",
        "Ravi",
        "Suresh",
        "Mahesh",
        "Ramesh",
        "Kiran",
        "Ajay"
    ]

    # Generate random marks
    marks = np.array([
        random.randint(0, 100)
        for i in range(10)
    ])

    # Create Student objects
    for i in range(len(names)):

        student = Student(names[i], int(marks[i]))

        students.append(student)

    # Create report
    report = []

    print("EXAM RESULTS")
    print("--------------------------")

    for student in students:

        grade = student.calculate_grade()

        print(
            student.name,
            "Marks:", student.marks,
            "Grade:", grade
        )

        report.append({
            "Name": student.name,
            "Marks": student.marks,
            "Grade": grade
        })

    # Convert into DataFrame
    df = pd.DataFrame(report)

    print("\nStudent Report:")
    print(df)

    # Calculate statistics
    average = math.ceil(np.mean(marks))

    highest = np.max(marks)

    lowest = np.min(marks)

    print("\nEXAM STATISTICS")
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    # Save report
    df.to_csv("exam_report.csv", index=False)

    with open("exam_report.txt", "w") as file:

        file.write("EXAM RESULTS\n")
        file.write(df.to_string())
        file.write("\n\nAverage Marks: " + str(average))
        file.write("\nHighest Marks: " + str(highest))
        file.write("\nLowest Marks: " + str(lowest))

    print("\nReports saved successfully!")

except Exception as e:

    print("Error occurred:", e)
