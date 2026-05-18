class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__pin = 1234

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return (f"Deposit successful. New balance: {self.__balance}")
        else:
            return ("Deposit amount must be positive")
    
    def get_balance(self, pin):
        if pin == self.__pin:
            return (f"Balance: {self.__balance}")
        else:
            return ("Invalid PIN")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
    
# using methods
acc = BankAccount("jai", 1000)

print(acc.owner)
# print(acc.__balance) 
print(acc.get_balance(1234))
print(acc.get_balance(9999))
print(acc.deposit(500))
print(acc.balance)
acc.balance = 2000
print(acc.balance)



        

        
