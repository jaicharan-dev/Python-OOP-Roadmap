class UserSubscription:
    def __init__(self, user_name, plan_tier, monthly_cost):
        self.user_name = user_name
        # PRO-TIP: We assign to the property names (no underscores) 
        # so the initial values are also validated by the setters!
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
            raise ValueError(f"Invalid plan tier: '{plan}'. Must be Free, Basic, or Pro.")
        
    @property
    def monthly_cost(self):
        return self.__monthly_cost
    
    @monthly_cost.setter
    def monthly_cost(self, cost):
        if cost >= 0:
            self.__monthly_cost = cost
        else:
            raise ValueError(f"Invalid cost: {cost}. Cost cannot be negative.")

# --- Testing the Object (The Professional Way) ---
if __name__ == "__main__":
    print("--- 1. Initializing User ---")
    user1 = UserSubscription("Rahul", "Free", 0)
    print(f"User: {user1.user_name} | Plan: {user1.plan_tier} | Cost: {user1.monthly_cost}")

    print("\n--- 2. Testing Valid Change ---")
    user1.plan_tier = "Pro"
    user1.monthly_cost = 20.0
    print(f"Upgrade Success! New Plan: {user1.plan_tier}, New Cost: {user1.monthly_cost}")

    print("\n--- 3. Testing Encapsulation (Invalid Inputs) ---")

    # We use try/except so the script doesn't stop after the first error
    try:
        print("Attempting to set a negative cost...")
        user1.monthly_cost = -100
    except ValueError as e:
        print(f"Blocked! Error: {e}")

    try:
        print("\nAttempting to set an invalid plan...")
        user1.plan_tier = "Ultra"
    except ValueError as e:
        print(f"Blocked! Error: {e}")

    print("\n--- 4. Final State Verification ---")
    # Notice that despite the "bad" attempts above, the user data stayed safe!
    print(f"Current Plan: {user1.plan_tier} (Still Pro)")
    print(f"Current Cost: {user1.monthly_cost} (Still 20.0)")