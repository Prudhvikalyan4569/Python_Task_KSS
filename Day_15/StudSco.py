#  Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file




import math

students = [
    ("Prudhvi", 75),
    ("Kalyan", 45),
    ("Rahul", 85),
    ("Arun", 60),
    ("Ravi", 35)
]

# Convert list of tuples into dictionary
student_dict = dict(students)

print("Students Scoring Above 50:")

total = 0
count = 0

for name, marks in student_dict.items():
    total += marks
    count += 1

    if marks > 50:
        print(name, marks)

# Calculate average
average = math.ceil(total / count)

# Store results in text file
with open("student_results.txt", "w") as file:
    file.write("Student Results\n")

    for name, marks in student_dict.items():
        file.write(f"{name}: {marks}\n")

    file.write(f"Average Marks: {average}")

print("Average Marks:", average)
print("Results saved successfully!")
