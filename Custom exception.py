# Define a custom exception class
class WithdrawalError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Insufficient balance of {balance}")

# Example banking account class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise WithdrawalError(self.balance, amount)
        else:
            self.balance -= amount
            return self.balance

# Example usage
try:
    account = BankAccount(100)
    print("Current balance:", account.balance)
    withdraw_amount = 150
    remaining_balance = account.withdraw(withdraw_amount)
    print(f"Withdrew {withdraw_amount}. Remaining balance:", remaining_balance)
except WithdrawalError as e:
    print("Withdrawal Error:", e)
