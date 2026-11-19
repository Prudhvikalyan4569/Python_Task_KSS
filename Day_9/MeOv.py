# Student Result Generator (Method Overloading Concept)
A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subjects.




class Result:

    def calculate(self, m1, m2, m3=None):

        if m3 is None:
            total = m1 + m2
            average = total / 2
            print("Total Marks:", total)
            print("Average Marks:", average)

        else:
            total = m1 + m2 + m3
            average = total / 3
            print("Total Marks:", total)
            print("Average Marks:", average)


# Creating object
r = Result()

# Calculating result using two subjects
print("Result for Two Subjects:")
r.calculate(80, 90)

# Calculating result using three subjects
print("\nResult for Three Subjects:")
r.calculate(80, 90, 85)
