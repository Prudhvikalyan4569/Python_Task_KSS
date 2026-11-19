# Online Shopping System (Multilevel Inheritance)
An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details.




class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def display_electronic(self):
        print("Brand:", self.brand)


class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, model):
        super().__init__(name, price, brand)
        self.model = model

    def display_mobile(self):
        self.display_product()
        self.display_electronic()
        print("Model:", self.model)


# Creating an object
mobile = MobilePhone("Smartphone", 25000, "Samsung", "Galaxy S24")

# Displaying details
mobile.display_mobile()
