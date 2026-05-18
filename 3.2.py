## testing

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} Kmph")

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
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
        print(f"Single Seat: {self.single_seat}")


