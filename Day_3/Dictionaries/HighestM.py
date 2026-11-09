#  Write a program to find the student with the highest marks from a dictionary.


students = {
    "Prudhvi": 85,
    "Rahul": 90,
    "Kiran": 78
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Highest Marks:", students[topper])
