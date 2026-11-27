# Data Cleaning + Visualization
Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert into Pandas Series
s = pd.Series(data)

print("Original Data:")
print(s)

# Replace NaN with Mean
mean_value = s.mean()

cleaned_data = s.fillna(mean_value)

print("\nCleaned Data:")
print(cleaned_data)

# Calculate Average
average = cleaned_data.mean()

print("\nAverage:", average)

# Filter Values Greater Than Average
filtered_data = cleaned_data[cleaned_data > average]

print("\nValues Greater Than Average:")
print(filtered_data)

# Create Subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Line Graph
axes[0].plot(cleaned_data, marker='o')
axes[0].set_title("Cleaned Data Line Graph")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")
axes[0].grid(True)

# Bar Chart
axes[1].bar(filtered_data.index, filtered_data.values)
axes[1].set_title("Values Above Average")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")

plt.tight_layout()

plt.show()
