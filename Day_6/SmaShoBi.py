# Develop a Python program for a small shop to process customer purchases. Store product
names and prices in a dictionary, items added to the cart in a list, product categories in a set,
and product details using tuples. Create functions to display products, add items to the cart, and
calculate the total bill. Use a recursive function to compute the total price of all items in the cart.
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist).




# Store product names and prices in a dictionary
products = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 150,
    "Milk": 30,
    "Soap": 40
}

# Store product categories in a set
categories = {"Groceries", "Dairy", "Household"}

# Store product details using tuples
product_details = (
    ("Rice", "Groceries"),
    ("Sugar", "Groceries"),
    ("Oil", "Groceries"),
    ("Milk", "Dairy"),
    ("Soap", "Household")
)

# Store cart items in a list
cart = []


# Function to display products
def display_products():
    print("\n----- AVAILABLE PRODUCTS -----")

    for name, price in products.items():
        print(name, ":", price)


# Function to add items to cart
def add_to_cart():
    try:
        product_name = input("\nEnter product name: ")

        if product_name not in products:
            raise NameError("Product does not exist!")

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")

        price = products[product_name]

        cart.append((product_name, quantity, price))

        print("Item added to cart successfully!")

    except ValueError:
        print("Error: Please enter a valid quantity!")

    except NameError as e:
        print("Error:", e)


# Recursive function to calculate total price
def calculate_total(items, index=0):

    if index == len(items):
        return 0

    if not isinstance(items[index], tuple):
        raise TypeError("Cart must contain tuples!")

    name, quantity, price = items[index]

    if not isinstance(quantity, (int, float)):
        raise TypeError("Invalid quantity data type!")

    if not isinstance(price, (int, float)):
        raise TypeError("Invalid price data type!")

    return (quantity * price) + calculate_total(items, index + 1)


# Function to calculate and display bill
def calculate_bill():
    try:
        total = calculate_total(cart)

        print("\n-------- CUSTOMER BILL --------")

        for name, quantity, price in cart:
            print(name, "x", quantity, "=", quantity * price)

        print("-------------------------------")
        print("Total Bill: Rs.", total)

        # Calculate average item price
        average = total / len(cart)

        print("Average Item Price: Rs.", average)

    except ZeroDivisionError:
        print("Error: Cart is empty. Cannot calculate average!")

    except TypeError as e:
        print("Error:", e)


# Main program
while True:

    print("\n===== SMALL SHOP BILLING SYSTEM =====")
    print("1. Display Products")
    print("2. Add Item to Cart")
    print("3. Calculate Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            calculate_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter numbers only!")
