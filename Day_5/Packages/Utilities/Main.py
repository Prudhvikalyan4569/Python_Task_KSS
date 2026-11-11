# Write a Python program that imports the package and uses functions from both modules..


from utilities.math_operations import addition, multiplication
from utilities.string_operations import convert_uppercase, count_characters

# Math Operations
a = 10
b = 5

print("Addition:", addition(a, b))
print("Multiplication:", multiplication(a, b))

# String Operations
text = "python programming"

print("Uppercase:", convert_uppercase(text))
print("Character Count:", count_characters(text))
