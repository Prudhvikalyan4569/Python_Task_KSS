# Write a program to perform left shift (<<) and right shift (>>) operations on a number.


num = int(input("Enter a number: "))
shift = int(input("Enter shift position: "))

left_shift = num << shift
right_shift = num >> shift

print("Left Shift result:", left_shift)
print("Right Shift result:", right_shift)
