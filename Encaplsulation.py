class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance #private 

    def get_balance(self):
        return self.__balance 
    
    def deposit(self, amount): 
        if amount > 0:
            self.__balance += amount 
        else:
            raise ValueError("Amount must be positive")
        
    @property 
    def formatted_balance(self): 
        return f"${self.__balance:.2f}"
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())
print(account.formatted_balance)
