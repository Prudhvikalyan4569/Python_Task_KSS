# Rectangle Area Calculator (Constructor)
A geometry application needs to calculate the area of rectangles. Create a Rectangle
class that uses a constructor to initialize length and width. Add a method to calculate
and display the area.


class Rectangle:
    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate and display area
    def calculate_area(self):
        area = self.length * self.width
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area of Rectangle:", area)


# Creating an object
rect = Rectangle(10, 5)

# Calling the method
rect.calculate_area()


