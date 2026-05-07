class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, Roll No: {self.roll_number}, Branch: {self.branch}")
    
student1 = Student("Jaicharan", 231124, "Civil" )
student2 = Student("Agni", 123104, "Civil")

student1.introduce()
student2.introduce()
