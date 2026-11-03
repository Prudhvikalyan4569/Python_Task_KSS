# Write a program to find the second largest number in a list.


numbers = [10, 25, 5, 40, 15, 30]

unique_numbers = list(set(numbers))

unique_numbers.sort()

second_largest = unique_numbers[-2]

print("Second largest number:", second_largest)
