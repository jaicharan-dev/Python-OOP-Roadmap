from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
    
    @abstractmethod    
    def perimeter(self): pass 
    
    def describe(self):
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

rectangle = Rectangle(10, 5)
rectangle.describe()

circle = Circle(5)
circle.describe()

# its a blueprint, cannot create object directly from it
s = Shape()

    
