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

class EmailNotifier:
    def send_reminder(self, user_name):
        print(f"[Email] Sending renewal link to user: {user_name}")

class SMSNotifier:
    def send_reminder(self, user_name):
        print(f"[SMS] Texting renewal alert to user: {user_name}")
class PushNotifier:
    def send_reminder(self, user_name):
        print(f"[Push] Pinging app notification for user: {user_name}")
    
def trigger_notification(notifier_object, user_name):
    notifier_object.send_reminder(user_name)

# --- Testing the inheritance ---

if __name__ == "__main__":
    print("--- 1. Creating Notifier Objects ---")
    # First, we instantiate one of each 'duck'
    email_system = EmailNotifier()
    sms_system = SMSNotifier()
    push_system = PushNotifier()

    print("\n--- 2. Building the Preferences List ---")
    # Even though these are three completely different classes, 
    # Python lets us group them into a single list.
    user_preferences = [email_system, sms_system, push_system]

    print("\n--- 3. Testing Polymorphism (The Loop) ---")
    # We iterate through the list. The trigger function doesn't know or care 
    # WHICH class it is dealing with at any given moment!
    for notifier in user_preferences:
        trigger_notification(notifier, "Alex")