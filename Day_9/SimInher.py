# Employee Salary System (Simple Inheritance)
A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details.


# Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Derived Class
class Manager(Employee):
    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


# Creating Manager Object
m1 = Manager("Prudhvi", 50000)

# Displaying Employee Details
m1.display()


