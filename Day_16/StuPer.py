# Student Performance Dashboard
Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

# 1. Line Graph
plt.plot(students, marks, marker='o')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.bar(students, marks)
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart
passed = np.sum(marks > 50)
failed = np.sum(marks <= 50)

plt.pie([passed, failed],
        labels=["Pass", "Fail"],
        autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()

# 4. Histogram
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()
