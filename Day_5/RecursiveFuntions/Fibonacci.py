# Write a recursive function to find the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a number: "))
print("Fibonacci number:", fibonacci(num))
