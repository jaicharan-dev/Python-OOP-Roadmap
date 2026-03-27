"""
Topic: 1.1 Classes and Objects
Project: Digital Wallet Implementation
Goal: Demonstrate Public, Protected, and Private attributes + Name Mangling.
"""

class DigitalWallet:
    def __init__(self, user_name, currency="IND"):
        self.user_name = user_name
        self._currency = currency
        self.__balance = 0

    def __update_transaction_history(self):
        print("Internal System: Transaction recorded in ledger.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Success: Deposited {amount} {self._currency}.")
            self.__update_transaction_history()
                    
        else:
            print("Error: deposit amount must be positive")

    def show_details(self):
        print(f"--- Account Details ---")
        print(f"User: {self.user_name}")
        print(f"Balance: {self.__balance} {self._currency}")

if __name__ == "__main__":
    print("--- Starting Object Tests ---")

    my_wallet = DigitalWallet("Rahul", "INR")
    my_wallet.deposit(500)
    my_wallet.deposit(-50)
    my_wallet.show_details()

    print(f"Owner: {my_wallet.user_name}")   # orks fine
    print(f"Currency: {my_wallet._currency}") # Works, but should not touch 

    # 3. Attempting to access Private Attribute
    try:
        print(my_wallet.__balance)
    except AttributeError:
        print("\nAccess Denied: Cannot access '__balance' directly due to Name Mangling.")

    # 4. The "Dirty Trick" (Name Mangling)
    print(f"Hidden Access: {my_wallet._DigitalWallet__balance}")

    print("--- Tests Complete ---") 
