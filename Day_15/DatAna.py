#   Data Analysis Tool (NumPy + Pandas)
Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print result


import numpy as np
import pandas as pd

# Generate student marks
marks = np.random.randint(30, 101, 10)

# Create DataFrame
df = pd.DataFrame({
    "Student": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],
    "Marks": marks
})

print("Student Data:")
print(df)

# Filter passing students
passing_students = df[df["Marks"] >= 40]

print("\nPassing Students:")
print(passing_students)

# Calculate mean
average = np.mean(marks)

print("\nAverage Marks:", average)

# Print individual results
print("\nStudent Results:")

for index, row in df.iterrows():

    if row["Marks"] >= 40:
        print(row["Student"], "- Pass")
    else:
        print(row["Student"], "- Fail")
