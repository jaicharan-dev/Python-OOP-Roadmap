class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def clock_in(self):
        print(f"{self.name} has clocked in")

    def get_details(self):
        return f"{self.name} makes ${self.salary}/year"
    
class SoftwareEngineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def write_code(self):
        print(f"{self.name} is writing {self.programming_language} code")

# method overriding    
class CEO(Employee):
    # We are overriding the parent's clock_in method
    def clock_in(self):
        print(f"{self.name} just arrived in a helicopter. No need to clock in.")

sde = SoftwareEngineer("Jaicharan", 12000, "Python")
sde.clock_in()
sde.write_code()

