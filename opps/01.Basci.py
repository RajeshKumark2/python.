class BankAccount: 
    def __init__(self, balance=0):
        self.__balance = balance

    def deposite(self, amount): 
        self.__balance += amount 

    def withdraw(self, amount):
        if amount <= self.__balance: 
            self.__balance -+ amount 
        else:
            raise ValueError("Insufficient funds")
    @property
    def balance(self):
        return self.__balance 
account = BankAccount(1000)
account.deposite(40)
print(account.balance)

