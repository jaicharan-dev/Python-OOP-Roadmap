class Car:
    def pay_toll(self):
        return 50

class Truck:
    def pay_toll(self):
        return 150

class Motorcycle:
    def pay_toll(self):
        return 20

# --- THE POLYMORPHIC ACTION ---
# This function doesn't care what type of vehicle passes through.
# It only cares that the vehicle has a 'pay_toll()' method.

def process_vehicle(vehicle):
    cost = vehicle.pay_toll()
    print(f"Vehicle processed. Toll collected: {cost} Rupees.")


# testing it:
my_car = Car()
my_truck = Truck()
my_bike = Motorcycle()

# We pass completely different objects into the exact same function!
process_vehicle(my_car)   # Output: Vehicle processed. Toll collected: 50 Rupees.
process_vehicle(my_truck) # Output: Vehicle processed. Toll collected: 150 Rupees.
process_vehicle(my_bike)  # Output: Vehicle processed. Toll collected: 20 Rupees.