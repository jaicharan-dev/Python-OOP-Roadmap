class Bank_account:
    def __init__(self, owner_name, account_number, balance = 0):
        self.owner_name = owner_name
        self._account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print(ValueError("Deposit amount must be positive"))
         
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print(ValueError("Withdrawal amount must be positive and less than balance")) 
    
    def get_balance(self):
        print(self.__balance)
    
    def get_account_info(self):
        print(f"Owner Name: {self.owner_name} | Account Number: *****{self._account_number[-4:]}")



account_1 = Bank_account("Jaicharan", "123456789", 1000)

account_1.deposit(1000)
account_1.withdraw(5000)
account_1.withdraw(500)
account_1.get_balance()
account_1.get_account_info()
print(account_1._Bank_account__balance)

