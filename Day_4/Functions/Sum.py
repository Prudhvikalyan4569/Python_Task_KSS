# Write a function to find the sum of elements in a list using a user-defined function.


def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

numbers = [10, 20, 30, 40, 50]

print("Sum of list elements:", list_sum(numbers))
