# Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-excep




cart = []

prices = {
    "apple": 30,
    "banana": 10,
    "orange": 20,
    "mango": 50
}

try:
    n = int(input("How many items do you want to add? "))

    for i in range(n):
        item = input("Enter item name: ").lower()
        cart.append(item)

    # Remove duplicates
    unique_cart = set(cart)

    total = 0

    print("\nShopping Cart:")

    for item in unique_cart:
        if item in prices:
            print(item, "-", prices[item])
            total += prices[item]
        else:
            print(item, "- Item not available")

    print("Total Cost:", total)

except ValueError:
    print("Invalid input! Please enter a number.")
