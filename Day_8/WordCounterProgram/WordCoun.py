# Word Counter Program
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results.




file = open("article.txt", "r")

content = file.read()

words = content.split()
word_count = len(words)

line_count = len(content.splitlines())

character_count = len(content)

print("Total Words:", word_count)
print("Total Lines:", line_count)
print("Total Characters:", character_count)

file.close()
