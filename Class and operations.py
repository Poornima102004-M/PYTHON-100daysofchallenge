class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} units. New balance is {self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} units. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

def main():
    # Create a new bank account
    account1 = BankAccount("1234567890", "John Doe")
    
    # Perform operations on the account
    account1.display_balance()  # Display initial balance (0)
    account1.deposit(1000)      # Deposit 1000 units
    account1.withdraw(500)      # Withdraw 500 units
    account1.display_balance()  # Display remaining balance

if __name__ == "__main__":
    main()
