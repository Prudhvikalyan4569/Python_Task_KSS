# Write a program to check whether a string is a palindrome.


string = input("Enter a string: ")

if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
