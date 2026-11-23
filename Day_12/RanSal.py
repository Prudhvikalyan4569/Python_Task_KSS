# Random Sales Simulation
Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.



import numpy as np

sales = np.random.randint(100, 501, size=10)

average_sales = np.mean(sales)

print("10 Days Sales:", sales)
print("Average Sales:", average_sales)
