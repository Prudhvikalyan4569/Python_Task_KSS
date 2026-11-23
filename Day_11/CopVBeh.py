# Copy vs View Behavior in Data Processing
Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference.


import numpy as np

arr = np.array([10, 20, 30, 40])

# Copy
copy_arr = arr.copy()

arr[0] = 100

print("Original Array:", arr)
print("Copy Array:", copy_arr)

# View
arr2 = np.array([10, 20, 30, 40])

view_arr = arr2.view()

arr2[0] = 200

print("Original Array:", arr2)
print("View Array:", view_arr)

