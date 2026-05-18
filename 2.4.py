class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # fully public

s = Student("Ravi", 85)

# no rules
s.marks = -999       
s.marks = "hello"    
s.marks = 999999     

print(s.marks)