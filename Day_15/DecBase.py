# Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary


users = {
    "Prudhvi": "admin",
    "Rahul": "user",
    "Arun": "manager"
}


def check_role(required_role):

    def decorator(func):

        def wrapper(username):

            if username in users:

                if users[username] == required_role:
                    return func(username)

                else:
                    print("Access Denied!")

            else:
                print("User not found!")

        return wrapper

    return decorator


@check_role("admin")
def delete_data(username):
    print(username, "can delete data")


@check_role("manager")
def view_reports(username):
    print(username, "can view reports")


@check_role("admin")
def add_employee(username):
    print(username, "can add employees")


# Function calls
delete_data("Prudhvi")
view_reports("Arun")
add_employee("Rahul")
