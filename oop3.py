# Inheritance: an Animal parent class, with Dog and Cat child classes that print their sound

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()