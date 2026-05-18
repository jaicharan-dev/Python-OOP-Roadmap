'''
Here are your requirements:
Lock the data: Make price and is_active private variables.
The Safe Setter: Create a method called update_price(new_price). It should only update the price IF the new_price is greater than 0. Otherwise, print an error message.
The Safe Action: Create a method called cancel_subscription(). It should safely change the private is_active variable to False.
The Safe Getter: Create a method called get_details() that prints out the current price and whether the subscription is active.

class Subscription:
    def __init__(self, service_name, starting_price):
        self.service_name = service_name  # It is okay to leave the name public
        self.price = starting_price       # FIX ME: Make me private!
        self.is_active = True             # FIX ME: Make me private!

    # Add your safe methods here...
'''

''' 
# the general way to write encapsulation
class Subcription:
    def __init__(self, service_name, starting_price):
        self.service_name = service_name
        self.__price = starting_price
        self.__is_active = True
    
    def update_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than 0")
    
    def cancel_subscription(self):
        self.__is_active = False
    
    def get_details(self):
        print(f"Service: {self.service_name}, Price: {self.__price} Ruppees, Active: {self.__is_active}")
'''

# Test the class

class Subscription:
    def __init__(self, service_name, starting_price):
        self.service_name = service_name
        self.__price = starting_price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than 0")

my_sub = Subscription("YouTube Premium", 150)
my_sub.price = -50