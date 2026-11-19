# Performance Tracker (Decorators)
A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function.



import time

# Decorator to measure execution time
def performance_tracker(func):
    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()

        execution_time = end_time - start_time

        print("Execution Time:", execution_time, "seconds")

    return wrapper


@performance_tracker
def my_function():
    print("Function is executing...")
    time.sleep(2)


# Calling the function
my_function()
