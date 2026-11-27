# Product Sales & Profit Analysis
Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Product data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

# 1. Line Graph
plt.plot(products, sales, marker='o')
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 2. Bar Chart
plt.bar(products, sales)
plt.title("Product vs Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart
plt.pie(sales,
        labels=products,
        autopct="%1.1f%%")
plt.title("Product Sales Contribution")
plt.show()

# 4. Histogram
plt.hist(profit, bins=5, edgecolor="black")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(sales, profit)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
