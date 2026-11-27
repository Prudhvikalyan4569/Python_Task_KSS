# Temperature Monitoring System
Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Temperature data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

# 1. Line Graph
plt.plot(days, temps, marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

# 2. Bar Chart
plt.bar(days, temps)
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

# 3. Pie Chart
high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.pie([high, low],
        labels=["High Temperature", "Low Temperature"],
        autopct="%1.1f%%")
plt.title("High vs Low Temperature")
plt.show()

# 4. Histogram
plt.hist(temps, bins=5, edgecolor="black")
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(range(len(temps)), temps)
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")
plt.show()
