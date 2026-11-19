# Employee Bonus Calculator (Decorators & OOP)
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it.



def bonus_decorator(func):
    def wrapper(self):
        salary = func(self)
        bonus = salary * 0.10
        total_salary = salary + bonus

        print("Basic Salary:", salary)
        print("Bonus:", bonus)
        print("Total Salary:", total_salary)

    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus_decorator
    def display_salary(self):
        return self.salary


# Creating an object
emp = Employee("Prudhvi", 30000)

print("Employee Name:", emp.name)
emp.display_salary()
