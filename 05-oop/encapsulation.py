class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Insufficient funds"
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(f"Balance: ${account.get_balance()}")
