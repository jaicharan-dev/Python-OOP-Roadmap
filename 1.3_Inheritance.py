# --- Parent Class (SuperClass) ---
class UserSubscription:
    def __init__(self, user_name, plan_tier, monthly_cost):
        self.user_name = user_name
        self.plan_tier = plan_tier
        self.monthly_cost = monthly_cost

    @property
    def plan_tier(self):
        return self.__plan_tier

    @plan_tier.setter
    def plan_tier(self, plan):
        if plan in ["Free", "Basic", "Pro"]:
            self.__plan_tier = plan
        else:
            raise ValueError("Invalid plan tier")
    
    @property
    def monthly_cost(self):
        return self.__monthly_cost
    
    @monthly_cost.setter
    def monthly_cost(self, cost):
        if cost >= 0:
            self.__monthly_cost = cost
        else:
            raise ValueError("cost cannot be negative")
        
# --- Child Class (Inheritance) ---
class PremiumSubscription(UserSubscription):
    def __init__(self, user_name, plan_tier, monthly_cost, max_devices):
        super().__init__(user_name, plan_tier, monthly_cost)
        self.max_devices = max_devices
        self.__active_devices = 0

    def add_device(self):
        if self.__active_devices < self.max_devices:
            self.__active_devices += 1
            print(f"Success: Device added. Total active: {self.__active_devices}/{self.max_devices}")
        else:
            print(f"Error: Device limit of {self.max_devices} reached! Cannot add more.")
        
# --- Testing the inheritance ---
if __name__ == "__main__":
    print("---1. Creating Premium User ---")
    priya_account = PremiumSubscription("Priya", "Pro", 20.0, 2)
    print(f"Created account for {priya_account.user_name} with {priya_account.max_devices} max devices.")
    
    print("\n--- 2. Testing Inheritance Encapsulation ---")
    try:
        priya_account.monthly_cost = -50
    except ValueError as e:
        print(f"Security Worked! Blocked bad cost: {e}")

    print("\n--- 3. Testing Child Behaviour ---")
    priya_account.add_device()
    priya_account.add_device()
    priya_account.add_device()



