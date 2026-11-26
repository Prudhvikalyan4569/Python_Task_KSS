# Random Number Analyzer
Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates



import random

# Generate 10 random numbers
numbers = []

for i in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

print("Random Numbers:", numbers)

even = 0
odd = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Remove duplicates
unique_numbers = set(numbers)

print("Even Numbers Count:", even)
print("Odd Numbers Count:", odd)
print("Unique Numbers:", unique_numbers)
