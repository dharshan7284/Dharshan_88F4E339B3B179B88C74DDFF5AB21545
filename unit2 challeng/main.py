class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}"
        else:
            return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}"
        elif amount <= 0:
            return "Withdrawal amount must be greater than 0."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
       return (f"Account number:{self.__account_number} HolderName:{self.__account_holder_name} balance:₹{self.__account_balance:}")
account1 = BankAccount("12345", "karthik", 1000)
print(account1.display_balance())
print(account1.deposit(500))
print(account1.withdraw(200))