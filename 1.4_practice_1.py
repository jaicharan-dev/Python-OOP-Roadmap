## testing

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def describe(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} kmph")
    
class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand,speed)
        self.num_doors = num_doors

    def describe(self):
        super().describe()
        print(f"Doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, speed, single_seat = False):
        super().__init__(brand, speed)
        self.single_seat = single_seat

    def describe(self):
        super().describe()
        print(f"Single seat: {self.single_seat}")
    
car1 = Car("bmw", 180, 4)
car2 = Car("audi", 180, 2)
car3 = Car("rolls royce", 180, 4)

bike1 = Bike("Honda", 180, False)
bike2 = Bike("Suzuki", 180, True)
bike3 = Bike("Yamaha", 180)

vehicles = [car1, car2, car3, bike1, bike2, bike3]

for vehicle in vehicles:
    vehicle.describe()