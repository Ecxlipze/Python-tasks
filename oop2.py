# Create a BankAccount class with deposit/withdraw methods; balance must never go negative

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
        else:
            return "Not enough balance"

account = BankAccount(1000)

print("Starting balance:", account.balance)
print("After deposit:", account.deposit(500))
print("After withdraw:", account.withdraw(300))
print(account.withdraw(2000))
print("Final balance:", account.balance)
