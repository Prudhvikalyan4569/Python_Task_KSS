#  Smart Data Processing Pipeline
Scenario:
A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time




import numpy as np
import pandas as pd
import time


# Decorator to measure execution time
def execution_time(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start, "seconds")

        return result

    return wrapper


# Generator to read numbers
def read_numbers(filename):

    with open(filename, "r") as file:

        for line in file:

            try:
                yield float(line.strip())

            except ValueError:
                print("Invalid data:", line.strip())


@execution_time
def process_data():

    numbers = []

    try:

        for num in read_numbers("numbers.txt"):
            numbers.append(num)

        if len(numbers) == 0:
            print("No valid numbers found!")
            return

        # NumPy calculations
        arr = np.array(numbers)

        mean = np.mean(arr)
        std = np.std(arr)

        # Convert results into DataFrame
        df = pd.DataFrame({
            "Numbers": arr
        })

        print("DataFrame:")
        print(df)

        print("\nMean:", mean)
        print("Standard Deviation:", std)

        result_df = pd.DataFrame({
            "Mean": [mean],
            "Standard Deviation": [std]
        })

        result_df.to_csv("analysis_results.csv", index=False)

        print("\nResults saved successfully!")

    except FileNotFoundError:
        print("File not found!")

    except OSError as e:
        print("File Error:", e)


process_data()
