#  University Staff Management (Hierarchical Inheritance)
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information.



# Base Class
class Staff:
    def __init__(self, name, staff_id, salary):
        self.name = name
        self.staff_id = staff_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Staff ID:", self.staff_id)
        print("Salary:", self.salary)


# Derived Class 1
class Professor(Staff):
    def __init__(self, name, staff_id, salary, subject):
        super().__init__(name, staff_id, salary)
        self.subject = subject

    def display(self):
        print("\n--- Professor Details ---")
        super().display()
        print("Subject:", self.subject)


# Derived Class 2
class LabAssistant(Staff):
    def __init__(self, name, staff_id, salary, lab_name):
        super().__init__(name, staff_id, salary)
        self.lab_name = lab_name

    def display(self):
        print("\n--- Lab Assistant Details ---")
        super().display()
        print("Lab Name:", self.lab_name)


# Derived Class 3
class Administrator(Staff):
    def __init__(self, name, staff_id, salary, department):
        super().__init__(name, staff_id, salary)
        self.department = department

    def display(self):
        print("\n--- Administrator Details ---")
        super().display()
        print("Department:", self.department)


# Creating Objects
p = Professor("Ravi", 101, 50000, "Python")
l = LabAssistant("Kiran", 102, 30000, "Computer Lab")
a = Administrator("Suresh", 103, 40000, "HR")

# Displaying Details
p.display()
l.display()
a.display()



