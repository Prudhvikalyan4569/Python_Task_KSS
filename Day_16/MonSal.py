# Monthly Sales Analysis
Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sales data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

# 1. Line Graph
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 2. Bar Chart
plt.bar(months, sales)
plt.title("Month-wise Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart
plt.pie(sales,
        labels=months,
        autopct="%1.1f%%")
plt.title("Monthly Sales Contribution")
plt.show()

# 4. Histogram
plt.hist(sales, bins=5, edgecolor="black")
plt.title("Sales Frequency Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(range(len(sales)), sales)
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.show()
