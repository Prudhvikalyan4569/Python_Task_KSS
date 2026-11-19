# Vehicle Management System (Inheritance)
A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details.




# Base Class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

# Derived Class - Car
class Car(Vehicle):
    def display(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")

# Derived Class - Bike
class Bike(Vehicle):
    def display(self):
        print("\nBike Details:")
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")


# Creating Objects
car1 = Car("Toyota", 180)
bike1 = Bike("Royal Enfield", 120)

# Displaying Details
car1.display()
bike1.display()
