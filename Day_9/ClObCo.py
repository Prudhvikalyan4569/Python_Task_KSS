# Bank Account System (Class, Object, Constructor)
A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance.



class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# Creating Object
account1 = BankAccount(123456789, 10000)

# Performing Operations
account1.display_balance()
account1.deposit(5000)
account1.withdraw(3000)
account1.display_balance()

