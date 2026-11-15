# Student Marks File Analyzer
A teacher stores student marks in a file marks.txt in the format:
Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class




total = 0
count = 0

file = open("marks.txt", "r")

print("Student Records:")
print("----------------")

for line in file:
    name, marks = line.split()

    marks = int(marks)

    print("Name:", name, "Marks:", marks)

    total = total + marks
    count = count + 1

file.close()

if count > 0:
    average = total / count
    print("----------------")
    print("Average Marks:", average)
else:
    print("No student records found.")
