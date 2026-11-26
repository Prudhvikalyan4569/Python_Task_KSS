# . Basic File Logger
Scenario:
A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling



try:
    while True:

        log = input("Enter user activity (type exit to stop): ")

        if log.lower() == "exit":
            break

        with open("user_logs.txt", "a") as file:
            file.write(log + "\n")

        print("Log saved successfully!")

except OSError as e:
    print("File Error:", e)

print("Logging completed!")
