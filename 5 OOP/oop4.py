# Add a __str__ method so that print(student) gives readable output. 

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

student = Student("Ali", 20, 75)
print(student)
