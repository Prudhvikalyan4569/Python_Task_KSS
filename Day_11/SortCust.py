# Sorting Customer Names
A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically.



import numpy as np

names = ["Ravi", "Anil", "Sita", "John"]

arr = np.array(names)

sorted_names = np.sort(arr)

print("Sorted Names:", sorted_names)
