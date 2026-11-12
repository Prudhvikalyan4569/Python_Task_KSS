# Write a program to check whether a number is a Palindrome.


num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a Palindrome number")
else:
    print(original, "is not a Palindrome number")
