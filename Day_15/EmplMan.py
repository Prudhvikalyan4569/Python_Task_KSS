#  Employee Management System (OOP + File + Dict)
Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees


class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        try:
            salary = float(input("Enter Employee Salary: "))

            if salary < 0:
                raise ValueError("Salary cannot be negative")

            emp = Employee(emp_id, name, salary)

            employees[emp_id] = emp

        except ValueError as e:
            print("Invalid Salary:", e)

    # Save employee data
    with open("employees.txt", "w") as file:

        for emp in employees.values():
            file.write(
                f"{emp.emp_id}, {emp.name}, {emp.salary}\n"
            )

    # Display employees
    print("\nEmployee Details:")

    for emp in employees.values():
        print("ID:", emp.emp_id)
        print("Name:", emp.name)
        print("Salary:", emp.salary)
        print("----------------")

except ValueError:
    print("Please enter a valid number of employees.")
