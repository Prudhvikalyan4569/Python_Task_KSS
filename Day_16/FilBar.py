# Filtered Bar Chart
Scenario:
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
Task:
● Convert to DataFrame
● Filter students with marks > 50
● Plot bar chart only for filtered student



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

filtered_df = df[df["Marks"] > 50]

print("Filtered Students:")
print(filtered_df)

plt.bar(filtered_df["Student"], filtered_df["Marks"])

plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Students Scoring Above 50")

plt.show()
