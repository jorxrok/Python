# Implement a simple banking application:
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rupees {amount}. Current balance: Rupees {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rupees {amount}. Current balance: Rupees {self.balance}")
        else:
            print("Insufficient funds!")

    def compute_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(f"Interest computed. Current balance: Rupees {self.balance}")

    def display_balance(self):
        print(f"Current balance: Rupees {self.balance}")


# Example usage:
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.compute_interest(2)
account.display_balance()
