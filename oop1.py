# Create a Student class with name, age, marks, and a method that returns pass/fail. 

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student1 = Student("Ali", 20, 75)
student2 = Student("Sara", 19, 35)

print(student1.name, student1.result())
print(student2.name, student2.result())
