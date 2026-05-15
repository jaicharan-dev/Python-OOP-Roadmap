class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
        self.__pin = 1234

    def get_marks(self, pin):
        if pin == self.__pin:
            return self.__marks
        return "wrong pin"

    def set_marks(self, pin, marks):
        if pin == self.__pin:
            self.__marks = marks
    
    @property
    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        else:
            return "F"

# test

s = Student("Ravi", 85)
print(s.get_marks(1234))   
print(s.grade)            
s.set_marks(1234, 95)
print(s.grade)  